#!/bin/bash

vcpkgRootDir=$(X= cd -- "$(dirname -- "$0")" && pwd -P)
declare -a subdirectories
subdirectories=( "bt" "buildtrees" "downloads" "installed" "packages" )

for dir in "${subdirectories[@]}"
do
  if [ -d "${vcpkgRootDir}/${dir}" ]
  then
    echo "Deleting directory: $dir"
    rm -rf "${vcpkgRootDir}/${dir}"
  else
    echo "Directory not found: ${vcpkgRootDir}/${dir}"
  fi
done

[ -f "${vcpkgRootDir}/vcpkg" ] && rm -f "${vcpkgRootDir}/vcpkg"
[ -f "${vcpkgRootDir}/vcpkg.exe" ] && rm -f "${vcpkgRootDir}/vcpkg.exe"
