from .E_SystemTypes import E_SystemTypes
import emoji
import random

Emojies = ['đ','đ','đ','đ','đĽ°','đ¤','đĽľ','đĽś','đ','đ','đŠ','đ¤Ą','đť','đ˝','đž','đ¤','đť','đź','đ','đ','đ','đ','đŻ','đ˘','đĽ','đŤ','đŚ','đ¨','đ','đ','đ¤','đ¤','đ¤','đ','đ§ ','đŚˇ','đŚ´','đ','đś','đŚ','đ§','đ¨âđť','đ','đŚ','đŚ§','đś','đŚ','đŁ','đ¤','đŚ','đŚ','đ¸','đŚ','đ','đŚ','đ','đ','đ¸','đˇ','đľ','đ','đ','đ','đ˝','đĽ','đĽŹ','đĽŚ','đ§','đ§','đ','đĽ','â','đ','đ','đŞ','đ','đ§¨','â¨','đ','â','â','â','â','â','â','â','â','â','â','â','â','â']

def _getRandomEmoji(res,options):
    Selected = random.choice(Emojies)
    if(Selected in res or Selected in options):
        return _getRandomEmoji(res,options)
    else:
        return Selected


def GetRandomEmojies(Options):
    res = []
    for i in range(4):
        Selected = _getRandomEmoji(res,Options)
        res.append(Selected)
    return res

class M_Captcha():
    """
    ŘŻŰŘŞŘ§ ŮŘŻŮ ÚŠŮžÚŘ§ ŮŘ§Ű ŘłŰŘłŘŞŮ
    """
    def __init__(self):
        self.Options = [] # ÚŻŘ˛ŰŮŮ ŮŘ§Ű ŮŮŘŹŮŘŻ
        _seq = random.choice(range(1,5))
        for i in range(5):
            self.Options.append(random.choice(Emojies))
        self.Value = _seq # ÚŻŘ˛ŰŮŮ ŘľŘ­ŰŘ­ ÚŠŮžÚŘ§
        self.IsSolved = False # Ř˘ŰŘ§ ÚŠŮžÚŘ§ Ř­Ů Ř´ŘŻŮ
        self.IsSent: bool = False # Ř˘ŰŘ§ ŮŘąŘłŘŞŘ§ŘŻŮ Ř´ŘŻŮ
        