cmake_minimum_required( VERSION 3.5 )
PROJECT(ImageNoise)

if(NOT SETIFEMPTY)
  macro(SETIFEMPTY)
    set(KEY ${ARGV0})
    set(VALUE ${ARGV1})
    if(NOT ${KEY})
      set(${KEY} ${VALUE})
    endif(NOT ${KEY})
  endmacro(SETIFEMPTY KEY VALUE)
endif(NOT SETIFEMPTY)
###
SETIFEMPTY(INSTALL_RUNTIME_DESTINATION bin)

find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})
include(${GenerateCLP_USE_FILE})

FIND_PACKAGE(ITK REQUIRED)
IF(ITK_USE_FILE)
  INCLUDE(${ITK_USE_FILE})
ENDIF()

set(Filter ImageNoise)

set(${Filter}_SOURCE ${Filter}.cxx)
GENERATECLP(${Filter}_SOURCE ${Filter}.xml)
add_executable( ${Filter} ${${Filter}_SOURCE})
target_link_libraries( ${Filter} ${ITK_LIBRARIES})

install( TARGETS ${Filter} RUNTIME DESTINATION ${INSTALL_RUNTIME_DESTINATION} )
