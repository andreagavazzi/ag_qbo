# joy #
http://wiki.ros.org/joy  
È il prerequisito per il funzionamento di qbo_joy. Si tratta di un driver ROS per un generico joystick connesso a Linux. Il package contiene joy_node, un nodo che si interfaccia al joystick pubblicando un messaggio "Joy" che contiene lo stato di ogni asse e bottone.
Per verificare la connessione al SO ed individuare il suo numero di riferimento js:
```
ls /dev/input/
```
### Setup ###
```
sudo apt-get install ros-xxxxxxxxx-joy
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
il [sensor_msgs/Joy](http://docs.ros.org/api/sensor_msgs/html/msg/Joy.html) sarà simile a:

>header:   
>  seq: 9414  
>  stamp:   
>    secs: 1325530130  
>    nsecs: 146351623  
>  frame_id: ''  
>axes: [-0.0038758506998419762, -0.0038453321903944016, -0.0, -0.999969482421875, 0.0, 0.0]  
>buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    


### Messagio /Joy: ###
| **joy.buttons** | Descrizione |  | **joy.axis** | Descrizione |
| :---: | :--- | --- | :---: | :--- |
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

**Esempio**
```python
rospy.Subscriber('/joy', Joy, callback)
def callback():
    if data.axes[3] != 0:
    ...
```

# qbo_joy #


