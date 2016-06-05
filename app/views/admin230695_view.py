# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Book, Alumni, AlumniToadd
from random import randint
mod = Blueprint(
    'admin230695', __name__, url_prefix='/admin230695/'
)

from wtforms import Form, BooleanField, TextField, PasswordField, validators

"""class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


@mod.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        user.save()
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin230695/register.html', form=form)
"""

@mod.route('/')
def index():
    return render_template('admin230695/index.html')

@mod.route('addbooks')
def add():
    for i in range(1,200):
        bookname = "book"+str(i)
        bookauthor = "author"+str(i/2)
        subject = "subject"+str(i/5)
        isbn = "isbnnumber"+str(i)
        numberavailable = randint(0,5)
        book = Book(bookname=bookname, author=bookauthor, subject=subject, isbn=isbn, numberavailable=numberavailable)
        book.save()
    return render_template('admin230695/index.html')

@mod.route('library')
def booksadmin():
    books = Book.query.all()
    return render_template('admin230695/library.html', books=books)

class BookForm(Form):
    bookname = TextField('Book Name', [validators.Length(min=1, max=100)])
    author = TextField('Author', [validators.Length(min=1, max=100)])
    subject = TextField('Subject', [validators.Length(min=1, max=100)])
    isbn = TextField('ISBN', [validators.Length(min=0, max=100)])
    numberavailable = TextField('Number of copies available')#, [validators.Length(min=6, max=100)])
    #password = PasswordField('New Password', [
    #    validators.Required(),
    #    validators.EqualTo('confirm', message='Passwords must match')
    #])
    #confirm = PasswordField('Repeat Password')
    #accept_tos = BooleanField('I accept the TOS', [validators.Required()])

@mod.route('addbook', methods=['GET', 'POST'])
def addbook():
    form = BookForm(request.form)
    if request.method == 'POST' and form.validate():
        book = Book(form.bookname.data, form.author.data, form.subject.data, form.isbn.data,
                    form.numberavailable.data)
        book.save()
        #db_session.add(user)
        flash('Book Added')
        return redirect('/admin230695/library')
    return render_template('admin230695/addbook.html', form=form)

@mod.route('editbook/<string:book_id>', methods=['GET', 'POST'])
def editbook(book_id):
    book1 = Book.query.filter_by(id = int(book_id)).one()
    #book = Book.query.get(self.id).one()
    book1.delete()
    #return render_template('admin230695/library.html', books=books)
    return redirect('/admin230695/library')

@mod.route('deletebook/<string:book_id>', methods=['GET', 'POST'])
def deletebook(book_id):
    book1 = Book.query.filter_by(id = int(book_id)).one()
    book1.delete()
    #return render_template('admin230695/library.html', books=books)
    return redirect('/admin230695/library')

"""class AlumForm(Form):
    alumname = TextField('Alum Name', [validators.Length(min=1, max=100)])
    alumsurname = TextField('Alum Surname', [validators.Length(min=1, max=100)])
    graduationyear = TextField('Graduation Year', [validators.Length(min=4, max=4)])

@mod.route('addalum', methods=['GET', 'POST'])
def addalum():
    form = AlumForm(request.form)
    if request.method == 'POST' and form.validate():
        alum = Alumni(form.name.data, form.surname.data, form.graduationyear.data)
        alum.save()
        #db_session.add(user)
        flash('Alum Added')
        return redirect('/admin230695/people/alumni')
    return render_template('admin230695/addalumni.html', form=form)"""

"""@mod.route('editalum/<string:alum_id>', methods=['GET', 'POST'])
def editalum(alum_id):
    alum = Alumni.query.filter_by(id = int(alum_id)).one()
    #book = Book.query.get(self.id).one()
    alum.delete()
    #return render_template('admin230695/library.html', books=books)
    return redirect('/admin230695/people/alumni')"""

@mod.route('deletealum/<string:alum_id>', methods=['GET', 'POST'])
def deletealum(alum_id):
    alum = Alum.query.filter_by(id = int(alum_id)).one()
    alum.delete()
    #return render_template('admin230695/library.html', books=books)
    return redirect('/admin230695/people/alumni')

