user_name='user123'
pass_word=123456
attempt=3
while attempt>0:
        username=input("enter the username to login")
        password=input("enter the password to login")
        if username==user_name and password==pass_word:
                print("login succesful")
        else:
            attempt-=1
            print("incorrect password")
if attempt==0:
    print(" to many attempt login failed")
