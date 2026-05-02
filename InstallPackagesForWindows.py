#!/usr/bin/env python

import inspect
import os
import platform
import subprocess
import sys

type str_list = list[str]

x64OnlyPackageList: str_list = [
  "qt[default-features]"
]

x86OnlyPackageList: str_list = [
]

arm64PackageList: str_list = [
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
  'bdwgc',
  'better-enums',
  'bigint',
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
  'catch2[thread-safe-assertions]',
  'chaiscript',
  'color-console',
  'configcat[network,sha]',
  'constexpr',
  'cpp-base64',
  'cpptoml',
  'decimal-for-cpp',
  'dirent',
  'dlfcn-win32',
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
  'icu[core]',
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
  'mp3lame',
  'ms-gsl',
  'nana',
  'nativefiledialog-extended',
  'openal-soft',
  'platform-folders',
  'plog',
  'portaudio',
  'protobuf',
  'pystring',
  'qt[default-features]',
  'rapidcsv',
  're2',
  'safeint',
  'sfgui',
  'sdl2',
  'sdl2-image[core,libjpeg-turbo,libwebp,tiff]',
  'sdl2-mixer[core,fluidsynth,libflac,mpg123]',
  'sdl2-net',
  'sdl2-ttf[harfbuzz]',
  'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
  'sdl3',
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
  'wil',
  'wildcards',
  'winreg',
  'wtl',
  'wxcharts',
  'wxwidgets[core,example,fonts,media,secretstore,sound,webview]'
]

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
  'boost-mpi[core,python3]',
  'boost-odeint[core,mpi]',
  'boost-regex[core,icu]',
  'boost[core,mpi]',
  'catch2[thread-safe-assertions]',
  'chaiscript',
  'color-console',
  'configcat[network,sha]',
  'constexpr',
  'cpp-base64',
  'cpptoml',
  'decimal-for-cpp',
  'dirent',
  'dlfcn-win32',
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
  'mpi',
  'ms-gsl',
  'nana',
  'nativefiledialog-extended',
  'openal-soft',
  'platform-folders',
  'plog',
  'portaudio',
  'protobuf',
  'pystring',
  'python3',
  'qt[default-features]',
  'quickjs-ng',
  'rapidcsv',
  're2',
  'safeint',
  'sciter-js',
  'sfgui',
  'sdl2',
  'sdl2-image[core,libjpeg-turbo,libwebp,tiff]',
  'sdl2-mixer[core,fluidsynth,libflac,mpg123]',
  'sdl2-net',
  'sdl2-ttf[harfbuzz]',
  'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
  'sdl3',
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
  'vs-yasm',
  'wil',
  'wildcards',
  'winreg',
  'wt[dbo,openssl,openssl]',
  'wtl',
  'wxcharts',
  'wxwidgets[core,example,fonts,media,secretstore,sound,webview]',
  'yasm[tools]'
]

def GetScriptFile() -> str:
    """Obtains the full path and file name of the Python script."""
    if (hasattr(GetScriptFile, "file")):
        return getattr(GetScriptFile, "file")
    
    ret: str = ""
    try:
        # Use abspath instead of realpath to keep subst drives
        ret = os.path.abspath(__file__)
    except NameError:
        if (len(sys.argv) > 0 and len(sys.argv[0]) > 0 and os.path.isabs(sys.argv[0])):
            ret = os.path.abspath(sys.argv[0])
        else:
            ret = os.path.abspath(inspect.getfile(GetScriptFile))
            
    if (not os.path.exists(ret)):
        ret = os.path.dirname(ret)

    ret = os.path.normpath(ret) 
    ret = ret.replace("\\", "/")
    setattr(GetScriptFile, "file", ret)
    return getattr(GetScriptFile, "file")

def GetScriptDirectory() -> str:
  """Obtains the path to the directory containing the script."""
  if (hasattr(GetScriptDirectory, "dir")):
    return getattr(GetScriptDirectory, "dir")
  ret: str = os.path.dirname(GetScriptFile())
  if (len(ret) == 3 and ret[1] == ":" and ret[2] == "/"):
    ret = ret[0:2]
  setattr(GetScriptDirectory, "dir", ret)
  return getattr(GetScriptDirectory, "dir")

def filter_list(list: str_list, excluded_list: str_list) -> str_list:
  if (len(excluded_list) == 0):
    return list
  excluded_set = set(excluded_list)
  return [item for item in list if item not in excluded_set]   

def IsDryRun() -> bool:
  return ("--dry-run" in sys.argv)

def ShouldRecurse() -> bool:
  return ("--recurse" in sys.argv)

def GetHostTriplet() -> str:
  return "x64-windows"

def GetTriplet(platform: str) -> str:
  return f"{platform}-windows"

def InstallPackagesWorker(packages: str_list, triplet: str, hostTriplet: str, platform: str, recurse: bool) -> bool:
  print("+++++++++++++++++++")
  print(f"++ {triplet} ++")
  print("+++++++++++++++++++")
  print()
  os.environ["VCPKG_DEFAULT_TRIPLET"] = triplet
  scriptDirectory: str = GetScriptDirectory()
  args: str_list = []
  args.append("vcpkg")
  args.append("install")
  args.extend(packages)
  args.append("--triplet")
  args.append(triplet)
  args.append("--host-triplet")
  args.append(hostTriplet)
  args.append(f"--overlay-triplets={scriptDirectory}/triplets/custom")
  args.append(f"--x-buildtrees-root={scriptDirectory}/bt/{platform}")
  args.append("--clean-after-build")
  args.append("--classic")
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
  triplet: str = GetTriplet("arm64")
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
  ret: bool = InstallPackagesWorker(packages, triplet, hostTriplet, "arm64", recurse)
  print()
  return ret

def InstallPackages(packages: str_list, recurse: bool) -> bool:
  hostTriplet: str = GetHostTriplet()
  if (len(hostTriplet) == 0):
    return False
  print()
  print("################################################################################")
  print(f"Installing packages: {packages}")
  print("################################################################################")
  print()
  ret: bool = False
  filtered_packages: str_list = filter_list(packages, x86OnlyPackageList)
  if (len(filtered_packages) == 0):
    print("No x64 packages to install.")
    print()
    return False
  triplet: str = GetTriplet("x64")
  if (len(triplet) == 0):
    return False
  ret = InstallPackagesWorker(filtered_packages, triplet, hostTriplet, "x64", recurse)
  if (not ret):
    return False
  print()
  filtered_packages = filter_list(packages, x64OnlyPackageList)
  if (len(filtered_packages) == 0):
    print("No x86 packages to install.")
    print()
    return ret
  triplet = GetTriplet("x86")
  if (len(triplet) == 0):
    return False
  ret = InstallPackagesWorker(filtered_packages, triplet, hostTriplet, "x86", recurse)
  print()
  return ret

def InstallPackagesInARM64PackageList() -> bool:
  ret: bool = InstallARM64Packages(arm64PackageList, ShouldRecurse())
  if ret == False:
    return False
  return True

def InstallPackagesInPackageList() -> bool:
  ret: bool = InstallPackages(packageList, ShouldRecurse())
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
