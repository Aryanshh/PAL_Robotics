# PAL_Robotics

# Intralogistics Simulation with DummySensor (Gazebo Harmonic + ROS 2)

This project demonstrates a simple intralogistics robot simulation using **Gazebo Harmonic** and **ROS 2**, featuring a custom Gazebo sensor plugin called `DummySensor`. The plugin publishes "Hello World" to a ROS 2 topic using `gz-transport` when loaded.

## Features

- Warehouse-style simulated world
- Mobile robot model (`simple_agv`)
- Custom Gazebo Harmonic plugin (`DummySensor`)
- ROS 2 integration using `gz-transport`
- Easily extendable to simulate RFID tags

---

## Requirements

- Ubuntu 22.04
- [ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html)
- [Gazebo Harmonic](https://gazebosim.org/docs/harmonic/installation)
- `colcon` build system

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/intralogistics_gz_sim.git
cd intralogistics_gz_sim

sudo apt update
sudo apt install -y lsb-release wget gnupg
sudo sh -c 'echo "deb [arch=amd64] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
sudo apt install -y gazebo-harmonic


cd ~/intralogistics_gz_sim
colcon build
source install/setup.bash


cd ~/intralogistics_gz_sim
colcon build
source install/setup.bash

ros2 launch simple_agv demo.launch.py



  
