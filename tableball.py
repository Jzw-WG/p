import pyHook,pythoncom  #导入pyHook库，可以在程序没有获得焦点的情况下检测到键盘输入，非常关键
import autopy,win32api,win32con  #autopy库用来获取鼠标位置  设置鼠标位置
import math
from ctypes import *
User32dll = windll.User32

# initial
radius = 12.70  #球的半径，具体是多少我也不清楚，多试了几次，发现这个值差不多

# position of ball and drop
source_x,source_y = 1.0,1.0        # 目标球位置
dest_x,dest_y = 2.0,2.0           # 目标袋口位置 

# 根据目标球、目标袋口位置计算母球应该打到的位置
def calculateMotherBall(source_x,source_y,dest_x,dest_y):
    result_x,result_y = 0.0,0.0
    distance = math.sqrt((source_x - dest_x)**2 + (source_y - dest_y)**2)
    if source_x == dest_x and source_y == dest_y :
       print ("fatal error: points coincide!")
    elif source_x == dest_x:
       result_x = source_x
       result_y = 2.0*radius/distance*(source_y-dest_y) + source_y
    elif source_y == dest_y:
       result_y = source_y
       result_x = 2.0*radius/distance*(source_x-dest_x) + source_x
    else:
       result_x = 2.0*radius/distance*(source_x-dest_x) + source_x
       result_y = 2.0*radius/distance*(source_y-dest_y) + source_y
    return result_x,result_y

# 按键处理函数，附带使用说明
# 将鼠标移动到目标球上，再按S键，记录目标球位置
# 将鼠标移动到目标袋口，再按D键，记录目标袋口位置
# 按F键，计算母球应该打到的位置，并设置鼠标到它应该去的地方
def onKeyboardEvent(event):
    global source_x,source_y,dest_x,dest_y

    if event.Key == 'S':
       source_x,source_y = autopy.mouse.location()
       print ("source pos: ",source_x,source_y)
    if event.Key == 'D':
       dest_x,dest_y = autopy.mouse.location()
       print ("dest pos: ",dest_x,dest_y)
    if event.Key == 'F':
       a,b = calculateMotherBall(source_x,source_y,dest_x,dest_y)
       # autopy.mouse.move(int(a),int(b))
       # more accurate mouse control: SetCursorPos!
# autopy库里面设置鼠标位置的函数精度不够，常会有5个像素左右的误差，所以改用下面的动态链接库
       User32dll.SetCursorPos(int(a),int(b))
       print ("result pos: ",int(a),int(b))
# 如果可以把int(a)改成int(round(a))，效果会更好。但是始终报错，过不了，不知道为啥。有人知道的，麻烦告诉一声，谢谢。
# 以下是套路，开启监测模式

# create a hook obj
hm = pyHook.HookManager()

hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()

# loop
pythoncom.PumpMessages()