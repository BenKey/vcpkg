#!/usr/bin/env python

import inspect
import os
import subprocess
import sys

type str_list = list[str]

x64OnlyPackageList = [
  "qt[default-features]"
]

x86OnlyPackageList = [
]

arm64PackageList = [
  ([
    'aixlog',
    'args',
    'better-enums',
    'boost-accumulators[core]',
    'boost-algorithm[core]',
    'boost-align[core]',
    'boost-any[core]',
    'boost-array[core]',
    'boost-assert[core]',
    'boost-assign[core]',
    'boost-atomic[core]',
    'boost-beast[core]',
    'boost-bimap[core]',
    'boost-bind[core]',
    'boost-callable-traits[core]',
    'boost-charconv[core]',
    'boost-chrono[core]',
    'boost-circular-buffer[core]',
    'boost-cobalt[core]',
    'boost-compat[core]',
    'boost-compute[core]',
    'boost-concept-check[core]',
    'boost-config[core]',
    'boost-container[core]',
    'boost-container-hash[core]',
    'boost-context[core]',
    'boost-contract[core]',
    'boost-convert[core]',
    'boost-core[core]',
    'boost-crc[core]',
    'boost-date-time[core]',
    'boost-describe[core]',
    'boost-detail[core]',
    'boost-dll[core]',
    'boost-dynamic-bitset[core]',
    'boost-endian[core]',
    'boost-exception[core]',
    'boost-filesystem[core]',
    'boost-flyweight[core]',
    'boost-foreach[core]',
    'boost-format[core]',
    'boost-function[core]',
    'boost-function-types[core]',
    'boost-functional[core]',
    'boost-fusion[core]',
    'boost-geometry[core]',
    'boost-gil[core]',
    'boost-graph[core]',
    'boost-hana[core]',
    'boost-headers[core]',
    'boost-heap[core]',
    'boost-histogram[core]',
    'boost-hof[core]',
    'boost-icl[core]',
    'boost-integer[core]',
    'boost-interprocess[core]',
    'boost-interval[core]',
    'boost-intrusive[core]',
    'boost-io[core]',
    'boost-iostreams[core]',
    'boost-iterator[core]',
    'boost-json[core]',
    'boost-lambda[core]',
    'boost-lambda2[core]',
    'boost-leaf[core]',
    'boost-lexical-cast[core]',
    'boost-local-function[core]',
    'boost-locale[core,icu]',
    'boost-lockfree[core]',
    'boost-log[core]',
    'boost-logic[core]',
    'boost-math[core]',
    'boost-metaparse[core]',
    'boost-move[core]',
    'boost-mp11[core]',
    'boost-mpl[core]',
    'boost-msm[core]',
    'boost-multi-array[core]',
    'boost-multi-index[core]',
    'boost-multiprecision[core]',
    'boost-mysql[core]',
    'boost-nowide[core]',
    'boost-odeint[core]',
    'boost-optional[core]',
    'boost-outcome[core]',
    'boost-parameter[core]',
    'boost-pfr[core]',
    'boost-phoenix[core]',
    'boost-poly-collection[core]',
    'boost-polygon[core]',
    'boost-pool[core]',
    'boost-predef[core]',
    'boost-preprocessor[core]',
    'boost-process[core]',
    'boost-program-options[core]',
    'boost-property-map[core]',
    'boost-property-tree[core]',
    'boost-proto[core]',
    'boost-ptr-container[core]',
    'boost-qvm[core]',
    'boost-random[core]',
    'boost-range[core]',
    'boost-ratio[core]',
    'boost-rational[core]',
    'boost-redis[core]',
    'boost-regex[core,icu]',
    'boost-safe-numerics[core]',
    'boost-scope[core]',
    'boost-scope-exit[core]',
    'boost-serialization[core]',
    'boost-signals2[core]',
    'boost-smart-ptr[core]',
    'boost-sort[core]',
    'boost-spirit[core]',
    'boost-stacktrace[core]',
    'boost-statechart[core]',
    'boost-static-assert[core]',
    'boost-static-string[core]',
    'boost-stl-interfaces[core]',
    'boost-system[core]',
    'boost-test[core]',
    'boost-thread[core]',
    'boost-throw-exception[core]',
    'boost-timer[core]',
    'boost-tokenizer[core]',
    'boost-tti[core]',
    'boost-tuple[core]',
    'boost-type-erasure[core]',
    'boost-type-index[core]',
    'boost-type-traits[core]',
    'boost-typeof[core]',
    'boost-ublas[core]',
    'boost-units[core]',
    'boost-unordered[core]',
    'boost-url[core]',
    'boost-utility[core]',
    'boost-uuid[core]',
    'boost-variant[core]',
    'boost-variant2[core]',
    'boost-vmd[core]',
    'boost-wave[core]',
    'boost-winapi[core]',
    'boost-xpressive[core]',
    'boost-yap[core]',
    'color-console',
    'cpptoml',
    'gtest',
    'gumbo',
    'icu[core]',
    'inipp',
    'jsoncons',
    'libguarded',
    'magic-enum',
    'mp3lame',
    'ms-gsl',
    'nana',
    'platform-folders',
    'rapidcsv',
    'strtk',
    'toml11',
    'tomlplusplus',
    'utf8h',
    'utfcpp',
    'wil',
    'wildcards',
    'wtl'
  ], False)
]

