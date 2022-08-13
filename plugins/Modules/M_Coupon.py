from .E_SystemTypes import E_SystemTypes
class M_Coupon():
    """
    دیتا مدل بیلیط های سیستم
    """
    def __init__(self,UserId:"int شناسه کاربر درون سیتسم",SystemType:"E_SystemTypes.E_Coupon",ammount : "مقدار این کوپن" = 7,_id:"int شناسه دیتابیس" = 0):
        self.UserId : int = UserId # شناسه کاربر
        self.Id : int = _id # شناسه بیلیط
        self.SystemType : E_SystemTypes.E_Coupon = E_SystemTypes.E_Coupon(SystemType) if type(SystemType) == int else SystemType #نوع بیلیط
        self.Ammount : int = ammount