# talker and listener 
Steps to run talker and listener scripts :
* To run the talker and listener first we need to copy the 1_chatter_listener to ros2_ws src

```
cp -r /home/(user_name)/MARIO/2_dh_simulation /home/(user_name)/ros2_ws/src
```
* To build the necesarry packages we need to install them so for that go to ros2_ws
```
cd ros2_ws
```
* Then to build run:
```
colcon build
```
* Now we need to source it
```
source install/setup.bash
```
* Now run the talker
```
ros2 run chatter_listener talker.py
```
* To run the listener `open another terminal` and run:
```
source install/setup.bash
```
* Run the listener
```
ros2 run chatter_listener listener.py
```