packageList = [
  ([
    'aixlog',
    'args',
    'better-enums',
    'boost-asio[core,ssl]',
    'boost-locale[core,icu]',
    'boost-mpi[core,python3]',
    'boost-odeint[core,mpi]',
    'boost-regex[core,icu]',
    'boost[core,mpi]',
    'color-console',
    'cpptoml',
    'fltk',
    'gppanel',
    'guilite',
    'gtest',
    'gumbo',
    'icu[core,tools]',
    'imgui[core,sdl3-binding,win32-binding]',
    'inipp',
    'jsoncons',
    'libguarded',
    'magic-enum',
    'mp3lame',
    'mpi',
    'ms-gsl',
    'nana',
    'openal-soft',
    'platform-folders',
    'portaudio',
    'python3',
    'rapidcsv',
    'sdl3-image[core,jpeg,png,tiff,webp]',
    'sdl3-ttf',
    'sdl3',
    'sqlite3[core,json1,tool,unicode,zlib]',
    'sqlitecpp',
    'strtk',
    'tiff[core,cxx,jpeg,lzma,tools,webp,zip,zstd]',
    'toml11',
    'tomlplusplus',
    'uberswitch',
    'utf8h',
    'utfcpp',
    'wil',
    'wildcards',
    'wtl',
    'wxcharts',
    'wxwidgets[core,example,fonts,media,secretstore,sound,webview]'
  ], False)
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

def InstallPackagesWorker(packages: str_list, triplet: str, platform: str, recurse: bool) -> bool:
  print("+++++++++++++++++++")
  print(f"++ {triplet} ++")
  print("+++++++++++++++++++")
  print()
  os.environ["VCPKG_DEFAULT_TRIPLET"] = triplet
  scriptDirectory = GetScriptDirectory()
  args: str_list = []
  args.append("vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append(f"--x-buildtrees-root={scriptDirectory}/bt/{platform}")
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

def InstallARM64Packages(packages: str_list, recurse: bool) -> bool:
  print()
  print("################################################################################")
  print(f"Installing packages: {packages}")
  print("################################################################################")
  print()
  ret: bool = InstallPackagesWorker(packages, "arm64-windows", "arm64", recurse)
  print()
  return ret

def InstallPackages(packages: str_list, recurse: bool) -> bool:
  print()
  print("################################################################################")
  print(f"Installing packages: {packages}")
  print("################################################################################")
  print()
  ret: bool = False
  x64Packages = filter_list(packages, x86OnlyPackageList)
  if (len(x64Packages) == 0):
    print("No x64 packages to install.")
    print()
    return False
  ret = InstallPackagesWorker(x64Packages, "x64-windows", "x64", recurse)
  if (not ret):
    return False
  print()
  x86Packages = filter_list(packages, x64OnlyPackageList)
  if (len(x86Packages) == 0):
    print("No x86 packages to install.")
    print()
    return ret
  ret = InstallPackagesWorker(x86Packages, "x86-windows", "x86", recurse)
  print()
  return ret

def InstallPackagesInARM64PackageList() -> bool:
  for package in arm64PackageList:
    ret: bool = InstallARM64Packages(package[0], package[1])
    if ret == False:
      return False
  return True

def InstallPackagesInPackageList() -> bool:
  for package in packageList:
    ret: bool = InstallPackages(package[0], package[1])
    if ret == False:
      return False
  return True

ret: bool = InstallPackagesInARM64PackageList()
if ret == False:
  sys.exit(1)

ret = InstallPackagesInPackageList()
if ret == False:
  sys.exit(2)

sys.exit(os.EX_OK)
