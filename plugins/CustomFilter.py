from pyrogram import filters
from pyrogram.types import InputMediaPhoto, InputMediaVideo , ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

from .Modules.E_Status import E_Status
from .Modules.M_Session import M_Session
from .Modules import B_User
from .Modules.M_Captcha import M_Captcha , GetRandomEmojies
from .Modules.M_User import M_User
from .Modules import Errors
from .LanguageManager import LanguageManager
from PIL import Image, ImageDraw, ImageFont
import random
#from .Models import M_error as errors

def dynamic_data_filter(data):
    async def func(flt, _, message):
        return flt.data == message.text
    return filters.create(func, data=data)

class CustomFilter():
    """
    A general CALLBACK FILTER
    """
    Sessions : [M_Session] = [] #نشست های موجود در سیستم
    Status : E_Status = E_Status.Non #استاتوس فیلتر
    
    def CaptchaImageCreator(param:M_Captcha)->bool:
        R,G,B = (172, 41, 131)
        im = Image.new("RGB", (870, 300), (R,G,B))
        draw = ImageDraw.Draw(im)
        unicode_font = ImageFont.truetype(r"E:\AppleColorEmoji.ttf", 137)
        for Text in param.Options:
            draw.text((15 + (param.Options.index(Text) * 170), int(random.choice(range(171)))), Text, font=unicode_font, embedded_color=True)
        im.save("output.jpg", format="JPEG", optimize=True, quality=15)
        return True
    
    def UpdateSession(param:M_Session) -> None:
        for _sesh in CustomFilter.Sessions:
            if(_sesh.User.Uid == param.User.Uid):
                CustomFilter.Sessions[CustomFilter.Sessions.index(_sesh)] = param
                
    def SetSession(param:M_Session)->None:
        CustomFilter.Sessions.append(param)
    
    def GetSession(uid) -> M_Session:
        for sesh in CustomFilter.Sessions:
            if(int(sesh.User.Uid) == int(uid)):
                return sesh
        raise Errors.NoSession()

    def __init__(self,Status:E_Status):
        self.Status = Status

    async def __call__(self, client, message: "Message") -> bool:
        Uid = message.from_user.id
        print("check attempt")
        try:
            _Session = CustomFilter.GetSession(Uid)
            if not _Session.Captcha.IsSolved:
                raise Errors.UnsolvedCaptcha
        except Errors.NoSession:
            _Session = M_Session()
            _Session.Captcha = M_Captcha()
            _Session.Captcha.IsSent = True
            try:
                _Session.User = B_User.GetByUid(Uid)
            except Errors.UserNotFound:
                _Session.User = B_User.SetUser(M_User(Uid))
            CustomFilter.SetSession(_Session)
            IsImageSaved = CustomFilter.CaptchaImageCreator(_Session.Captcha)
            CaptchaButtons = []
            for RandomEmoji in GetRandomEmojies(_Session.Captcha.Options):
                CaptchaButtons.append(
                    InlineKeyboardButton(
                        RandomEmoji,
                        callback_data=f"solvecp-{0}"
                    )
                )
            CaptchaButtons.insert(random.choice(range(4)),
                InlineKeyboardButton(
                    _Session.Captcha.Options[_Session.Captcha.Value],
                    callback_data=f"solvecp-{_Session.Captcha.Value}"
                )
            )
            _textToSend = LanguageManager.GetText(_Session.Language, "Text_CaptchaEmojiUserStart")
            await client.send_photo(
                chat_id = Uid,
                photo = "output.jpg",
                caption = _textToSend,
                reply_markup = InlineKeyboardMarkup(
                    [CaptchaButtons]
                )
            )
            return False
        except Errors.UnsolvedCaptcha:
            return False
        if(_Session.Status.value == self.Status.value or E_Status.Free.value == self.Status.value):
            return True
        print("not true")