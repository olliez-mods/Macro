from tkinter.constants import RIGHT
import pyautogui
import keyboard
import time

#from datetime import datetime

coms = ""
stop = False
stopKey = "~"
count = 0


def setStop(stopKey_new):
    global stopKey
    stopKey = stopKey_new

def confirm(to_say):
    answer = pyautogui.confirm(to_say)
    if(answer == "OK"):
        return True
    return False
    

def checkForStop():
    global stopKey
    global coms
    global count
    if (keyboard.is_pressed(stopKey) and coms != []):
        print("stopping")
        for to_del in range(len(coms)):
            if (coms[0] == "onEnd"):
                del coms[0]
                break
            del coms[0]
        count = -1
        stopKey = "END"
        return True
    return False



def exe(data):
    global coms
    global stop
    global count

    if data[0] == "click":
        pyautogui.click()
    elif data[0] == "Rclick":
        pyautogui.rightClick()
    elif data[0] == "move":
        pyautogui.moveTo(int(data[1]), int(data[2]))
    elif data[0] == "moveRel":
        pyautogui.moveRel(int(data[1]), int(data[2]))
    elif data[0] == "keyDown":
        pyautogui.keyDown(data[1])
    elif data[0] == "keyUp":
        pyautogui.keyUp(data[1])
    elif data[0] == "wait":
        time.sleep(float(data[1]) % 1)
        for i in range(int(float(data[1]))):
            time.sleep(1)
            if(checkForStop()):
                return
    elif data[0] == "press":
        pyautogui.press(data[1])
    elif data[0] == "repeat":
        count = -1
    elif data[0] == "confirm":
        if(confirm(data[1].replace("_", " "))):
            del data[0]
            del data[0]
            exe(data, coms)
    elif data[0] == "type":
        pyautogui.typewrite(data[1].replace("_", " "), data[2])
    elif data[0] == "alert":
        pyautogui.alert(data[1].replace("_", " "))
    elif data[0] == "mouseDown":
        pyautogui.mouseDown()
    elif data[0] == "mouseUp":
        pyautogui.mouseUp()
    elif data[0] == "RmouseDown":
        pyautogui.mouseDown(button=RIGHT)
    elif data[0] == "RmouseUp":
        pyautogui.mouseUp(button=RIGHT)
    elif data[0] == "once":
        del data[0]
        exe(data)
        coms[count] = " "
    elif data[0] == "exit":
        stop = True
    elif data[0] == "onEnd":
        stop = True
    elif data[0] == "counter":
        if(int(data[2]) == int(data[1])):
            data[2] = str(0)
            coms[count] = " ".join(data)
            temp_data = data.copy()
            del temp_data[0]
            del temp_data[0]
            del temp_data[0]
            exe(temp_data)
        else:
            data[2] = str(int(data[2])+1)
            coms[count] = " ".join(data)

def run(comands):
    
    #date_time_str = '9/11/21 16:10:00'
    #date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

    #if(datetime.now() >  date_time_obj ):
    #    pyautogui.alert("Sorry the time trial has expired.")
    #    return
    global stopKey

    global stop
    stop = False

    global coms
    coms = comands
    
    global count
    count = 0
    while(not stop):
        com = comands[count]

        data = com.split(" ")
        exe(data)

        checkForStop()

        
        count += 1
        if(count == len(coms)):
            stop = True



