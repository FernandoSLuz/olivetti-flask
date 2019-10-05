from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tbl_phones(db.Model):
    id = db.Column(db.Integer(11), primary_key=True)
    phone = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    isInAConversation = db.Column(db.Boolean(80))
    conversationId = db.Column(db.Integer(11))  
    def __init__(self, phone, name, email, isInAConversation, conversationId):
        self.phone = phone
        self.name = name
        self.email = email
        self.isInAConversation = isInAConversation
        self.conversationId = conversationId

def SelectAllPhones():
    data_phones = tbl_phones.query.all()
    phonesList = ""
    for num, item in enumerate(data_phones, start=0):
        phonesList += "\\n Phone: " + str(item.phone) + " ---- Name " + str(item.name)
    return(phonesList)