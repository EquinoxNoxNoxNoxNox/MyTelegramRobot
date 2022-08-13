from enum import Enum

class E_SystemTypes():
    class E_FileUpload(Enum):
        #Region Products
        PackagePhoto = 1
        PackageFile = 2
        SongPhoto = 3
        SongFile = 4
    class E_Coupon(Enum):
        #Region CouponTypes
        PackageCP = 5
        SongCp = 6
        GameCp = 7
        BookCp = 8
    class E_MimeType(Enum):
        #Region MimeTypes
        Audio = 9
        Document = 10
        Video = 11
        Photo = 12