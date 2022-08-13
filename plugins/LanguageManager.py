from .Modules.E_Language import E_Language
class LanguageManager():
    LResource = dict()
    
    def __init__(self,LResource : dict):
        LanguageManager.LResource = LResource

    def GetText(LType:E_Language,LKey:str) -> str:
        #TODO REMOVE TRY CATCH AFTER RELEASE
        try:
            return LanguageManager.LResource[LType][LKey]
        except KeyError:
            return f"{LKey} - {LType.name}" 