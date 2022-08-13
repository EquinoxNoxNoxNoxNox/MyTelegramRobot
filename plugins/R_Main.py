from pyrogram import Client , filters
from pyrogram.types import InputMediaPhoto, InputMediaVideo , ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from .CustomFilter import CustomFilter , dynamic_data_filter
from .UserButtons import UserButtons , ButtonValue
from .LanguageManager import LanguageManager
from .Modules.E_Status import E_Status
from .Modules.E_Language import E_Language

def GetMainMenu(client,uid):
    Session = CustomFilter.GetSession(uid)
    TextToSend = LanguageManager.GetText(Session.Language, "Text_UserStart")
    _Buttons = UserButtons.MainMenu
    client.send_message(
        chat_id=uid, 
        text=TextToSend,
        reply_markup=ReplyKeyboardMarkup([
            [KeyboardButton(text=_Buttons.Packages.Name)],
            [KeyboardButton(text=_Buttons.SongsAndArtistAlbums.Name)],
            [KeyboardButton(text=_Buttons.Books.Name)],
            [KeyboardButton(text=_Buttons.Codes.Name)],
            [KeyboardButton(text=_Buttons.VideoGames.Name)],
            [KeyboardButton(text=_Buttons.Language.Name)]
            ])
    )

@Client.on_message(filters.command("start") & CustomFilter(E_Status.Non))
def messageStartUser(client,message):
    uid = message.from_user.id
    GetMainMenu(client,uid)

@Client.on_callback_query(filters.regex(r"^solvecp-\d*$"))
def callbackUserSolveCaptcha(client,CB_Query):
    uid = CB_Query.from_user.id
    _Session = CustomFilter.GetSession(uid)
    ChosenNum = int(CB_Query.data.split("-")[1])
    if(ChosenNum == _Session.Captcha.Value):
        _Session.Captcha.IsSolved=True
        CustomFilter.SetSession(_Session)
        TextToSend = """WELCOME✅""" 
        client.answer_callback_query(
            CB_Query.id,
            text=TextToSend
        )
        CB_Query.message.delete()
        GetMainMenu(client,uid)
    else:
        client.answer_callback_query(
            CB_Query.id,
            text="Wrong❌"
        )

@Client.on_message(dynamic_data_filter(UserButtons.MainMenu.Language.Name) & CustomFilter(E_Status.Free))
def messageUserChangeMenuLanguage(client,message):
    uid = message.from_user.id
    mid = message.message_id
    Session = CustomFilter.GetSession(uid)
    TextToSend = LanguageManager.GetText(Session.Language, "Text_LanguageSelect")
    _Buttons = UserButtons.LanguageMenu
    client.send_message(
        chat_id = uid,
        text = TextToSend,
        reply_markup=ReplyKeyboardMarkup([
            [KeyboardButton(text=_Buttons.English.Name)],
            [KeyboardButton(text=_Buttons.Russian.Name)],
            [KeyboardButton(text=_Buttons.Hindi.Name)],
            [KeyboardButton(text=_Buttons.Farsi.Name)],
            [KeyboardButton(text=_Buttons.Arabic.Name)]])
    )

@Client.on_message(filters.regex(".+🗯") & CustomFilter(E_Status.Free))
def messageUserChangeLanguage(client,message):
    uid = message.from_user.id
    mid = message.message_id
    Session = CustomFilter.GetSession(uid)
    for k,v in vars(UserButtons.LanguageMenu).items():
        if type(v) == ButtonValue:
            if(v.Name == message.text):
                Session.Language = E_Language(v.Value)
                CustomFilter.UpdateSession(Session)
                GetMainMenu(client, uid)