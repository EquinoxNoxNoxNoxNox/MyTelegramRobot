class Base(Exception):
    """پایه ارور ها"""
    ...
class NoSession(Base):
    """
    نشست وجود ندارد
    """
    ...
class UnsolvedCaptcha(Base):
    """
    کپچا حل نشده است
    """
    ...
class UserNotFound(Base):
    """
    یوزر پیدا نشد
    """
    ...
    