Driver ROS per un generico joystick

ROS driver for a generic Linux joystick. The joy package contains joy_node, a node that interfaces a generic Linux joystick to ROS. This node publishes a "Joy" message, which contains the current state of each one of the joystick's buttons and axes.

### Setup ###
```
sudo apt-get install ros-indigo-joy
```
```
sudo chmod a+rw /dev/input/js0
rosparam set joy_node/dev "/dev/input/jsX"
```
### Esecuzione ###
```
rosrun joy joy_node
```

### /joy.buttons: ###
| Index | Button name |
| :---: | :--- |
| 0 | A |
| 1 | B |
| 2 | X |
| 3 | Y |
| 4 | LB |
| 5 | RB |
| 6 | back |
| 7 | start |
| 8 | power |
| 9 | Button stick left |
| 10 | Button stick right |

### /joy.axis: ###
| Index | Button name |
| :---: | :--- |
| 0 | Left/Right Axis stick left |
| 1 | Up/Down Axis stick left |
| 2 | LT |
| 3 | Left/Right Axis stick right |
| 4 | Up/Down Axis stick right |
| 5 | RT |
| 6 | cross key left/right |
| 7 | cross key up/down |
