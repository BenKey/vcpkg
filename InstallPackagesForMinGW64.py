#!/usr/bin/env python

import inspect
import os
import platform
import subprocess
import sys

type str_list = list[str]

packagesToExcludeOnLinuxHostList: str_list = [
  'wxcharts',
  'yasm[tools]'
]

packageList = [
  ([
    'abseil',
    'ada-idna',
    'ada-url[tools]',
    'aixlog',
    'angelscript',
    'antlr4',
    'approval-tests-cpp',
    'args',
    'bdwgc',
    'better-enums',
    'bigint',
    'boost-accumulators',
    'boost-algorithm',
    'boost-align',
    'boost-any',
    'boost-array',
    'boost-asio',
    'boost-assert',
    'boost-assign',
    'boost-atomic',
    'boost-beast',
    'boost-bimap',
    'boost-bind',
    'boost-bloom',
    'boost-callable-traits',
    'boost-charconv',
    'boost-chrono',
    'boost-circular-buffer',
    'boost-compat',
    'boost-compute',
    'boost-concept-check',
    'boost-config',
    'boost-container',
    'boost-container-hash',
    'boost-context',
    'boost-contract',
    'boost-conversion',
    'boost-convert',
    'boost-core',
    'boost-coroutine',
    'boost-coroutine2',
    'boost-crc',
    'boost-date-time',
    'boost-describe',
    'boost-detail',
    'boost-dll',
    'boost-dynamic-bitset',
    'boost-endian',
    'boost-exception',
    'boost-fiber',
    'boost-filesystem',
    'boost-flyweight',
    'boost-foreach',
    'boost-format',
    'boost-function',
    'boost-function-types',
    'boost-functional',
    'boost-fusion',
    'boost-geometry',
    'boost-gil',
    'boost-graph',
    'boost-hana',
    'boost-hash2',
    'boost-headers',
    'boost-heap',
    'boost-histogram',
    'boost-hof',
    'boost-icl',
    'boost-integer',
    'boost-interprocess',
    'boost-interval',
    'boost-intrusive',
    'boost-io',
    'boost-iostreams',
    'boost-iterator',
    'boost-json',
    'boost-lambda',
    'boost-lambda2',
    'boost-leaf',
    'boost-lexical-cast',
    'boost-local-function',
    'boost-locale[icu]',
    'boost-lockfree',
    'boost-log',
    'boost-logic',
    'boost-math',
    'boost-metaparse',
    'boost-move',
    'boost-mp11',
    'boost-mpl',
    'boost-msm',
    'boost-multi-array',
    'boost-multi-index',
    'boost-multiprecision',
    'boost-nowide',
    'boost-numeric-conversion',
    'boost-odeint',
    'boost-openmethod',
    'boost-optional',
    'boost-outcome',
    'boost-parameter',
    'boost-parser',
    'boost-pfr',
    'boost-phoenix',
    'boost-poly-collection',
    'boost-polygon',
    'boost-pool',
    'boost-predef',
    'boost-preprocessor',
    'boost-process',
    'boost-program-options',
    'boost-property-map',
    'boost-property-tree',
    'boost-proto',
    'boost-ptr-container',
    'boost-qvm',
    'boost-random',
    'boost-range',
    'boost-ratio',
    'boost-rational',
    'boost-redis',
    'boost-regex[icu]',
    'boost-safe-numerics',
    'boost-scope',
    'boost-scope-exit',
    'boost-serialization',
    'boost-signals2',
    'boost-smart-ptr',
    'boost-sort',
    'boost-spirit',
    'boost-statechart',
    'boost-static-assert',
    'boost-static-string',
    'boost-stl-interfaces',
    'boost-system',
    'boost-test',
    'boost-thread',
    'boost-throw-exception',
    'boost-timer',
    'boost-tokenizer',
    'boost-tti',
    'boost-tuple',
    'boost-type-erasure',
    'boost-type-index',
    'boost-type-traits',
    'boost-typeof',
    'boost-ublas',
    'boost-units',
    'boost-unordered',
    'boost-url',
    'boost-utility',
    'boost-uuid',
    'boost-variant',
    'boost-variant2',
    'boost-vmd',
    'boost-wave',
    'boost-winapi',
    'boost-xpressive',
    'boost-yap',
    'catch2[thread-safe-assertions]',
    'chaiscript',
    'color-console',
    'constexpr',
    'cpp-base64',
    'cpptoml',
    'decimal-for-cpp',
    'dlfcn-win32',
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
    'hello-imgui[core,glfw-binding,opengl3-binding]',
    'imgui[core,glfw-binding,opengl3-binding,sdl3-binding,win32-binding]',
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
    'quickjs-ng',
    'rapidcsv',
    're2',
    'safeint',
    'sciter-js',
    'sfgui',
    'sdl3-image[core,jpeg,png,tiff,webp]',
    'sdl3-ttf[harfbuzz,svg]',
    'sdl3',
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
    'winreg',
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

def filter_list(list: str_list, excluded_list: str_list) -> str_list:
  if (len(excluded_list) == 0):
    return list
  excluded_set = set(excluded_list)
  return [item for item in list if item not in excluded_set]   

def IsDryRun() -> bool:
  return ("--dry-run" in sys.argv)

def GetHostTriplet() -> str:
  if platform.system() == "Linux":
    return "x64-linux"
  return "x64-mingw-dynamic"

def GetTriplet() -> str:
  return "x64-mingw-dynamic"

def InstallPackagesWorker(packages: str_list, triplet: str, hostTriplet: str, recurse: bool) -> bool:
  args = []
  args.append("vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append("--host-triplet")
  args.append(hostTriplet)
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

def InstallPackages(packages: str_list, recurse: bool) -> bool:
  triplet = GetTriplet()
  if (len(triplet) == 0):
    return False
  hostTriplet = GetHostTriplet()
  if (len(hostTriplet) == 0):
    return False
  
  # Filter out packages based on platform
  filtered_packages = packages
  if hostTriplet == "x64-linux":
    filtered_packages = filter_list(packages, packagesToExcludeOnLinuxHostList)
    if len(filtered_packages) != len(packages):
      print(f"Skipping {', '.join(packagesToExcludeOnLinuxHostList)} on Linux")
  
  print()
  print("################################################################################")
  print("Installing packages: %s" % filtered_packages)
  print("################################################################################")
  print()
  ret = InstallPackagesWorker(filtered_packages, triplet, hostTriplet, recurse)
  return ret

def InstallPackagesInPackageList() -> bool:
  for package in packageList:
    ret = InstallPackages(package[0], package[1])
    if ret == False:
      return False
  return True

InstallPackagesInPackageList()
