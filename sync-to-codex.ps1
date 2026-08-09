[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$Destination,
    [string[]]$Names,
    [switch]$Prune
)

$ErrorActionPreference = 'Stop'
$repoRoot = $PSScriptRoot
$sourceRoot = Join-Path $repoRoot 'agents'

if ($Prune -and $Names) {
    throw '-Prune cannot be combined with -Names because that would remove unselected agents.'
}

if (-not $Destination) {
    if ($env:CODEX_HOME) {
        $Destination = Join-Path $env:CODEX_HOME 'agents'
    }
    else {
        $Destination = Join-Path $env:USERPROFILE '.codex\agents'
    }
}

$destinationFull = [IO.Path]::GetFullPath($Destination)
if ([string]::IsNullOrWhiteSpace($destinationFull) -or [IO.Path]::GetPathRoot($destinationFull) -eq $destinationFull) {
    throw "Unsafe destination: $Destination"
}

$packages = Get-ChildItem -LiteralPath $sourceRoot -Directory | Sort-Object Name
if ($Names) {
    $wanted = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
    foreach ($name in $Names) { [void]$wanted.Add($name) }
    $packages = @($packages | Where-Object { $wanted.Contains($_.Name) })
    $missing = @($Names | Where-Object { $_ -notin $packages.Name })
    if ($missing) { throw "Unknown agent(s): $($missing -join ', ')" }
}

if ($PSCmdlet.ShouldProcess($destinationFull, 'Create agent runtime directory')) {
    New-Item -ItemType Directory -Path $destinationFull -Force | Out-Null
}

$expected = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
foreach ($package in $packages) {
    $source = Join-Path $package.FullName 'agent.toml'
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        throw "Missing agent.toml in $($package.FullName)"
    }
    $targetName = "$($package.Name).toml"
    [void]$expected.Add($targetName)
    $target = Join-Path $destinationFull $targetName
    if ($PSCmdlet.ShouldProcess($target, "Install $($package.Name)")) {
        Copy-Item -LiteralPath $source -Destination $target -Force
    }
}

if ($Prune) {
    if (Test-Path -LiteralPath $destinationFull) {
        foreach ($file in Get-ChildItem -LiteralPath $destinationFull -File -Filter '*.toml') {
            if (-not $expected.Contains($file.Name)) {
                if ($PSCmdlet.ShouldProcess($file.FullName, 'Remove agent not present in registry')) {
                    Remove-Item -LiteralPath $file.FullName
                }
            }
        }
    }
}

Write-Host "Selected $($packages.Count) agent(s) for $destinationFull"
