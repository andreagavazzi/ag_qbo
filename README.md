## ag_qbo
Programmi e applicazioni per il progetto "Qbo Reloaded" che modifica, anche a livello hardware, l'ormai abbandonato qbo di The Corpora.

## qbo_arduqbo       
Driver per l'attivazione delle funzionalità base.
```
roslaunch qbo_arduqbo qbo_arduqbo_default.launchh
```
Topics:
### /cmd_joints
Gestisce il movimento (pan e tilt) della testa
### /cmd_lcd
Gestisce il display sul retro del robot

```
rostopic pub -1 /cmd_lcd std_msgs/String "nTesto"
```
n = blank/1/2/3/4 è il numero di riga


### /cmd_mouth
Gestisce i led della bocca (un codice 0b... per ogni linea di led)

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
### /cmd_vel
Gestisce i 2 motori del robot
```
rostopic pub /cmd_vel geometry_msgs/Twist ‘{linear: {x:1.0}}’ -r 10
```

___
![alt text](https://gavazzionline.files.wordpress.com/2014/01/img_6916.jpg?w=300)
