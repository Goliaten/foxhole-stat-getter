from PIL import ImageGrab
import pytesseract
import pyautogui as pg
from time import sleep
from pprint import pprint
import json
import sys, os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
activity_time_offset = 0.5 #1s works well
name_center = (1026, 358)
activity_log = (1115, 402)
activity_offset = (89, 44)
violation_log = (1115, 430)
violation_offset = (89, 72)
out_data = {}
start_delay = 5 #in seconds
printout_log = ''

def get_text_from_position(position, show=False):
    img = ImageGrab.grab()
    img = img.crop( position )
    img = img.convert('L')
    if show:
        img.show()
    #img.save(f"{position}.png")
    return pytesseract.image_to_string(img)

def get_number(position):
    text = get_text_from_position(position)
    #print(repr(text), end=' -- ')
    text = text.split(' ')[1:]
    text = ''.join(text)
    text = text.replace(',', '').replace('.', '').replace('O', '0').replace('\n', '')
    if text == '':
        text = '0'
    #print(text, end='---')
    text = ''.join([x for x in text if x.isdigit()])
    #print(text, end='---')
    try:
        text = int(text)
    except Exception as e:
        print(e, (position[3]-33)/34)
        print(repr(text))
        text = 0
    #print(text)
    return text
    

def get_activity_2():
    sleep(activity_time_offset)
    off = -25
    
    numbers = [
        get_number( (l:=837+off, t:=157, l+120, t+33) ),
        get_number( (l:=850+off, t+34*1, l+120, t+33+34*1) ),
        get_number( (l:=929+off, t+34*2, l+120, t+33+34*2) ),
        get_number( (l:=942+off, t+34*3, l+120, t+33+34*3) ),
        get_number( (l:=836+off, t+34*4, l+120, t+33+34*4) ),
        get_number( (l:=810+off, t+34*5, l+120, t+33+34*5) ),
        get_number( (l:=795+off, t+34*6, l+120, t+33+34*6) ),
        get_number( (l:=800+off, t+34*7, l+120, t+33+34*7) ),
        get_number( (l:=886+off, t+34*8, l+120, t+33+34*8) ),
        get_number( (l:=904+off, t+34*9, l+120, t+33+34*9) ),
        get_number( (l:=900+off, t+34*10, l+120, t+33+34*10) ),
        get_number( (l:=905+off, t+34*11, l+120, t+33+34*11) ),
        get_number( (l:=831+off, t+34*12, l+120, t+33+34*12) ),
        get_number( (l:=823+off, t+34*13, l+120, t+33+34*13) ),
        get_number( (l:=847+off, t+34*14, l+120, t+33+34*14) ),
    ]
    
    activity = {
        "EnemyPlayerDamage": numbers[0],
        "FriendlyPlayerDamage": numbers[1],
        "EnemyStructure/VehicleDamage": numbers[2],
        "FriendlyStructure/VehicleDamage": numbers[3],
        "FriendlyConstruction": numbers[4],
        "FriendlyRepairing": numbers[5],
        "FriendlyHealing": numbers[6],
        "FriendlyRevivals": numbers[7],
        "VehiclesCapturedByEnemy": numbers[8],
        "VehicleSelfDamage(Neutral": numbers[9],
        "VehicleSelfDamage(Colonial": numbers[10],
        "VehicleSelfDamage(Warden": numbers[11],
        "MaterialsSubmitted": numbers[12],
        "MaterialsGathered": numbers[13],
        "SupplyValueDelivered": numbers[14],
    }
    return activity

#default is the position at the top of the viewport
def get_name(position = (927, 343, 1126, 373)):
    return get_text_from_position(position)

def check_if_active(position):
    rect = ( position[0]-88, position[1]-12, position[0]+88, position[1]+13)
    rect = ( rect[0]+89, rect[1]+44, rect[2]+89, rect[3]+44)
    img = ImageGrab.grab()
    img = img.crop(rect)
    text = pytesseract.image_to_string(img).lower()
    if text == 'activity log\n':
        return 'AL'
    
    rect = ( rect[0], rect[1]+28, rect[2], rect[3]+28)
    img = ImageGrab.grab()
    img = img.crop(rect)
    text = pytesseract.image_to_string(img).lower()
    if text == 'activity log\n':
        return 'WH'
    else:
        return 'RP'


