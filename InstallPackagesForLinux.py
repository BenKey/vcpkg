#!/usr/bin/env python

import sys

from InstallPackagesHelper import GetScriptDirectory
from InstallPackagesHelper import ModuleMain

type str_list = list[str]

packageList: str_list = [
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
    'atk',
    'atkmm',
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
    'rapidcsv',
    're2',
    'safeint',
    'sfgui',
    'sdl2[core,wayland,x11]',
    'sdl2-image[core,libjpeg-turbo,libwebp,tiff]',
    'sdl2-mixer[core,fluidsynth,libflac,mpg123]',
    'sdl2-net',
    'sdl2-ttf[harfbuzz]',
    'sdl2pp[sdl2-image,sdl2-mixer,sdl2-ttf]',
    'sdl3[alsa,wayland,x11]',
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
    'wt[dbo,openssl]',
    'wxcharts',
    'wxwidgets[core,example,fonts,media,secretstore,sound]',
    'yasm[tools]'
]

def GetHostTriplet() -> str:
    return "x64-linux"

def GetTriplet() -> str:
    return "x64-linux"

def GetPackageList(hostTriplet: str, triplet: str) -> str_list:
    packages: str_list = packageList
    suffix: str = f":{triplet}"
    packages = [pkg + suffix for pkg in packages]
    return packages

def main() -> int:
    scriptDirectory: str = GetScriptDirectory()
    hostTriplet: str = GetHostTriplet()
    triplet: str = GetTriplet()
    packages: str_list = GetPackageList(hostTriplet, triplet)
    print()
    print(f"Script directory: {scriptDirectory}")
    print()
    return ModuleMain(scriptDirectory, packages, hostTriplet)

if __name__ == "__main__":
    sys.exit(main())
