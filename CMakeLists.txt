CMAKE_MINIMUM_REQUIRED( VERSION 2.6 )
CMAKE_POLICY(VERSION 2.6)
PROJECT(ImageNoise)

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

