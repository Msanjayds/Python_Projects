import datetime
def Calculateage(y,m,d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days / 365.25)
    print(age)

Calculateage(1981,5,8)
    
