import pyrebase as pb

firebaseConfig = {
    "apiKey": "your api key",
    "authDomain": "your domain",
    "databaseURL": "link to your realtime database",
    "projectId": "your project id",
    "storageBucket": "storage bucket but wtv",
    "messagingSenderId": "ur message sender id but wtv",
    "appId": "ur app id"
}

firebase = pb.initialize_app(firebaseConfig)
# email: firebase@gmail.com
# pass: Firebase123
auth = firebase.auth()
db = firebase.database()
def login():
    try:
        email = input("enter email:")
        password = input("enter password:")
        auth.sign_in_with_email_and_password(email,password)
        print("HHHA")
    except:
        print("Invalid email and/or password!")

def register():
    new_email = input("enter email:")
    new_pass = input("enter password:")
    cfm_new_pass = input("cfm password:")
    if(new_pass == cfm_new_pass):
        try:
            auth.create_user_with_email_and_password(new_email,new_pass)
            print("done")
        except:
            print("Account creation failed!")


def createItem():
    name = input("item name:")
    cost = int(input("item cost"))
    itemAvailable = True
    
    data = {
        "name":name,
        "cost":cost,
        "itemAvailable":itemAvailable
    }
    db.child("itemList").push(data)


def updateName():
    item_id = input("item ID:")
    try:
        new_name = input("change name")
        db.child("itemList").child(item_id).update({"name":new_name})
        print("Name updated")
    except:
        print("Update unsuccesful!")

def getItems():
    items = db.child("itemList").get()
    itemDict  = {}
    for item in items.each():
        print("___________") 
        print("key:",item.key())
        print("value:",item.val())

def conditionalGetItems():
    # column = input("column name:")
    # said_value = input("what is the value in that column?")

# 
    items = db.child("itemList").order_by_child("name").equal_to("bottle").get()
    # print(len(items))
    print("for name")
    for item in items.each():
        print("___________") 
        print("key:",item.key())
        print("value:",item.val())


    items = db.child("itemList").order_by_child("cost").equal_to(12).get()
    # print(len(items))
    print("for value")
    for item in items.each():
        print("___________") 
        print("key:",item.key())
        print("value:",item.val())

# createItem()
# createItem()
getItems()
conditionalGetItems()