# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_chatter_listener_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED chatter_listener_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(chatter_listener_FOUND FALSE)
  elseif(NOT chatter_listener_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(chatter_listener_FOUND FALSE)
  endif()
  return()
endif()
set(_chatter_listener_CONFIG_INCLUDED TRUE)

# output package information
if(NOT chatter_listener_FIND_QUIETLY)
  message(STATUS "Found chatter_listener: 0.0.0 (${chatter_listener_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'chatter_listener' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${chatter_listener_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(chatter_listener_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${chatter_listener_DIR}/${_extra}")
endforeach()