@mod.route('addalum/<string:alum_id>', methods=['GET', 'POST'])
def addalum(alum_id):
    alumtoadd = AlumniToadd.query.filter_by(id = int(alum_id)).one()
    alum = Alumni(name=alumtoadd.name, surname=alumtoadd.surname, advisor = alumtoadd.advisor, email = alumtoadd.email, imageUrl = alumtoadd.imageUrl,
    currentOrganisation=alumtoadd.currentOrganisation, phone=alumtoadd.phone, program=alumtoadd.program, webAddress=alumtoadd.webAddress, graduationyear=alumtoadd.graduationyear)
    #return render_template('admin230695/library.html', books=books)
    alum.save()
    alumtoadd.delete()
    return redirect('/admin230695/alumnipendinglist')

@mod.route('addalumni')
def addalumni():
    for i in range(1,100):
        name = "alumni"+str(i)
        surname = "author"+str(i/2)
        graduationyear = "2014"
        alumni = Alumni(name=name, surname=surname, graduationyear=graduationyear)
        alumni.save()
    return render_template('admin230695/people/alumni.html')


"""@mod.route('equipments/equipment1')
def equipment1():
    return render_template('admin230695/equipments/equipment1.html')

@mod.route('equipments/equipment2')
def equipment2():
    return render_template('admin230695/equipments/equipment2.html')"""

@mod.route('faculty')
def faculty():
    return render_template('admin230695/people/faculty.html')

@mod.route('staff')
def staff():
    return render_template('admin230695/people/staff.html')

@mod.route('alumni')
def alumni():
    alumni = Alumni.query.all()
    return render_template('admin230695/people/alumni.html', alumni=alumni)

@mod.route('submit-profile')
def submit_profile():
    return render_template('admin230695/people/submit-profile.html')

@mod.route('departmental-assignments')
def departmental_assignments():
    return render_template('admin230695/people/departmental-assignments.html')

@mod.route('visitors')
def visitors():
    return render_template('admin230695/people/visitors.html')

@mod.route('students')
def students():
    return render_template('admin230695/people/students.html')

@mod.route('academics')
def academics():
    return render_template('admin230695/academics.html')

@mod.route('research')
def research():
    return render_template('admin230695/research.html')

@mod.route('research/solid-mechanics')
def research_solid_mechanics():
    return render_template('admin230695/research/solid-mechanics.html')

@mod.route('research/fluid-mechanics')
def research_fluid_mechanics():
    return render_template('admin230695/research/fluid-mechanics.html')

@mod.route('research/design-engineering')
def research_design_engineering():
    return render_template('admin230695/research/design-engineering.html')

@mod.route('research/honours-and-awards')
def research_honours_and_awards():
    return render_template('admin230695/research/honours-and-awards.html')

@mod.route('research/applied-mechanics')
def research_applied_mechanics():
    return render_template('admin230695/research/applied-mechanics.html')

@mod.route('equipments')
def equipments():
    return render_template('admin230695/equipments.html')

@mod.route('requestequipments')
def requestequipments():
    return render_template('admin230695/requestequipments.html')

@mod.route('equipment1')
def equipment1():
    return render_template('admin230695/equipments/equipment1.html')

@mod.route('equipment2')
def equipment2():
    return render_template('admin230695/equipments/equipment2.html')

@mod.route('publications/solid-mechanics')
def publications_solid_mechanics():
    return render_template('admin230695/publications/solid-mechanics.html')

@mod.route('publications/fluid-mechanics')
def publications_fluid_mechanics():
    return render_template('admin230695/publications/fluid-mechanics.html')

@mod.route('publications/applied-mechanics')
def publications_applied_mechanics():
    return render_template('admin230695/publications/applied-mechanics.html')

@mod.route('facilities')
def facilities():
    return render_template('admin230695/facilities.html')

@mod.route('placement')
def placement():
    return render_template('admin230695/placement.html')

@mod.route('about-us')
def about_us():
    return render_template('admin230695/about-us.html')

@mod.route('contacts')
def contacts():
    return render_template('admin230695/contacts.html')

@mod.route('apply')
def apply():
    return render_template('admin230695/apply.html')

@mod.route('campus-life')
def campus_life():
    return render_template('admin230695/campus-life.html')

@mod.route('alumnipendinglist')
def alumnipendinglist():
    alumnipendinglist = AlumniToadd.query.all()
    return render_template('admin230695/alumnipendinglist.html', alumnipendinglist = alumnipendinglist)
