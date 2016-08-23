cmake_minimum_required(VERSION 3.0)
project(cute_example LANGUAGES CXX VERSION 2.0.0)

# Default to building the 'Release' configuration
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING "The build configuration" FORCE)
endif()

# Prepare Conan.io packages
set(CONAN_BUILD_INFO_FILE ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
if(NOT EXISTS ${CONAN_BUILD_INFO_FILE})
  message(STATUS "No conan package information available. Trying to fix that!")
  execute_process(COMMAND conan install --build=missing ${CMAKE_CURRENT_SOURCE_DIR} OUTPUT_QUIET)
endif()

# Set basic compiler flags.
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Werror -pedantic -std=c++14")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS} -g")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS} -Os")

# Import dependencies via Conan.io
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
set(CONAN_SYSTEM_INCLUDES On)
conan_basic_setup()

# Add the example target
add_executable(${PROJECT_NAME} example.cpp)
