from .E_SystemTypes import E_SystemTypes
import emoji
import random

Emojies = ['😁','😆','😅','🙃','🥰','🤑','🥵','🥶','😈','💀','💩','🤡','👻','👽','👾','🤖','😻','😼','🙉','💋','💌','💕','💯','💢','💥','💫','💦','💨','🖖','👌','🤟','🤘','🤙','🖕','🧠','🦷','🦴','👀','👶','👦','👧','👨‍💻','🐒','🦍','🦧','🐶','🦁','🐣','🐤','🦚','🦜','🐸','🦈','🐙','🦋','🐛','🐝','🕸','🌷','🌵','🍇','🍉','🍌','🌽','🥒','🥬','🥦','🧄','🧅','🍄','🥜','⚓','🌓','🌞','🪐','🌌','🧨','✨','🎈','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓','⛎']

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
    دیتا مدل کپچا های سیستم
    """
    def __init__(self):
        self.Options = [] # گزینه های موجود
        _seq = random.choice(range(1,5))
        for i in range(5):
            self.Options.append(random.choice(Emojies))
        self.Value = _seq # گزینه صحیح کپچا
        self.IsSolved = False # آیا کپچا حل شده
        self.IsSent: bool = False # آیا فرستاده شده
        