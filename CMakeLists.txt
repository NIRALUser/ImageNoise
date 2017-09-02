cmake_minimum_required( VERSION 3.5 )

project(ImageNoise)

find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

SEMMacroBuildCLI(
  NAME ImageNoise
  TARGET_LIBRARIES ${ITK_LIBRARIES}
  EXECUTABLE_ONLY
  )

