import json
from plugins.LanguageManager import LanguageManager
from plugins.Modules.E_Language import E_Language
try:
    from pyrogram import Client , filters
    from pyrogram.types import InputMediaPhoto, InputMediaVideo , ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
    from pyrogram.raw.functions.messages import EditMessage
except ModuleNotFoundError:
    import os
    os.system("pip install pyrogram")
    os.system("pip3 install -U tgcrypto")
    os.system("pip install tinydb")
    print("\n\n[[[[[[Modules installed]]]]]]\nRestart the program")
    quit()
api_id = 2496
api_hash = '8da85b0d5bfe62527e5b244c209159c3'

botClient=Client("my_account",api_id,api_hash,plugins=dict(root="plugins"))

SystemTexts = {}
with open("SystemLang1.json", encoding="utf8") as _EnglishResource:
    DictLangEnglish = json.load(_EnglishResource)
    SystemTexts[E_Language.English] = DictLangEnglish

with open("SystemLang2.json", encoding="utf8") as _RussianResource:
    DictLangRussian = json.load(_RussianResource)
    SystemTexts[E_Language.Russian] = DictLangRussian

with open("SystemLang3.json", encoding="utf8") as _HindiResource:
    DictLangHindi = json.load(_HindiResource)
    SystemTexts[E_Language.Hindi] = DictLangHindi

with open("SystemLang4.json", encoding="utf8") as _FarsiResource:
    DictLangFarsi = json.load(_FarsiResource)
    SystemTexts[E_Language.Farsi] = DictLangFarsi

with open("SystemLang5.json", encoding="utf8") as _ArabiResource:
    DictLangArabi = json.load(_ArabiResource)
    SystemTexts[E_Language.Arabic] = DictLangArabi

LanguageManager(SystemTexts)

print("Client connected.")
botClient.run()