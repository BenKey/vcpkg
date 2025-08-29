@echo off
call :GetBatchFileDirectory _MyDir
set VCPKG_ROOT=
set VCPKG_ROOT=%_MyDir%

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
