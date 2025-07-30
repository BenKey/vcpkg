#!/usr/bin/env python

import os
import subprocess
import sys

packageList = [
  ([
    'aixlog',
    'args',
    'better-enums',
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
    'color-console',
    'cpptoml',
    'guilite',
    'gumbo',
    'imgui[core,sdl3-binding,win32-binding]',
    'inipp',
    'jsoncons',
    'libguarded',
    'magic-enum',
    'nana',
    'platform-folders',
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
    'wildcards',
    'wxcharts',
    'wxwidgets[core,example,fonts,media,sound]'
  ], False),
]

def GetScriptFile() -> str:
  """Obtains the full path and file name of the Python script."""
  if (hasattr(GetScriptFile, "file")):
    return GetScriptFile.file
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
  GetScriptFile.file: str = ret
  return GetScriptFile.file

def GetScriptDirectory() -> str:
  """Obtains the path to the directory containing the script."""
  if (hasattr(GetScriptDirectory, "dir")):
    return GetScriptDirectory.dir
  module_path: str = GetScriptFile()
  GetScriptDirectory.dir: str = os.path.dirname(module_path)
  return GetScriptDirectory.dir

def InstallPackagesWorker(packages, triplet, recurse):
  args = []
  args.append("vcpkg")
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
    subprocess.check_call(args)
    return True
  except subprocess.CalledProcessError as err:
    return False
  except OSError as err:
    return False

def GetTriplet():
  return "x64-mingw-dynamic"

def InstallPackages(packages, recurse):
  triplet = GetTriplet()
  if (len(triplet) == 0):
    return False
  print()
  print("################################################################################")
  print("Installing packages: %s" % packages)
  print("################################################################################")
  print()
  ret = InstallPackagesWorker(packages, triplet, recurse)
  return ret

def InstallPackagesInPackageList():
  for package in packageList:
    ret = InstallPackages(package[0], package[1])
    if ret == False:
      return False
  return True

InstallPackagesInPackageList()
