#!/usr/bin/env python

import inspect
import os
import subprocess
import sys

type str_list = list[str]

packageList = [
  ([
    'abseil',
    'ada-idna',
    'ada-url[tools]',
    'aixlog',
    'alsa',
    'angelscript[addons]',
    'antlr4',
    'approval-tests-cpp',
    'apr',
    'apr-util',
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
    'catch2[thread-safe-assertions]',
    'chaiscript',
    'configcat[network,sha]',
    'constexpr',
    'cpp-base64',
    'cpptoml',
    'decimal-for-cpp',
    'dirent',
    'dukglue',
    'duktape',
    'fenster',
    'fltk',
    'fmt',
    'freeglut',
    'glui',
    'gppanel',
    'gtest',
    'guilite',
    'gumbo',
    'hello-imgui',
    'icu[core,tools]',
    'hello-imgui[core,glfw-binding,opengl3-binding]',
    'imgui[core,glfw-binding,opengl3-binding,sdl3-binding]',
    'imgui-sfml',
    'inipp',
    'json-spirit',
    'json11',
    'jsoncons',
    'libcpplocate',
    'libfork',
    'libguarded',
    'libsndfile[external-libs,mpeg]',
    'litehtml',
    'lua[cpp,tools]',
    'magic-enum',
    'mp3lame[frontend]',
    'mpi',
    'ms-gsl',
    'nana',
    'nativefiledialog-extended',
    'openal-soft',
    'platform-folders',
    'portaudio',
    'protobuf',
    'pystring',
    'qt[default-features]',
    'rapidcsv',
    're2',
    'safeint',
    'sfgui',
    'sdl3-image[core,jpeg,png,tiff,webp]',
    'sdl3-ttf[harfbuzz,svg]',
    'sdl3[alsa,wayland,x11]',
    'spirit-po',
    'sqlite-modern-cpp',
    'sqlite3[core,json1,tool,unicode,zlib]',
    'sqlitecpp',
    'stduuid',
    'strtk[boost]',
    'tgui[sdl3,sfml,tool]',
    'tidy-html5',
    'tiff[core,cxx,jpeg,lzma,tools,webp,zip,zstd]',
    'toml11',
    'tomlplusplus',
    'tvision',
    'uberswitch',
    'uni-algo',
    'utf8h',
    'utfcpp',
    'wildcards',
    'wt[dbo,openssl,openssl]',
    'wxcharts',
    'wxwidgets[core,example,fonts,media,secretstore,sound]',
    'yasm[tools]'
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

def InstallPackagesWorker(packages: str_list, triplet: str, recurse: bool) -> bool:
  scriptDirectory = GetScriptDirectory()
  args = []
  args.append("./vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append(f"--overlay-triplets={scriptDirectory}/triplets/custom")
  args.append(f"--x-buildtrees-root={scriptDirectory}/bt")
  args.append("--clean-after-build")
  if (recurse):
    args.append("--recurse")
  try:
    seperator = ' '
    argsString = seperator.join(args)
    print(f"Calling '{argsString}'.")
    if (IsDryRun()):
      print("Dry run. Not actually installing packages.")
      return True
    subprocess.check_call(args)
    return True
  except subprocess.CalledProcessError as err:
    return False
  except OSError as err:
    return False

def InstallPackages(packages: str_list, recurse: bool) -> bool:
  print()
  print("################################################################################")
  print(f"Installing packages: {packages}")
  print("################################################################################")
  print()
  ret = InstallPackagesWorker(packages, "x64-linux", recurse)
  print()
  return ret

def InstallPackagesInPackageList() -> bool:
  for package in packageList:
    ret = InstallPackages(package[0], package[1])
    if ret == False:
      return False
  return True

InstallPackagesInPackageList()
