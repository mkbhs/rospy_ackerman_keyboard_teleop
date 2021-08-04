# Simple ROS-Python Teleop Node for Ackerman-based vehicles

Simple Python ROS node for teleoperating an ackerman-based vehicle via keyboard inputs by publishing steering and velocity setpoint commands.


## Basic Keyboard Input
```
A -> turn to the left
D -> turn to the right
W -> increase forward velocity
S -> decrease forward velocity
```

## Published Topics
```
/steering_cmd -> setpoint command for steering angle (Float64)
/vel_cmd -> setpoint command for forward velocity (Float64)
```
