from time import sleep
import os


class Messager:
    def __init__(self, pyg=None):
        self.path_parent = os.getcwd()
        self.assets_path = self.path_parent + "/assets"
        self.pyg = pyg

    def validate(self, msg):
        return isinstance(msg, str)

    def refactor(self, excel_dt):

        to_modify = [
            str(number).replace(" ", "")
            for number in excel_dt["Contact Number"].to_list()
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

    def sendMsg(self, msg, contact):

        if not self.validate(msg):
            print("The message that you provided needs to a string")
            return

        search_box = self.pyg.locateCenterOnScreen(f"{self.assets_path}/light.png")
        if search_box == None:
            search_box = self.pyg.locateCenterOnScreen(f"{self.assets_path}/dark.png")

        if search_box == None:
            print("Something is not right. Could not find the search bar")
            return

        x, y = search_box
        self.pyg.click(x, y)
        self.pyg.write(contact)
        sleep(1)
        self.pyg.press("down")
        self.pyg.press("enter")
        self.pyg.write(msg)
        self.pyg.press("enter")
        sleep(0.5)
