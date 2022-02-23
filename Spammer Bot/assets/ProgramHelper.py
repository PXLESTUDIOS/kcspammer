import pyautogui
import time


def play(filename):
    lyr = open(filename)
    
    for each_line in lyr:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
        time.sleep(0.7)



def imports():
    print("""
    The text below this shows what you put in the SONG PLAYER section:
    if whatSong == \'song name\':
        time.sleep(5)
        import assets.program_name
    """)




    

