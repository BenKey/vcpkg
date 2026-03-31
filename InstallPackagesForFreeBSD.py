#!/usr/bin/env python

import inspect
import os
import platform
import subprocess
import sys

str_list = list[str]

packageList: str_list = [
  'abseil',
  'ada-idna',
  'ada-url[tools]',
  'aixlog',
  'angelscript[addons]',
  'antlr4',
  'approval-tests-cpp',
  'apr',
  'apr-util',
  'args',
  'atk',
  'atkmm',
  'bdwgc',
  'better-enums',
  'bigint',
  'boost-asio[core,ssl]',
  'boost-locale[core,icu]',
  'boost-odeint[core]',
  'boost-regex[core,icu]',
  'boost[core]',
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
  'gtk',
  'gtkmm',
  'guilite',
  'gumbo',
  'hello-imgui[core,glfw-binding,opengl3-binding]',
  'libiconv',
  'icu[core,tools]',
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
  'ms-gsl',
  'nana',
  'nativefiledialog-extended',
  'openal-soft',
  'platform-folders',
  'portaudio',
  'protobuf',
  'pystring',
  'python3',
  'rapidcsv',
  're2',
  'safeint',
  'sfgui',
  'sdl2[core,x11]',
  'sdl2-image[core,libjpeg-turbo,libwebp,tiff]',
  'sdl2-mixer[core,fluidsynth,libflac,mpg123]',
  'sdl2-net',
  'sdl2-ttf[harfbuzz]',
  'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
  'sdl3[core,x11]',
  'sdl3-image[core,jpeg,png,tiff,webp]',
  'sdl3-mixer[core,fluidsynth,libflac,libvorbis,mpg123]',
  'sdl3-ttf[harfbuzz,svg]',
  'spirit-po',
  'sqlite-modern-cpp',
  'sqlite3[core,json1,tool,unicode,zlib]',
  'sqlitecpp',
  'status-code',
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

def ShouldRecurse() -> bool:
  return ("--recurse" in sys.argv)

def GetHostTriplet() -> str:
  return "x64-freebsd-custom"

def GetTriplet() -> str:
  return "x64-freebsd-custom"

def InstallPackagesWorker(packages: str_list, triplet: str, hostTriplet: str, recurse: bool) -> bool:
  scriptDirectory: str = GetScriptDirectory()
  args: str_list = []
  args.append("./vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append("--host-triplet")
  args.append(hostTriplet)
  args.append(f"--overlay-triplets={scriptDirectory}/triplets/custom")
  args.append(f"--x-buildtrees-root={scriptDirectory}/bt")
  args.append("--clean-after-build")
  if (recurse):
    args.append("--recurse")
  try:
    separator: str = ' '
    joinedArgs: str = separator.join(args)
    print(f"Calling '{joinedArgs}'.")
    if (IsDryRun()):
      print("Dry run. Not actually installing packages.")
      return True
    subprocess.check_call(args)
    return True
  except subprocess.CalledProcessError:
    return False
  except OSError:
    return False

def InstallPackages(packages: str_list, recurse: bool) -> bool:
  triplet: str = GetTriplet()
  if (len(triplet) == 0):
    return False
  hostTriplet = GetHostTriplet()
  if (len(hostTriplet) == 0):
    return False
  print()
  print("################################################################################")
  print(f"Installing packages: {packages}")
  print("################################################################################")
  print()
  ret: bool = InstallPackagesWorker(packages, triplet, hostTriplet, recurse)
  print()
  return ret

def InstallPackagesInPackageList() -> bool:
  ret: bool = InstallPackages(packageList, ShouldRecurse())
  if ret == False:
    return False
  return True

InstallPackagesInPackageList()
