import re


######################################################################
# entery claim: email: mail
#
# exit claim:   bool. Valid Email?
######################################################################
def check_email(email):
    if re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
        return True
    else:
        return False


######################################################################
# entery claim: user_name: user_name
#
# exit claim:   bool. Valid user name?
######################################################################
def check_user_name(user_name):
    if re.match("^[a-zA-Z0-9_.-]+$", user_name):
        return True
    else:
        return False


######################################################################
# entery claim: user_name: user_name
#
# exit claim:   bool. Valid user name?
######################################################################
def check_password(password):
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        str = input("pls enter password")
        print(check_password(str))
