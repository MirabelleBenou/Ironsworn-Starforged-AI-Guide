# Crée une copie allégée d'un export Stargazer (images base64 du journal retirées).
# L'export original n'est pas modifié. Usage : glisser le .json sur alleger_export_stargazer.bat
param([Parameter(Mandatory = $true)][string]$Path)

$src = (Resolve-Path -LiteralPath $Path).Path
$utf8 = New-Object System.Text.UTF8Encoding($false)
$text = [System.IO.File]::ReadAllText($src, $utf8)

$pattern = 'data:image/[a-zA-Z0-9.+-]+;base64,[A-Za-z0-9+/=]+'
$count = ([regex]::Matches($text, $pattern)).Count
$light = [regex]::Replace($text, $pattern, '')

$dst = Join-Path ([System.IO.Path]::GetDirectoryName($src)) (([System.IO.Path]::GetFileNameWithoutExtension($src)) + '-light.json')
[System.IO.File]::WriteAllText($dst, $light, $utf8)

$kbIn = [math]::Round((Get-Item -LiteralPath $src).Length / 1KB)
$kbOut = [math]::Round((Get-Item -LiteralPath $dst).Length / 1KB)
Write-Host "$count image(s) retirée(s) : $kbIn Ko -> $kbOut Ko"
Write-Host "Fichier créé : $dst"
