#!/usr/bin/env python

import inspect
import os
import subprocess
import sys

packageList = [
  ([
    'abseil[core,cxx17]',
    'aixlog',
    'angelscript',
    'antlr4',
    'approval-tests-cpp',
    'args',
    'bdwgc',
    'better-enums',
    'bigint',
    'boost-asio[core,ssl]',
    'boost-locale[core,icu]',
    'boost-mpi[core]',
    'boost-odeint[core,mpi]',
    'boost-regex[core,icu]',
    'boost[core,mpi]',
    'Catch2',
    'chaiscript',
    'cpp-base64',
    'cpptoml',
    'decimal-for-cpp',
    'dukglue',
    'duktape',
    'fenster',
    'fltk',
    'gppanel',
    'gtest[core,cxx17]',
    'guilite',
    'gumbo',
    'hello-imgui',
    'icu[core,tools]',
    'imgui[core,sdl3-binding]',
    'inipp',
    'json-spirit',
    'json11',
    'jsoncons',
    'libguarded',
    'litehtml',
    'magic-enum',
    'mp3lame',
    'mpi',
    'ms-gsl',
    'nana',
    'platform-folders',
    'quickjs-ng',
    'rapidcsv',
    'sciter-js',
    'sfgui',
    'sdl3-image[core,jpeg,png,tiff,webp]',
    'sdl3-ttf',
    'sdl3',
    'spirit-po',
    'sqlite-modern-cpp',
    'sqlite3[core,json1,tool,unicode,zlib]',
    'sqlitecpp',
    'status-code',
    'strtk',
    'tgui',
    'tiff[core,cxx,jpeg,lzma,tools,webp,zip,zstd]',
    'toml11',
    'tomlplusplus',
    'uberswitch',
    'utf8h',
    'utfcpp',
    'wildcards',
    'wxcharts',
    'wxwidgets[core,example,fonts,media,sound]'
  ], False),
]

def GetScriptFile() -> str:
  """Obtains the full path and file name of the Python script."""
  if (hasattr(GetScriptFile, "file")):
    return getattr(GetScriptFile, "file")
  ret: str = ""
  try:
    # The easy way. Just use __file__.
    # Unfortunately, __file__ is not available when cx_freeze is used or in IDLE.
    ret = os.path.realpath(__file__)
  except NameError:
    # The hard way.
    if (len(sys.argv) > 0 and len(sys.argv[0]) > 0 and os.path.isabs(sys.argv[0])):
      ret = os.path.realpath(sys.argv[0])
    else:
      ret = os.path.realpath(inspect.getfile(GetScriptFile))
      if (not os.path.exists(ret)):
        # If cx_freeze is used the value of the ret variable at this point is in
        # the following format: {PathToExeFile}\{NameOfPythonSourceFile}. This
        # makes it necessary to strip off the file name to get the correct path.
        ret = os.path.dirname(ret)
  setattr(GetScriptFile, "file", ret)
  return getattr(GetScriptFile, "file")

def GetScriptDirectory() -> str:
  """Obtains the path to the directory containing the script."""
  if (hasattr(GetScriptDirectory, "dir")):
    return getattr(GetScriptDirectory, "dir")
  module_path: str = GetScriptFile()
  setattr(GetScriptDirectory, "dir", os.path.dirname(module_path))
  return getattr(GetScriptDirectory, "dir")

def IsDryRun() -> bool:
  return ("--dry-run" in sys.argv)

def InstallPackagesWorker(packages, triplet, recurse):
  args = []
  args.append("./vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append("--x-buildtrees-root=%s/bt" % GetScriptDirectory())
  if (recurse):
    args.append("--recurse")
  try:
    seperator = ' '
    print("Calling '%s'." % seperator.join(args))
    if (IsDryRun()):
      print("Dry run. Not actually installing packages.")
      return True
    subprocess.check_call(args)
    return True
  except subprocess.CalledProcessError as err:
    return False
  except OSError as err:
    return False

def InstallPackages(packages, recurse):
  print()
  print("################################################################################")
  print("Installing packages: %s" % packages)
  print("################################################################################")
  print()
  ret = InstallPackagesWorker(packages, "x64-linux", recurse)
  print()
  return ret

def InstallPackagesInPackageList():
  for package in packageList:
    ret = InstallPackages(package[0], package[1])
    if ret == False:
      return False
  return True

InstallPackagesInPackageList()

