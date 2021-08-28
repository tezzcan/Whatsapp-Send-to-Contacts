import pandas as pd
from time import sleep
import functions

EXCEL_FILE = "contacts.xlsx"
MESSAGE = "This is a test message"

data = pd.read_excel(EXCEL_FILE)
phones = functions.refactor(data)


print("Script will try to detect your Whatsapp Web window.")
input("So make it ready then come here and press <ENTER>")
print("Plase go that window in 5 seconds and wait.")
sleep(5)


for contact in phones:
    functions.sendMsg(MESSAGE, contact)
