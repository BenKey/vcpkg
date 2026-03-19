set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE static)

set(VCPKG_CMAKE_SYSTEM_NAME FreeBSD)

# List of ports that must NOT see /usr/local to avoid "Header Pollution"
set(SYSTEM_PATH_BLACKLIST "abseil;icu;libiconv;protobuf;sqlite3")

if(PORT IN_LIST SYSTEM_PATH_BLACKLIST)
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
