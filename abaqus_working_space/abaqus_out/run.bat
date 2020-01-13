@echo off

REM call "C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2017.6.270\windows\bin\ifortvars.bat" intel64
REM call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64

start "abaqus run" "C:\SIMULIA\CAE\2019\win_b64\code\bin\ABQLauncher.exe" -job dflux_experiment -user udfluxxx
