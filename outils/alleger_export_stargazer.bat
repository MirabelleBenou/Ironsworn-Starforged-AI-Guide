@echo off
rem Glisser-deposer l export Stargazer (.json) sur ce fichier.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0alleger_export_stargazer.ps1" "%~1"
pause
