@echo off
set _ShowDebugMessages=%~1
if "%_ShowDebugMessages%" equ "" set _ShowDebugMessages=no

set _IncludeMSYS64=%~2
if "%_IncludeMSYS64%" equ "" set _IncludeMSYS64=no

call :GetBatchFileDirectory _MyDir
call :SetOPT
if not defined OPT goto :EOF

set VCPKG_ROOT=

set LANG=en_US.UTF-8
set DOTNET_VERSION=9.0.305
set MSVC_TOOLS_VERSION=14.44.35207
set HOME=%LOCALAPPDATA%\Home
set JDK_HOME=%ProgramW6432%\Eclipse Adoptium\jdk-24.0.2.12-hotspot
set JDK_HOME_X64=%ProgramW6432%\Eclipse Adoptium\jdk-24.0.2.12-hotspot
set JDK_HOME_X86=%ProgramFiles(x86)%\Eclipse Adoptium\jdk-19.0.2.7-hotspot
set PANDOC_EXE=%ProgramW6432%\Pandoc\pandoc.exe
set VCPKG_FEATURE_FLAGS=-binarycaching
set VCPKG_ROOT=%_MyDir%
set Visual_Studio_2022_Install_Directory=%ProgramW6432%\Microsoft Visual Studio\2022\Professional
set CMAKE_TOOLCHAIN_FILE=%VCPKG_ROOT%\scripts\buildsystems\vcpkg.cmake

for %%a in (
"%_MyDir%\installed\%Platform%-windows\tools\gettext\bin"
"%_MyDir%\installed\%Platform%-windows\tools\icu\bin"
"%_MyDir%\installed\%Platform%-windows\tools\libiconv\bin"
"%_MyDir%\installed\%Platform%-windows\tools\python3\DLLs"
"%_MyDir%\installed\%Platform%-windows\tools\sassc\bin"
"%_MyDir%\downloads\tools\cmake-3.30.1-windows\cmake-3.30.1-windows-i386\bin"
"%_MyDir%\downloads\tools\jom\jom-1_1_4"
"%_MyDir%\downloads\tools\nasm\nasm-2.16.03"
"%_MyDir%\downloads\tools\perl\5.42.0.1\c\bin"
"%_MyDir%\downloads\tools\perl\5.42.0.1\c\x86_64-w64-mingw32\bin"
"%_MyDir%\downloads\tools\perl\5.42.0.1\perl\site\bin"
"%_MyDir%\downloads\tools\perl\5.42.0.1\perl\bin"
"%_MyDir%\downloads\tools\python\python-3.12.7-%Platform%"
"%_MyDir%\downloads\tools\python\python-3.12.7-%Platform%-1"
"%_MyDir%\downloads\tools\win_bison\2.5.24"
"%ProgramW6432%\Beyond Compare 4"
"%ProgramW6432%\Git\cmd"
"%JDK_HOME%\bin"
"%JDK_HOME%\bin\server"
"%ProgramW6432%\dotnet"
"%ProgramW6432%\dotnet\sdk\%DOTNET_VERSION%"
"%USERPROFILE%\.dotnet\tools"
"%ProgramW6432%\nodejs"
"%ProgramW6432%\Perforce"
"%ProgramW6432%\PowerShell\7"
"%ProgramW6432%\Python313"
"%ProgramW6432%\TortoiseSVN\bin"
"%ProgramW6432%\Pandoc"
"%ProgramFiles(x86)%\Poedit"
"%ProgramFiles(x86)%\Poedit\GettextTools\bin"
"%LOCALAPPDATA%\Programs\Microsoft VS Code"
"%OPT%\bin\X64"
"%OPT%\bin\X86"
"%OPT%\ExamDiff"
"%OPT%\Scripts"
) do (
  call :AppendToPath "%%~a"
)

call :AddMSYS64

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

::
:: Searches for the OPT directory and sets the OPT environment variable to the
:: found directory.
::
:: The OPT directory will be in the root directory of the hard drive but it may
:: be installed on any hard drive.
::
:SetOPT
  if defined OPT exit /b 0
  for %%a in (c d e f g h i j k l m n o p q r s t u v w x y z) do (
    if exist "%%a:\opt\." (
      set OPT=%%a:\opt
      exit /b 0
    )
  )
  exit /b 1
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

:: Function to show debug messages if debug messages are enabled
:: Usage: call :ShowDebugMessage "Your message here".
:ShowDebugMessage
  if "%_ShowDebugMessages%" neq "yes" exit /b 1
  echo %~1
goto :EOF

:: Function to add MSYS64 directories to PATH if _IncludeMSYS64 is set to "yes".
:: Usage: call :AddMSYS64
:AddMSYS64
  if "%_IncludeMSYS64%" neq "yes" exit /b 1
  for %%a in (
  "%SystemDrive%\msys64\mingw64\local\bin"
  "%SystemDrive%\msys64\mingw64\opt\bin"
  "%SystemDrive%\msys64\mingw64\bin"
  "%SystemDrive%\msys64\usr\local\bin"
  "%SystemDrive%\msys64\usr\bin"
  ) do (
    call :AppendToPath "%%~a"
  )
goto :EOF
