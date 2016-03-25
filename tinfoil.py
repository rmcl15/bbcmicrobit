from microbit import *
while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    elif pin1.is_touched():
        display.show(Image.GIRAFFE) 
    else:
        display.show(Image.SAD) 
        display.clear()
     
     # print(pin0.is_touched())
       #sleep(1000)
# Write your code here :-)
# Made by Rmcl
