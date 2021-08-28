import pyautogui as pyg
from time import sleep
import os

path_parent = os.getcwd()
assets_path = path_parent + "/assets"


def refactor(excel_dt):

    to_modify = [
        str(number).replace(" ", "") for number in excel_dt["Contact Number"].to_list()
    ]

    dummy = []
    for item in to_modify:
        dummy_it = ""
        if item[:3] == "+90":
            dummy.append(item)
        else:
            dummy_it = "+90" + item
            dummy.append(dummy_it)

    return dummy


def sendMsg(msg, contact):

    search_box = pyg.locateCenterOnScreen(f"{assets_path}/light.png")
    if search_box == None:
        search_box = pyg.locateCenterOnScreen(f"{assets_path}/dark.png")

    if search_box == None:
        print("Something is not right. Could not find the search bar")
        return

    x, y = search_box
    pyg.click(x, y)
    pyg.write(contact)
    sleep(1)
    pyg.press("down")
    pyg.press("enter")
    pyg.write(msg)
    pyg.press("enter")
    sleep(0.5)
