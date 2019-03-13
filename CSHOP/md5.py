import hashlib

 #自定义加密方法
def encryption(pwd):
    md=hashlib.md5()
    md.update(pwd.encode('utf-8'))
    md5_pwd=md.hexdigest()
    return md5_pwd