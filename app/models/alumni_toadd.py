from .. import db
from . import CRUDMixin


class AlumniToadd(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    advisor = db.Column(db.String(50))
    email = db.Column(db.String(50))
    imageUrl = db.Column(db.String(50))
    currentOrganisation = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    program = db.Column(db.String(50))
    webAddress = db.Column(db.String(50))
    graduationyear = db.Column(db.String(4))

    def __init__(self, name, surname, advisor, email, imageUrl, currentOrganisation, phone, program, webAddress, graduationyear):
        self.surname = surname
        self.name = name
        self.email = email
        self.advisor = advisor
        self.imageUrl = imageUrl
        self.currentOrganisation = currentOrganisation
        self.phone = phone
        self.program = program
        self.webAddress = webAddress
        self.graduationyear = graduationyear