#open only the first guy
def open_activity(position = name_center, log=activity_log):
    #check, if player is online or not
    #click on center of name
    pg.moveTo( position )
    pg.rightClick()
    
    control = check_if_active(position)
    if control == 'RP':
        pg.moveTo( ( log[0], log[1]+(28*2) ) )
        pg.click()
    elif control == 'AL':
        #click on center of activity log
        pg.moveTo( log )
        pg.click()
    elif control == 'WH':
        pg.moveTo( ( log[0], log[1]+(28*1) ) )
        pg.click()
    
def stats():
    pg.typewrite(['f1'])

def exit():
    pg.typewrite(['esc'])

def scroll(amount, multi=-1):
    pg.scroll(amount * multi)

def clean_data(data):
    data = data.replace('|', '').replace('+', '').replace('"', '').replace(' ', '').replace(',', '').replace('_', '').replace('.', '').replace(']', '').replace('}', '').replace('\\', '').replace(')', '')
    data = data.split('\n')
    data = [x for x in data if x != '']
    data = [x.split(':') for x in data]
    pprint(data)
    data = [ x if len(x) == 2 else [x[0], '0'] for x in data]
    data = [ [x[0], x[1]] if x[1] != '' else [x[0], '0'] for x in data]
    data = {x[0]: int(x[1].replace('O', '0'))    for x in data}
    return data

def save_data(name, data):
    
    name = name.replace('\n', '')
    out_data[name] = data
    
def save_to_file():
    with open('out.json', 'w') as file:
        file.write(json.dumps(out_data, indent=2))

def start_screen():
    print("This script will allow you to gather activity statistics of everyone in your regiment.")
    print("It works by controlling the mouse to show activity logs, and scanning the screen, therefore it's recommended to not use mouse while it's running")
    print("--\nIf at any moment you want to stop the script, move your mouse to top-left of the screen.\n--")
    print("At the start mouse will move to the area, on which foxhole should be opened. In foxhole you be spawned in, and should NOT have any menu/F1 open.")
    
def countdown(cnt):
    for x in range(cnt, 0):
        print(f"starting in {x}s")
        sleep(1)

def main():
    
    global printout_log
    
    # focus on game, assumed to be on screen one, 1920x1080
    start_screen()
    
    pg.click( (100, 100) )
    
    input("\nPress enter in terminal to start\n")
    countdown(start_delay)
    print("Starting")
    
    pg.click( (100, 100) )

    #open stats
    stats()

    # iterate over people
    counter = 0
    while True:
        if counter % 50 == 0 and counter != 0:
            scroll(-37 + 3 + 3)
        elif counter % 50 in (20, 30):
            scroll(-3)
        #single iteration of a loop
        name = get_name()
        if name == "":
            name = f"__{counter}__"
        print(name)
        printout_log += f"{name}\n"
        
        open_activity()
        data = get_activity_2()
        save_data(name, data)
        
        exit()
        stats()
        
        scroll(132) #need to scroll 35 pixels, and 132 = 35
        counter += 1
        
        if get_name() == name:
            counter += 1
            if counter > 4:
                break

    # iterate over people at the end of the list
    for x in range(1, 10):
        v_off = 35*x #vertical offset
        name = get_name( (927, 343 + v_off, 1126, 373 + v_off) ) #name_frame
        
        if name == "":
            name = f"__{counter}__"
        print(name)
        printout_log += f"{name}\n"
        
        open_activity( (1026, 358+v_off), (1115, 402+v_off) ) #name_center, activity_log
        data = get_activity_2()
        #pprint(data)
        save_data(name, data)
        exit()
        stats()

    save_to_file()
    exit()
    
if __name__ == '__main__':
    try:
        main()
    except pg.FailSafeException:
        print("Failsafe triggered.")
        print("Progress saved.")
        save_to_file()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        
        print(f"Exception occured -- {e} -- {type(e)}")
        print(exc_type, fname, exc_tb.tb_lineno)
        print("Progress saved.")
        save_to_file()
        
    with open("log.txt", "w", encoding="utf-8") as file:
        file.write(printout_log)
    
    input("Press enter to exit")