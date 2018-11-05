# ag_qbo
Programmi e applicazioni per il progetto "Qbo Reloaded" che modifica, anche a livello hardware, l'ormai abbandonato qbo di The Corpora.

## qbo_arduqbo       
Driver per l'attivazione delle funzionalità base.
```
roslaunch qbo_arduqbo qbo_arduqbo_default.launchh
```
Topics:
### /cmd_joints
Gestisce il movimento (pan e tilt) della testa con un messaggio sensor_msgs/JointState  
**Pan** (Position limit:)

```
rostopic pub -1 /cmd_joints sensor_msgs/JointState '{header: auto, name: ['head_pan_joint'], position: [0], velocity: [], effort: []}'
```
**Tilt** (Position limit: -0.659 ... 0.349)
```
rostopic pub -1 /cmd_joints sensor_msgs/JointState '{header: auto, name: ['head_tilt_joint'], position: [0], velocity: [], effort: []}'
```
**Combinati**
```
rostopic pub -1 /cmd_joints sensor_msgs/JointState '{header: auto, name: ['head_pan_joint', 'head_tilt_joint'], position: [0, 0], velocity: [], effort: []}'
```
  
### /cmd_lcd
Gestisce il display sul retro del robot

```
rostopic pub -1 /cmd_lcd std_msgs/String "nTesto"
```
n = blank/1/2/3/4 è il numero di riga


### /cmd_mouth
Gestisce i led della bocca (0b + status dei 5 led per ogni riga)

|  | A | B | C | D | E |
| :---: | :---: | :---: | :---: | :---: | :---: |
| *0b* | 0 | 0 | 0 | 0 | 0 |
| *0b* | 0 | 0 | 0 | 0 | 0 |
| *0b* | 0 | 0 | 0 | 0 | 0 |
| *0b* | 0 | 0 | 0 | 0 | 0 |

Off  
```
rostopic pub -1 /cmd_mouth std_msgs/ByteMultiArray "{}" [0b00000,0b00000,0b00000,0b00000]
```
Kiss
```
rostopic pub -1 /cmd_mouth std_msgs/ByteMultiArray "{}" [0b00100, 0b01110, 0b01110, 0b00100]
```
Smile
```
rostopic pub -1 /cmd_mouth std_msgs/ByteMultiArray "{}" [0b00000, 0b11111, 0b11111, 0b01111]
```

### /cmd_nose
Gestisce il led del naso
Riceve UInt16 standard message. Valori sopra 3 non sono usati (0: off, 1: rosso, 2: blu, 3: viola)
```
rostopic pub -1 /cmd_nose std_msgs/Uint16 2
```

### /cmd_vel
Gestisce i 2 motori del robot
```
rostopic pub /cmd_vel geometry_msgs/Twist ‘{linear: {x:1.0}}’ -r 10
```

___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=200)
