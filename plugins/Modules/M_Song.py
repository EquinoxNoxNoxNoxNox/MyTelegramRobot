from .M_Product import M_Product

class M_Song(M_Product):
    """
    دیتا مدل موزیک های سیستم
    """
    def __init__(self,Title:"عنوان",IsDeleted:"درصورت حذف بودن محصول"=False,_id:"int شناسه دیتابیس" = 0):
        super().__init__(self,Title,IsDeleted,_id)