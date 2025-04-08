# Generic ROS 2 Topic Subscriber

This package provides a generic subscriber that can listen to any ROS 2 topic, regardless of its message type. It dynamically loads the message type and prints out incoming data.

## Features

- Subscribe to any topic by name and type.
- Print received message with its data and type.
- Includes test publishers for `std_msgs/String`, `std_msgs/Int32`, and `geometry_msgs/Twist`.

## Installation

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/your_username/ros2_generic_subscriber.git
cd ..
colcon build
source install/setup.bash

