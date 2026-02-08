@echo off
set _ShowDebugMessages=%~1
if "%_ShowDebugMessages%" equ "" set _ShowDebugMessages=no

set _IncludeBusyBox=%~2
if "%_IncludeBusyBox%" equ "" set _IncludeBusyBox=no

call :GetBatchFileDirectory _MyDir

set VCPKG_ROOT=

set LANG=en_US.UTF-8
set HOME=%LOCALAPPDATA%\Home
set JAVA_HOME=%ProgramW6432%\Eclipse Adoptium\jdk-25.0.2.10-hotspot
set JDK_HOME=%ProgramW6432%\Eclipse Adoptium\jdk-25.0.2.10-hotspot
set VCPKG_ROOT=%_MyDir%
set CMAKE_TOOLCHAIN_FILE=%VCPKG_ROOT%\scripts\buildsystems\vcpkg.cmake
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
  call :AppendToPath "%%~a"
)

for %%a in (
"%_MyDir%\downloads\tools\python\python-3.14.2-x64-1"
"%_MyDir%\downloads\tools\ninja-1.13.2-windows"
"%_MyDir%\downloads\tools\meson-1.9.0-d1fcc2"
"%_MyDir%\downloads\tools\cmake-3.31.10-windows\cmake-3.31.10-windows-x86_64\bin"
"%_MyDir%\downloads\tools\7zip-25.01-windows"
"%_MyDir%\downloads\tools\7zr-25.01-windows"
"%_MyDir%\installed\x64-mingw-dynamic\tools\wxwidgets"
"%_MyDir%\installed\x64-mingw-dynamic\tools\tiff"
"%_MyDir%\installed\x64-mingw-dynamic\tools\pcre2"
"%_MyDir%\installed\x64-mingw-dynamic\tools\icu\bin"
"%_MyDir%\installed\x64-mingw-dynamic\tools\gperf"
"%_MyDir%\installed\x64-mingw-dynamic\tools\fltk"
"%_MyDir%\installed\x64-mingw-dynamic\tools\bzip2"
"%_MyDir%\installed\x64-mingw-dynamic\tools\brotli"
"%_MyDir%\installed\x64-mingw-dynamic\tools"
"%_MyDir%\installed\x64-mingw-dynamic\bin"
"%SystemDrive%\mingw64\x86_64-w64-mingw32\bin"
"%SystemDrive%\mingw64\opt\bin"
"%SystemDrive%\mingw64\opt\cmake\bin"
"%SystemDrive%\mingw64\opt\ntldd\bin"
"%SystemDrive%\mingw64\libexec\gcc\x86_64-w64-mingw32\15.2.0"
"%SystemDrive%\mingw64\bin"
) do (
  call :PrependToPath "%%~a"
)

:: **********************************************************************
:: Configure Include Paths
:: **********************************************************************

for %%a in (
  "%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.2.0\include"
  "%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.2.0\include\c++"
  "%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.2.0\include\c++\x86_64-w64-mingw32"
  "%SystemDrive%\mingw64\x86_64-w64-mingw32\include"
  "%SystemDrive%\mingw64\x86_64-w64-mingw32\include\sec_api"
  "%SystemDrive%\mingw64\include"
  "%SystemDrive%\mingw64\opt\include"
  "%_MyDir%\installed\x64-mingw-dynamic\include"
) do (
  call :AppendToIncludePath "%%~a"
)

:: **********************************************************************
:: Configure C Include Paths
:: **********************************************************************

for %%a in (
  "%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.2.0\include"
  "%SystemDrive%\mingw64\x86_64-w64-mingw32\include"
  "%SystemDrive%\mingw64\x86_64-w64-mingw32\include\sec_api"
  "%SystemDrive%\mingw64\include"
  "%SystemDrive%\mingw64\opt\include"
  "%_MyDir%\installed\x64-mingw-dynamic\include"
) do (
  call :AppendToCIncludePath "%%~a"
)

:: **********************************************************************
:: Configure Library Paths
:: **********************************************************************

for %%a in (
  "%SystemDrive%\mingw64\lib"
  "%SystemDrive%\mingw64\lib\gcc\x86_64-w64-mingw32\15.2.0"
  "%SystemDrive%\mingw64\opt\lib"
  "%SystemDrive%\mingw64\x86_64-w64-mingw32\lib"
  "%_MyDir%\installed\x64-mingw-dynamic\lib"
) do (
  call :AppendToLibraryPath "%%~a"
)

call :AddBusyBox

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

