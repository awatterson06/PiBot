import gpiozero
import time
from bluedot import BlueDot

bd = BlueDot()
bd.wait_for_press()


robot = gpiozero.Robot(left=(17,18), right=(21,20)) 
robot2 = gpiozero.Robot(left=(22,27),right=(16,19))

def mov(pos):
    if pos.top:
        robot.forward()
        robot2.forward()
    elif pos.bottom:
        robot.backwards()
        robot2.backwards()
    elif pos.left():
        robot.left()
        robot2.left()
    elif pos.right():
        robot.right()
        robot2.right()
def stop()
    robot.stop()
    robot2.stop()
    
bd.when_pressed = move
bd.when_move = move
bd.when_released = stop
