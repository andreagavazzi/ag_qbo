Driver ROS per un generico joystick connesso a Linux. Il package contiene joy_node, un nodo che si interfaccia al joystick pubblicando un messaggio "Joy" che contiene lo stato di ogni asse e bottone.
Per verificare la connessone
```
ls /dev/input/
```
### Setup ###
```
sudo apt-get install ros-indigo-joy
```
```
sudo chmod a+rw /dev/input/js0
```
```
rosparam set joy_node/dev "/dev/input/jsX"
```
### Esecuzione ###
```
rosrun joy joy_node
```

### Messagio /Joy: ###
| Index | Modulo | Descrizione |  | Modulo | Descrizione |
| :---: | :--- | :--- | --- | :--- | :--- |
| 0 | joy.buttons | A |  | joy.axis | Left/Right Axis stick left |
| 1 | joy.buttons | B |  | joy.axis | Up/Down Axis stick left |
| 2 | joy.buttons | X |  | joy.axis | LT |
| 3 | joy.buttons | Y |  | joy.axis | Left/Right Axis stick right |
| 4 | joy.buttons | LB |  | joy.axis | Up/Down Axis stick right |
| 5 | joy.buttons | RB |  | joy.axis | RT |
| 6 | joy.buttons | back |  | joy.axis | cross key left/right |
| 7 | joy.buttons | start |  | joy.axis | cross key up/down |
| 8 | joy.buttons | power |
| 9 | joy.buttons | Button stick left |
| 10 | joy.buttons | Button stick right |


