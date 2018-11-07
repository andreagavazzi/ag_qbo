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
| joy.buttons | Descrizione |  | joy.axis | Descrizione |
| :---: | :--- | :--- | --- | :--- | :--- |
| 0 | A |  | 0 | Left/Right Axis stick left |
| 1 | B |  | 1 | Up/Down Axis stick left |
| 2 | X |  | 2 | LT |
| 3 | Y |  | 3 | Left/Right Axis stick right |
| 4 | LB |  | 4 | Up/Down Axis stick right |
| 5 | RB |  | 5 | RT |
| 6 | back |  | 6 | cross key left/right |
| 7 | start |  | 7 | cross key up/down |
| 8 | power |
| 9 | Button stick left |
| 10 | Button stick right |


