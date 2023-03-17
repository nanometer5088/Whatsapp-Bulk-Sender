import pywhatkit
import time

from src.file import read_excel_file, saudacao
from src.contants import MESSAGE

file_path = "example.xlsx"
name, phone_no, sex, messages = read_excel_file(file_path)

for i in range(len(phone_no)):
    message = f"{saudacao()}, {name[i]}.\n{MESSAGE[f'{int(messages[i])}']}"
    pywhatkit.sendwhatmsg_instantly(phone_no[i], message, tab_close=True)
    time.sleep(3)