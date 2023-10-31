import database as db

def college_update():
    enrollment_no=input("enter your enrollment no:")
    name=input("enter your name:")
    branch=input("enter your branch:")
    db.car.execute(f"insert into college(enrollment_no,name,branch) values('{enrollment_no}','{name}','{branch}')")
    print("your data feed successfully")