:: Function to append a directory to PATH if it exists
:: Usage: call :AppendToPath "C:\Path\To\Directory"
:AppendToPath
  set "DirToAdd=%~1"
  if not exist "%DirToAdd%\." call :ShowDebugMessage "'%DirToAdd%' does not exist."
  if not exist "%DirToAdd%\." exit /b 1
  call :ShowDebugMessage "Adding '%DirToAdd%' to the path."
  set PATH=%PATH%;%DirToAdd%
  exit /b 0
goto :EOF

:: Function to prepend a directory to PATH if it exists
:: Usage: call :PrependToPath "C:\Path\To\Directory"
:PrependToPath
  set "DirToAdd=%~1"
  if not exist "%DirToAdd%\." call :ShowDebugMessage "'%DirToAdd%' does not exist."
  if not exist "%DirToAdd%\." exit /b 1
  call :ShowDebugMessage "Adding '%DirToAdd%' to the path."
  set PATH=%DirToAdd%;%PATH%
  exit /b 0
goto :EOF

:: Function to append a directory to CPLUS_INCLUDE_PATH and INCLUDE if it exists
:: Usage: call :AppendToIncludePath "C:\Path\To\Directory"
:AppendToIncludePath
  set "DirToAdd=%~1"
  if not exist "%DirToAdd%\." call :ShowDebugMessage "'%DirToAdd%' does not exist."
  if not exist "%DirToAdd%\." exit /b 1
  call :ShowDebugMessage "Adding '%DirToAdd%' to CPLUS_INCLUDE_PATH and INCLUDE."
  if defined CPLUS_INCLUDE_PATH (
    set "CPLUS_INCLUDE_PATH=%CPLUS_INCLUDE_PATH%;%DirToAdd%"
  ) else (
    set "CPLUS_INCLUDE_PATH=%DirToAdd%"
  )
  if defined INCLUDE (
    set "INCLUDE=%INCLUDE%;%DirToAdd%"
  ) else (
    set "INCLUDE=%DirToAdd%"
  )
  exit /b 0
goto :eof

:: Function to append a directory to C_INCLUDE_PATH if it exists
:: Usage: call :AppendToCIncludePath "C:\Path\To\Directory"
:AppendToCIncludePath
  set "DirToAdd=%~1"
  if not exist "%DirToAdd%\." call :ShowDebugMessage "'%DirToAdd%' does not exist."
  if not exist "%DirToAdd%\." exit /b 1
  call :ShowDebugMessage "Adding '%DirToAdd%' to C_INCLUDE_PATH."
  if defined C_INCLUDE_PATH (
    set "C_INCLUDE_PATH=%C_INCLUDE_PATH%;%DirToAdd%"
  ) else (
    set "C_INCLUDE_PATH=%DirToAdd%"
  )
  exit /b 0
goto :eof

:: Function to append a directory to LIBRARY_PATH if it exists
:: Usage: call :AppendToLibraryPath "C:\Path\To\Directory"
:AppendToLibraryPath
  set "DirToAdd=%~1"
  if not exist "%DirToAdd%\." call :ShowDebugMessage "'%DirToAdd%' does not exist."
  if not exist "%DirToAdd%\." exit /b 1
  call :ShowDebugMessage "Adding '%DirToAdd%' to LIBRARY_PATH."
  if defined LIBRARY_PATH (
    set "LIBRARY_PATH=%LIBRARY_PATH%;%DirToAdd%"
  ) else (
    set "LIBRARY_PATH=%DirToAdd%"
  )
  exit /b 0
goto :eof

:: Function to show debug messages if debug messages are enabled
:: Usage: call :ShowDebugMessage "Your message here".
:ShowDebugMessage
  if "%_ShowDebugMessages%" neq "yes" exit /b 1
  echo %~1
goto :EOF

:: Function to add BusyBox to PATH if _IncludeBusyBox is set to "yes"
:: Usage: call :AddBusyBox
:AddBusyBox
  if "%_IncludeBusyBox%" neq "yes" exit /b 1
  for %%a in (
  "%SystemDrive%\mingw64\opt\BusyBox"
  ) do (
    call :AppendToPath "%%~a"
  )
goto :EOF

:: Function to set wxWidgets environment variables
:: Usage: call :SetWXWidgetsEnv
:SetWXWidgetsEnv
  if not exist "%_MyDir%\installed\x64-mingw-dynamic\lib\." exit /b 1
  if not exist "%_MyDir%\installed\x64-mingw-dynamic\include\wx\." exit /b 1
  set wxWidgets_CONFIGURATION=mswu
  set wxWidgets_LIB_DIR=%_MyDir%\installed\x64-mingw-dynamic\lib
  set wxWidgets_ROOT_DIR=%_MyDir%\installed\x64-mingw-dynamic
  exit /b 0
goto :EOF
