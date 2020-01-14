@echo off

cd %1
shift
set params=%1
:loop
shift
if [%1]==[] goto afterloop
set params=%params% %1
goto loop
:afterloop

REM call "C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2017.6.270\windows\bin\ifortvars.bat" intel64
REM call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64

"C:\SIMULIA\CAE\2019\win_b64\code\bin\ABQLauncher.exe" %params%

cd ..

REM run example_2 -job udfluxxx -user udfluxxx