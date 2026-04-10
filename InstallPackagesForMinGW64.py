#!/usr/bin/env python

import inspect
import os
import platform
import subprocess
import sys

type str_list = list[str]

packagesToExcludeOnLinuxHostList: str_list = [
  'qt[default-features]',
  'wxcharts',
  'yasm[tools]'
]

packageList: str_list = [
  'abseil',
  'ada-idna',
  'ada-url[tools]',
  'aixlog',
  'angelscript[addons]',
  'antlr4',
  'approval-tests-cpp',
  'args',
  'atk',
  'atkmm',
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
  'configcat[network,sha]',
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
  'ms-gsl',
  'nana',
  'nativefiledialog-extended',
  'openal-soft',
  'platform-folders',
  'portaudio',
  'protobuf',
  'pystring',
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
  'wildcards',
  'winreg',
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

def FilterPackagesList(packages: str_list, hostTriplet: str) -> str_list:
  filtered_packages: str_list = packages
  if hostTriplet == "x64-linux":
    filtered_packages = filter_list(packages, packagesToExcludeOnLinuxHostList)
  return filtered_packages

def IsDryRun() -> bool:
  return ("--dry-run" in sys.argv)

def ShouldRecurse() -> bool:
  return ("--recurse" in sys.argv)

def GetHostTriplet() -> str:
  if platform.system() == "Linux":
    return "x64-linux"
  return "x64-mingw-dynamic-custom"

def GetTriplet() -> str:
  return "x64-mingw-dynamic-custom"

def InstallPackagesWorker(packages: str_list, triplet: str, hostTriplet: str, recurse: bool) -> bool:
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
  hostTriplet: str = GetHostTriplet()
  if (len(hostTriplet) == 0):
    return False
  filtered_packages: str_list = FilterPackagesList(packages, hostTriplet)
  if len(filtered_packages) != len(packages):
    print(f"Skipping {', '.join(packagesToExcludeOnLinuxHostList)} on Linux")
  print()
  print("################################################################################")
  print(f"Installing packages: {filtered_packages}")
  print("################################################################################")
  print()
  ret: bool = InstallPackagesWorker(filtered_packages, triplet, hostTriplet, recurse)
  print()
  return ret

def InstallPackagesInPackageList() -> bool:
  ret: bool = InstallPackages(packageList, ShouldRecurse())
  if ret == False:
    return False
  return True

scriptDirectory: str = GetScriptDirectory()
print()
print(f"Script directory: {scriptDirectory}")
print()
InstallPackagesInPackageList()
