cmake_minimum_required(VERSION 3.5)
project(chatter_listener)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install launch files
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
