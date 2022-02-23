###############################
# IMPORTS
###############################
import pyautogui
import time


songList = "Nike Ticks" #enter all the songs you have added


whatSong = input(f"What song would you like? {songList}\n")
##########################################
# SONG PLAYER
##########################################
if whatSong.lower() == 'nike ticks':
    time.sleep(5)
    import assets.NikeTicks
else:
    print("Sorry, we do not have that song in the playlist!")