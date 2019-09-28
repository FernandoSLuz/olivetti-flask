from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tbl_phones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    name = db.Column(db.String(80))
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

def SelectAllPhones():
    data_phones = tbl_phones.query.all()
    phonesList = ""
    for num, item in enumerate(data_phones, start=0):
        phonesList += "\\n Phone: " + str(item.phone) + " ---- Name " + str(item.name)
    return(phonesList)