import time
from .E_Status import E_Status
from .E_Language import E_Language

class M_Session():
    """مدل دیتا جلسه کاربر"""
    def __init__(self):
        self.IsBan : bool = False #فلگ بن بودن یا نبودن کاربر
        self.BanTime : "tiemstamp" = time.time() #تایم بن کاربر
        self.BanReason : str = "NO REASON" #دلیل بن شدن کاربر
        self.Status : E_Status = E_Status.Non
        self.User : "M_User" = None # یوزر سیستم
        self.Captcha : "M_Captcha" = None #کپچا حل شده
        self.TimeLastMessage : "tiemstamp" = time.time() # آخرین مسیج فرستاده شده
        self.SpamWarns : "int" = 0 # تعداد اخطار های اسپم
        self.Language : E_Language = E_Language.English # زبان سیستم برای این نشست بطور پیشفرض انگلیسی است
    
    #بن کردن این نشست
    def Ban(self):
        self.IsBan = True