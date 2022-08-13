from .M_Product import M_Product

class M_VideGame(M_Product):
    """
    دیتا مدل ویدئو گیم های سیستم
    """
    def __init__(self,Title:"عنوان",Links:"str لینک دانلود بازی",IsDeleted:"درصورت حذف بودن محصول"=False,_id:"int شناسه دیتابیس" = 0):
        self.Links = Links
        super().__init__(self,Title,IsDeleted,_id)