@echo off

call "C:\Program Files (x86)\IntelSWTools\compilers_and_libraries_2018.5.274\windows\bin\ifortvars.bat" intel64
call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat" x64
REM call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
C:\SIMULIA\CAE\2019\win_b64\code\bin\ABQLauncher.exe -user udflux -job udflux


REM run example_2 -job udfluxxx -user udfluxxx