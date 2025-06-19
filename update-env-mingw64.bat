@echo off
set _ShowDebugMessages=%~1
if "%_ShowDebugMessages%" equ "" set _ShowDebugMessages=no

set _IncludeBusyBox=%~2
if "%_IncludeBusyBox%" equ "" set _IncludeBusyBox=no

call :GetBatchFileDirectory _MyDir

set VCPKG_ROOT=

set LANG=en_US.UTF-8
set HOME=%LOCALAPPDATA%\Home
set JAVA_HOME=%ProgramW6432%\Eclipse Adoptium\jdk-24.0.1.9-hotspot
set JDK_HOME=%ProgramW6432%\Eclipse Adoptium\jdk-24.0.1.9-hotspot
set VCPKG_ROOT=%_MyDir%
set CMAKE_TOOLCHAIN_FILE=%VCPKG_ROOT%\scripts\buildsystems\vcpkg.cmake
set C_INCLUDE_PATH=%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0\include;%SystemDrive%\mingw64\x86_64-w64-mingw32\include;%SystemDrive%\mingw64\x86_64-w64-mingw32\include\sec_api;%SystemDrive%\mingw64\include;%SystemDrive%\mingw64\opt\include;%VCPKG_ROOT%\installed\x64-mingw-dynamic\include
set CPLUS_INCLUDE_PATH=%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0\include;%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0\include\c++;%SystemDrive%\mingw64\x86_64-w64-mingw32\include;%SystemDrive%\mingw64\x86_64-w64-mingw32\include\sec_api;%SystemDrive%\mingw64\include;%SystemDrive%\mingw64\opt\include;%VCPKG_ROOT%\installed\x64-mingw-dynamic\include
set INCLUDE=%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0\include;%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0\include\c++;%SystemDrive%\mingw64\x86_64-w64-mingw32\include;%SystemDrive%\mingw64\x86_64-w64-mingw32\include\sec_api;%SystemDrive%\mingw64\include;%SystemDrive%\mingw64\opt\include;%VCPKG_ROOT%\installed\x64-mingw-dynamic\include
set LIBRARY_PATH=%SystemDrive%\mingw64\lib;%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.1.0;%SystemDrive%\mingw64\opt\lib;%SystemDrive%\mingw64\x86_64-w64-mingw32\lib;%VCPKG_ROOT%\installed\x64-mingw-dynamic\lib
set VCPKG_DEFAULT_HOST_TRIPLET=x64-mingw-dynamic
set VCPKG_DEFAULT_TRIPLET=x64-mingw-dynamic

for %%a in (
"%ProgramW6432%\Git"
"%ProgramW6432%\Git\cmd"
"%JDK_HOME%\bin"
"%JDK_HOME%\bin\server"
"%ProgramW6432%\dotnet"
"%USERPROFILE%\.dotnet\tools"
"%ProgramW6432%\PowerShell\7"
"%LOCALAPPDATA%\Programs\Microsoft VS Code"
) do (
  call :AppendToPathIfExists "%%~a"
)

for %%a in (
"%_MyDir%\downloads\tools\python\python-3.12.7-x64-1"
"%_MyDir%\downloads\tools\ninja\1.12.1-windows"
"%_MyDir%\downloads\tools\cmake-3.30.1-windows\cmake-3.30.1-windows-i386\bin"
"%_MyDir%\downloads\tools\7zr-24.09-windows"
"%_MyDir%\downloads\tools\7zip-24.09-windows"
"%_MyDir%\installed\x64-mingw-dynamic\tools\wxwidgets"
"%_MyDir%\installed\x64-mingw-dynamic\tools\tiff"
"%_MyDir%\installed\x64-mingw-dynamic\tools\gperf"
"%_MyDir%\installed\x64-mingw-dynamic\tools\fltk"
"%_MyDir%\installed\x64-mingw-dynamic\tools\bzip2"
"%_MyDir%\installed\x64-mingw-dynamic\tools\brotli"
"%_MyDir%\installed\x64-mingw-dynamic\tools"
"%_MyDir%\installed\x64-mingw-dynamic\bin"
"%SystemDrive%\mingw64\x86_64-w64-mingw32\bin"
"%SystemDrive%\mingw64\opt\bin"
"%SystemDrive%\mingw64\libexec\gcc\x86_64-w64-mingw32\15.1.0"
"%SystemDrive%\mingw64\bin"
) do (
  call :PrependToPathIfExists "%%~a"
)

goto :EOF

::
:: GetBatchFileDirectory
::
:: Gets the name of the directory in which the batch file is located.  The directory name will not
:: have a final trailing \ character.
::
:: The directory name is stored in the environment variable specified by the first parameter of the
:: function.
::
:GetBatchFileDirectory
  set _dir=%~dp0
  set _dir=%_dir:~0,-1%
  if "%_dir%" EQU "" (
    set _dir=
    exit /b 1
  )
  set %1=%_dir%
  set _dir=
  exit /b 0
goto :EOF

:AppendToPathIfExists
  if exist "%~1\." call :ShowDebugMessage "Adding '%~1' to the path."
  if not exist "%~1\." call :ShowDebugMessage "'%~1' does not exist."
  if exist "%~1\." set PATH=%PATH%;%~1
goto :EOF

:PrependToPathIfExists
  if exist "%~1\." call :ShowDebugMessage "Adding '%~1' to the path."
  if not exist "%~1\." call :ShowDebugMessage "'%~1' does not exist."
  if exist "%~1\." set PATH=%~1;%PATH%
goto :EOF

:ShowDebugMessage
  if "%_ShowDebugMessages%" neq "yes" exit /b 1
  echo %~1
goto :EOF

:AddBusyBox
  if "%_IncludeBusyBox%" neq "yes" exit /b 1
  for %%a in (
  "%SystemDrive%\mingw64\opt\BusyBox"
  ) do (
    call :AppendToPathIfExists "%%~a"
  )
goto :EOF
