set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE static)

set(VCPKG_CMAKE_SYSTEM_NAME FreeBSD)

# List of ports that should allow undefined symbols when linking shared
# libraries.
set(ALLOW_UNDEFINED_SYMBOLS_WHEN_LINKING_SHARED_LIBRARIES_LIST "gtk")
if(PORT IN_LIST ALLOW_UNDEFINED_SYMBOLS_WHEN_LINKING_SHARED_LIBRARIES_LIST)
  set(VCPKG_MESON_CONFIGURE_OPTIONS "-Db_lundef=false")
endif()

# List of ports that must NOT use '-I/usr/local/include' and '-L/usr/local/lib'.
set(NO_USR_LOCAL_LIST "abseil;grpc;icu;libiconv;protobuf;sqlite3")
if(PORT IN_LIST NO_USR_LOCAL_LIST)
    message(STATUS ">>> [CUSTOM TRIPLET] Building ${PORT} without '-I/usr/local/include' and '-L/usr/local/lib'.")
    set(VCPKG_C_FLAGS "-std=gnu17")
    set(VCPKG_CXX_FLAGS "-std=gnu++17")
    set(VCPKG_LINKER_FLAGS "")
else()
    set(VCPKG_C_FLAGS "-I/usr/local/include -std=gnu17")
    set(VCPKG_CXX_FLAGS "-I/usr/local/include -std=gnu++17")
    set(VCPKG_LINKER_FLAGS "-L/usr/local/lib")
endif()

# Fallback search paths for CMake-based ports
list(APPEND VCPKG_CMAKE_CONFIGURE_OPTIONS
    "-DCMAKE_REQUIRED_INCLUDES=/usr/local/include"
    "-DCMAKE_REQUIRED_LIBRARIES=/usr/local/lib"
    "-DCMAKE_PREFIX_PATH=/usr/local"
)
