set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE dynamic)

set(VCPKG_CMAKE_SYSTEM_NAME FreeBSD)

set(ALLOW_UNDEFINED_SYMBOLS_WHEN_LINKING_SHARED_LIBRARIES_LIST "atk;cairo;fontconfig;gdk-pixbuf;glib;gtk;harfbuzz;libarchive;pango;zix")
if(PORT IN_LIST ALLOW_UNDEFINED_SYMBOLS_WHEN_LINKING_SHARED_LIBRARIES_LIST)
  message(STATUS "FreeBSD Workaround: Allowing undefined symbols for port: ${PORT}")
  set(VCPKG_MESON_CONFIGURE_OPTIONS "-Db_lundef=false")
endif()

# Determine the C++ Standard that will be used for the current port.
set(CPP17_PORTS_LIST "libsass;nana")
if(PORT IN_LIST CPP17_PORTS_LIST)
  set(CPP_STANDARD "gnu++17")
else()
  set(CPP_STANDARD "gnu++23")
endif()

# Apply global VCPKG_C_FLAGS and VCPKG_CXX_FLAGS.
string(APPEND VCPKG_C_FLAGS " -std=gnu17")
string(APPEND VCPKG_CXX_FLAGS " -std=${CPP_STANDARD}")

# Conditional /usr/local Inclusion.
set(NO_USR_LOCAL_LIST "abseil;grpc;icu;libiconv;protobuf;sqlite3")
if(NOT (PORT IN_LIST NO_USR_LOCAL_LIST OR PORT MATCHES "boost"))
  # Tells CMake's find_package where to look
  list(APPEND VCPKG_CMAKE_CONFIGURE_OPTIONS "-DCMAKE_SYSTEM_PREFIX_PATH=${VCPKG_INSTALLED_DIR}/${VCPKG_TARGET_TRIPLET};/usr/local")
  # Force flags for non-CMake ports or ports that don't use find_package correctly
  string(APPEND VCPKG_C_FLAGS " -I/usr/local/include")
  string(APPEND VCPKG_CXX_FLAGS " -I/usr/local/include")
  string(APPEND VCPKG_LINKER_FLAGS " -L/usr/local/lib")
endif()
