vcpkg_check_linkage(ONLY_STATIC_LIBRARY)

vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO woollybah/gppanel
    REF f58a9028f7c9a8e9b4324ff2165951f558365f90
    SHA512 4ec5fbef4c487d351c60f48b0c0e41c5d077989ab96f827b9fd5ef01c167d50f39a313bd82db1b5df19d14025983e83db4d19cc4048c1c50fc8ef9128de15575
    HEAD_REF master
    PATCHES 
        00001-fix-build.patch
        use-complex-header.patch
        fix-missing-headers.patch # https://github.com/woollybah/gppanel/pull/5
)

file(COPY ${CMAKE_CURRENT_LIST_DIR}/CMakeLists.txt DESTINATION ${SOURCE_PATH})

# Only apply the manual bypass when cross-compiling for MinGW from a Non-Windows host
if(VCPKG_TARGET_IS_MINGW AND NOT VCPKG_HOST_IS_WINDOWS)
    message(STATUS "Applying MinGW-on-Linux bypass for wxWidgets discovery")
    # 1. Inject variables including BOTH header paths (main and setup.h)
    vcpkg_replace_string(
        "${SOURCE_PATH}/CMakeLists.txt"
        "project(gpPanel CXX)"
        "project(gpPanel CXX)
set(wxWidgets_FOUND TRUE)
set(wxWidgets_INCLUDE_DIRS \"${CURRENT_INSTALLED_DIR}/include/wx-3.3\" \"${CURRENT_INSTALLED_DIR}/lib/wx/include/msw-unicode-3.3\")
set(wxWidgets_LIBRARIES \"-L${CURRENT_INSTALLED_DIR}/lib\" \"wx_mswu_core-3.3\" \"wx_baseu-3.3\")"
    )
    # 2. Comment out the lines that trigger the broken vcpkg-cmake-wrapper
    vcpkg_replace_string("${SOURCE_PATH}/CMakeLists.txt" "find_package(wxWidgets REQUIRED COMPONENTS core base)" "# find_package bypassed")
    vcpkg_replace_string("${SOURCE_PATH}/CMakeLists.txt" "include(\${wxWidgets_USE_FILE})" "# include bypassed")
    # 3. Force the target to use these injected paths
    file(APPEND "${SOURCE_PATH}/CMakeLists.txt" "\ntarget_include_directories(gpPanel PRIVATE \${wxWidgets_INCLUDE_DIRS})\ntarget_link_libraries(gpPanel PRIVATE \${wxWidgets_LIBRARIES})\n")
    vcpkg_cmake_configure(
        SOURCE_PATH "${SOURCE_PATH}"
        OPTIONS -DCMAKE_CXX_STANDARD=11
    )
else()
    # Standard behavior for Native Windows or Linux
    vcpkg_cmake_configure(
        SOURCE_PATH "${SOURCE_PATH}"
        OPTIONS -DCMAKE_CXX_STANDARD=11
    )
endif()

vcpkg_cmake_install()
vcpkg_copy_pdbs()
vcpkg_cmake_config_fixup(CONFIG_PATH share/cmake/gpPanel)

file(REMOVE_RECURSE ${CURRENT_PACKAGES_DIR}/debug/include)
file(REMOVE_RECURSE ${CURRENT_PACKAGES_DIR}/debug/share)

configure_file(${SOURCE_PATH}/LICENSE ${CURRENT_PACKAGES_DIR}/share/gppanel/copyright COPYONLY)
