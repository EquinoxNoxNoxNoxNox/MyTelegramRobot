import time
from .M_Coupon import M_Coupon , E_SystemTypes
InitializedScore = 5
class M_User():
    """
    دیتا مدل کاربر های سیستم
    """
    def __init__(self,Uid:"int یوزر آیدی تلگرام",PhoneNumber:"str شماره تماس کاربر"="",JoinDate:"timestamp"=None,_id:"int شناسه دیتابیس" = 0,Coupons=[]):
        self.Uid : int = Uid
        self.PhoneNumber : str =PhoneNumber
        self.JoinDate : "timestamp/datetime"= JoinDate or time.strftime('%Y-%m-%d %H:%M:%S')
        self.Id : int = _id
        self.Coupons : [M_Coupon] = Coupons or [
            M_Coupon(self.Id,E_SystemTypes.E_Coupon.BookCp,InitializedScore),
            M_Coupon(self.Id,E_SystemTypes.E_Coupon.GameCp,InitializedScore),
            M_Coupon(self.Id,E_SystemTypes.E_Coupon.PackageCP,InitializedScore),
            M_Coupon(self.Id,E_SystemTypes.E_Coupon.SongCp,InitializedScore)
        ]