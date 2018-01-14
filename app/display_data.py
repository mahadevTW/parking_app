from app.sql_alchemy import User


def display():
    users = User.query.all()
    for user in users:
        print "Username: {}".format(user.username)
        print "Password: {}".format(user.password)
        print "Mobile number: {}".format(user.mobile_no)
        print "Address: {}".format(user.address)
        print "============================================"



if __name__=="__main__":
    display()