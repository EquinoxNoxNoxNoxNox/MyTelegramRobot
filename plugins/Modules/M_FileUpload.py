from .E_SystemTypes import E_SystemTypes
class M_FileUpload():
    """
    دیتا مدل فایل های آپلود شده سیستم
    """
    def __init__(self,FileId:"str فایل های آ",GenId:"int شناسه",SystemType:"E_FileUpload تایپ",_id:"int شناسه دیتابیس" = 0):
        self.Id = _id
        self.FileId = FileId
        self.GenId = GenId
        if(type(SystemType)==int):
            self.SystemType = E_SystemTypes.E_FileUpload(SystemType)
        else:
            self.SystemType = SystemType