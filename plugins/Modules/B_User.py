from .M_User import M_User
from .DataAccess import Cursor,Database
from . import Errors

#get user by it's UID
def GetByUid(uid:int)->M_User:
    sql = """SELECT Id, Uid, PhoneNumber, JoinDate from users WHERE Uid=%s"""
    try:
        Cursor.execute(sql,(uid))
    except:
        raise Errors.UserNotFound("")
    _User = Cursor.fetchone()
    result = M_User(_User[1],_User[2],_User[3],_User[0])
    sqlCp = """SELECT Id, UserId, SystemType, _Ammount from coupons WHERE UserId=%s"""
    Cursor.execute(sqlCp,(result.Id))
    for Cp in Cursor.fetchall():
        result.Coupons.append(M_User.M_Coupon(Cp[1],Cp[2],Cp[3],Cp[0]))
    return result

#Update user
def UpdateUser(param:M_User)->None:
    sql = """UPDATE users SET Uid=%s, PhoneNumber=%s WHERE Id=%s"""
    sqlCp = "UPDATE coupons SET _Ammount=%s WHERE UserId=%s AND SystemType=%s"
    Cursor.execute(sql,(param.Uid,
        param.PhoneNumber,
        param.Id))
    Database.commit()
    ResultCoupons = []
    for Cp in param.Coupons:
        ResultCoupons.append((
            Cp.Ammount,
            param.Id,
            Cp.SystemType.value
        ))
    Cursor.executemany(sqlCp,ResultCoupons)
    Database.commit()

#Set user
def SetUser(param:M_User)->M_User:
    sql = """INSERT INTO users (Uid, PhoneNumber, JoinDate) VALUES (%s, %s,%s)"""
    Cursor.execute(sql,(
        param.Uid
        ,param.PhoneNumber
        ,param.JoinDate)
    )
    param.Id = Cursor.lastrowid
    Database.commit()
    sqlCp = "INSERT INTO coupons (UserId,SystemType,_Ammount) VALUES (%s,%s,%s)"
    CpToBeRecorded = []
    for Cp in param.Coupons:
        CpToBeRecorded.append(
            (
                param.Id
                ,Cp.SystemType.value
                ,Cp.Ammount
            )
        )
    Cursor.executemany(sqlCp,CpToBeRecorded)
    Database.commit()
    return param