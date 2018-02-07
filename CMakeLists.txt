cmake_minimum_required(VERSION 3.5)
project(ptex VERSION 2.1.28)

include(GNUInstallDirs)
include(CTest)
include(FindZLIB)
include(FindThreads)

enable_testing()

# Detect the build type from the $FLAVOR environment variable
if ("$ENV{FLAVOR}" MATCHES "debug")
    set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "type of build" FORCE)
else ()
    set(CMAKE_BUILD_TYPE "Release" CACHE STRING "type of build" FORCE)
endif ()

if (NOT WIN32)
    set(CMAKE_CXX_FLAGS "-std=c++98 -Wall -Wextra -pedantic")
endif ()

if(MSVC)
    add_definitions(

        #warning C4800: 'BOOL': forcing value to bool 'true' or 'false' (performance warning)
        /wd4800 

        #warning C4244: 'argument': conversion from 'double' to 'float', possible loss of data
        /wd4244 

        /D_CRT_SECURE_NO_WARNINGS
    )
endif()

if (${PRMAN_15_COMPATIBLE_PTEX})
    add_definitions(-DPTEX_NO_LARGE_METADATA_BLOCKS)
endif ()

include_directories(${ZLIB_INCLUDE_DIR})

add_subdirectory(src/ptex)
add_subdirectory(src/utils)
add_subdirectory(src/tests)
add_subdirectory(src/doc)

configure_file(cmake/Ptex-config-version.cmake.in ${CMAKE_CURRENT_BINARY_DIR}/Ptex-config-version.cmake @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/Ptex-config-version.cmake DESTINATION ${CMAKE_INSTALL_PREFIX}/cmake)
