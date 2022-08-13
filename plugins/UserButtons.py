from .Modules.E_Language import E_Language

class ButtonValue:
    """
    مقدار درون هر دکمه
    """
    def __init__(self,Name,Value):
        self.Name : str = Name
        self.Value : "dynamic" = Value
class UserButtons:
    """
    بخش های رابط کاربری تلگرام
    """
    class MainMenu:
        #پکیج ها
        Packages : ButtonValue = ButtonValue("📚Packages🎬", 0)
        #آهنگ ها و آلبوم های آرتیست
        SongsAndArtistAlbums : ButtonValue = ButtonValue("🌜🎧Songs and artist albums🧘‍♀️🌛", 0)
        #کتاب ها
        Books : ButtonValue = ButtonValue("📚Books📖", 0)
        #کد ها
        Codes : ButtonValue = ButtonValue("🧑🏻‍💻Codes⌨️", 0)
        #ویدئو گِیم ها
        VideoGames : ButtonValue = ButtonValue("🎮Video games♥️", 0)
        #تظیم زبان ربات
        Language : ButtonValue = ButtonValue("🇬🇧🇷🇺Language⚙️Setting🇮🇳🇸🇦🇮🇷", 0)
    
    class LanguageMenu:
        """
        منوی تعویض زبان
        """
        English = ButtonValue("🇬🇧English🇬🇧🗯", E_Language.English.value)
        Russian = ButtonValue("🇷🇺русский🇷🇺🗯", E_Language.Russian.value)
        Hindi = ButtonValue("🇮🇳हिन्दी🇮🇳🗯", E_Language.Hindi.value)
        Farsi = ButtonValue("🇮🇷فارسی🇮🇷🗯", E_Language.Farsi.value)
        Arabic = ButtonValue("🇦🇪عربی🇦🇪🗯", E_Language.Arabic.value)