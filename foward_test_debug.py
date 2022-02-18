import gpiozero
import time 

robot = gpiozero.Robot(left=(17,18), right=(21,20)) 
robot2 = gpiozero.Robot(left=(22,27),right=(16,19))

for i in range(1):
	robot.forward()
	robot2.forward()
	time.sleep(1.5)
	robot.reverse()
	robot2.reverse()
	time.sleep(0.5)
	robot.forward()
	robot2.reverse()
	time.sleep(1.5)
	robot.reverse()
	robot2.forward()
	time.sleep(0.5)
