class M_Product():
    """
    ابسترکت مدل محصولات
    """
    def __init__(self,Title:"عنوان",IsDeleted:"درصورت حذف بودن محصول"=False,_id:"int شناسه دیتابیس" = 0):
        self.Id = _id
        self.Title = Title
        self.IsDeleted = IsDeleted
    
    def Delete(self):
        """
        حذف منطقی آیتم
        """
        self.IsDeleted = True

if __name__ == "__main__":
    print(help(M_Prouct))