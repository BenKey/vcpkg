# pyright: reportMissingImports=false

import inspect
import os
import sys

from InstallPackagesHelper import filter_list
from InstallPackagesHelper import ModuleMain

type str_list = list[str]

x64OnlyPackageList: str_list = [
  "qt[default-features]"
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
  'boost-accumulators',
  'boost-algorithm',
  'boost-align',
  'boost-any',
  'boost-array',
  'boost-assert',
  'boost-assign',
  'boost-atomic',
  'boost-beast',
  'boost-bimap',
  'boost-bind',
  'boost-callable-traits',
  'boost-charconv',
  'boost-chrono',
  'boost-circular-buffer',
  'boost-cobalt',
  'boost-compat',
  'boost-compute',
  'boost-concept-check',
  'boost-config',
  'boost-container',
  'boost-container-hash',
  'boost-context',
  'boost-contract',
  'boost-convert',
  'boost-core',
  'boost-crc',
  'boost-date-time',
  'boost-describe',
  'boost-detail',
  'boost-dll',
  'boost-dynamic-bitset',
  'boost-endian',
  'boost-exception',
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
  'boost-mysql',
  'boost-nowide',
  'boost-odeint',
  'boost-optional',
  'boost-outcome',
  'boost-parameter',
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
  'boost-stacktrace',
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
  'icu',
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
  'rapidcsv',
  're2',
  'safeint',
  'sfgui',
  'sdl2',
  'sdl2-image[libjpeg-turbo,libwebp,tiff]',
  'sdl2-mixer[fluidsynth,libflac,mpg123]',
  'sdl2-net',
  'sdl2-ttf[harfbuzz]',
  'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
  'sdl3',
  'sdl3-image[jpeg,png,tiff,webp]',
  'sdl3-mixer[fluidsynth,libflac,libvorbis,mpg123]',
  'sdl3-ttf[harfbuzz,svg]',
  'spirit-po',
  'sqlite-modern-cpp',    
  'sqlite3[json1,tool,unicode,zlib]',
  'sqlitecpp',
  'status-code',
  'stduuid',
  'strtk[boost]',
  'tgui[sdl3,sfml,tool]',
  'tidy-html5',
  'tiff[cxx,jpeg,lzma,tools,webp,zip,zstd]',
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
  'wxwidgets[example,fonts,media,secretstore,sound,webview]'
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
  'boost-asio[ssl]',
  'boost-locale[icu]',
  'boost-mpi[python3]',
  'boost-odeint[mpi]',
  'boost-regex[icu]',
  'boost[mpi]',
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
  'hello-imgui[glfw-binding,opengl3-binding]',
  'libiconv',
  'icu[tools]',
  'imgui[glfw-binding,opengl3-binding,sdl3-binding,win32-binding]',
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
  'quickjs-ng',
  'rapidcsv',
  're2',
  'safeint',
  'sciter-js',
  'sfgui',
  'sdl2',
  'sdl2-image[libjpeg-turbo,libwebp,tiff]',
  'sdl2-mixer[fluidsynth,libflac,mpg123]',
  'sdl2-net',
  'sdl2-ttf[harfbuzz]',
  'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
  'sdl3',
  'sdl3-image[jpeg,png,tiff,webp]',
  'sdl3-mixer[fluidsynth,libflac,libvorbis,mpg123]',
  'sdl3-ttf[harfbuzz,svg]',
  'spirit-po',
  'sqlite-modern-cpp',
  'sqlite3[json1,tool,unicode,zlib]',
  'sqlitecpp',
  'status-code',
  'stduuid',
  'strtk[boost]',
  'tgui[sdl3,sfml,tool]',
  'tidy-html5',
  'tiff[cxx,jpeg,lzma,tools,webp,zip,zstd]',
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
  'wxwidgets[example,fonts,media,secretstore,sound,webview]',
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

def GetPackageListForPlatform(vcpkgPlatform: str) -> str_list:
  if (vcpkgPlatform == "arm64"):
    return arm64PackageList
  if (vcpkgPlatform == "x86"):
    return filter_list(packageList, x64OnlyPackageList)
  if (vcpkgPlatform == "x64"):
    return packageList
  raise ValueError(f"Unsupported platform '{vcpkgPlatform}'.")

def GetUnifiedPackageList() -> str_list:
  unifiedList: str_list = []
  arm64Packages: str_list = GetPackageListForPlatform("arm64")
  suffix: str = ":arm64-windows"
  arm64Packages = [pkg + suffix for pkg in arm64Packages]
  unifiedList.extend(arm64Packages)
  suffix = ":x64-windows"
  x64Packages: str_list = GetPackageListForPlatform("x64")
  x64Packages = [pkg + suffix for pkg in x64Packages]
  unifiedList.extend(x64Packages)
  x86Packages: str_list = GetPackageListForPlatform("x86")
  suffix = ":x86-windows"
  x86Packages = [pkg + suffix for pkg in x86Packages]
  unifiedList.extend(x86Packages)
  return unifiedList

def main():
  scriptDirectory: str = GetScriptDirectory()
  packages: str_list = GetUnifiedPackageList()
  return ModuleMain(scriptDirectory, packages, "nt")

if __name__ == "__main__":
    sys.exit(main())
