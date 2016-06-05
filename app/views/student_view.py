# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Book, Alumni, AlumniToadd
from random import randint

mod = Blueprint(
    'student', __name__, url_prefix='/'
)

from wtforms import Form, BooleanField, TextField, PasswordField, validators

@mod.route('/')
def index():
    return render_template('student/index.html')

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
    return render_template('student/index.html')

@mod.route('removebooks')
def removebooks():
    books = Book.query.all()
    for book in books:
        book.delete()
    return render_template('student/index.html')

@mod.route('removealumni')
def removealumni():
    alumni = Alumni.query.all()
    for alum in alumni:
        alum.delete()
    return render_template('student/index.html')

@mod.route('addalumni')
def addalumni():
    for i in range(1,100):
        name = "alumni"+str(i)
        surname = "surname"+str(i/2)
        advisor = "advisor"+str(i/5)
        email = "email"+str(i)
        currentOrganisation = "organisation"+str(randint(1,100))
        phone = "phone"+str(i)
        program = "program"+str(randint(1,5))
        webAddress = "webAddress"+str(i)
        graduationyear = str(randint(2010,2015))
        alumni = Alumni(name=name, surname=surname, advisor=advisor, email=email, currentOrganisation=currentOrganisation, phone=phone, program=program, webAddress=webAddress, graduationyear=graduationyear)
        alumni.save()
    return render_template('student/people/alumni.html')

@mod.route('library')
def books():
    books = Book.query.all()
    return render_template('student/library.html', books=books)

#@mod.route('equipments/equipment1')
#def equipment1():
#    return render_template('student/equipments/equipment1.html')

#@mod.route('equipments/equipment2')
#def equipment2():
#    return render_template('student/equipments/equipment2.html')

@mod.route('faculty')
def faculty():
    return render_template('student/people/faculty.html')

@mod.route('staff')
def staff():
    return render_template('student/people/staff.html')

@mod.route('alumni')
def alumni():
    alumni = Alumni.query.all()
    return render_template('student/people/alumni.html', alumni=alumni)

class AlumniForm(Form):
    name = TextField('Your Name', [validators.Length(min=1, max=100)])
    surname = TextField('Surname', [validators.Length(min=1, max=100)])
    advisor = TextField('Advisor', [validators.Length(min=1, max=100)])
    email = TextField('Email', [validators.Length(min=0, max=100)])
    currentOrganisation = TextField('Current Organisation', [validators.Length(min=0, max=100)])
    phone = TextField('Phone', [validators.Length(min=0, max=100)])
    program = TextField('Program', [validators.Length(min=0, max=100)])
    webAddress = TextField('Web Address', [validators.Length(min=0, max=100)])
    graduationyear = TextField('Graduation Year', [validators.Length(min=0, max=100)])

@mod.route('submit-profile', methods=['GET', 'POST'])
def submit_profile():
    form = AlumniForm(request.form)
    if request.method == 'POST' and form.validate():
        alumnitoadd = AlumniToadd(form.name.data, form.surname.data, form.advisor.data, form.email.data,
                    "na", form.currentOrganisation.data, form.phone.data, form.program.data,
                    form.webAddress.data, form.graduationyear.data)
        alumnitoadd.save()
        #db_session.add(user)
        #flash('Profile Submitted')
        return redirect('/')
    return render_template('student/people/submit-profile.html', form=form)

@mod.route('departmental-assignments')
def departmental_assignments():
    return render_template('student/people/departmental-assignments.html')

@mod.route('visitors')
def visitors():
    return render_template('student/people/visitors.html')

@mod.route('students')
def students():
    return render_template('student/people/students.html')

@mod.route('academics')
def academics():
    return render_template('student/academics.html')

@mod.route('research')
def research():
    return render_template('student/research.html')

@mod.route('research/solid-mechanics')
def research_solid_mechanics():
    return render_template('student/research/solid-mechanics.html')

@mod.route('research/fluid-mechanics')
def research_fluid_mechanics():
    return render_template('student/research/fluid-mechanics.html')

@mod.route('research/design-engineering')
def research_design_engineering():
    return render_template('student/research/design-engineering.html')

@mod.route('equipment1')
def equipment1():
    return render_template('student/equipments/equipment1.html')

@mod.route('equipment2')
def equipment2():
    return render_template('student/equipments/equipment2.html')

@mod.route('research/honours-and-awards')
def research_honours_and_awards():
    return render_template('student/research/honours-and-awards.html')

@mod.route('research/applied-mechanics')
def research_applied_mechanics():
    return render_template('student/research/applied-mechanics.html')

@mod.route('equipments')
def equipments():
    return render_template('student/equipments.html')

@mod.route('requestequipment')
def requestequipments():
    return render_template('student/requestequipment.html')

@mod.route('publications/solid-mechanics')
def publications_solid_mechanics():
    return render_template('student/publications/solid-mechanics.html')

@mod.route('publications/fluid-mechanics')
def publications_fluid_mechanics():
    return render_template('student/publications/fluid-mechanics.html')

@mod.route('publications/applied-mechanics')
def publications_applied_mechanics():
    return render_template('student/publications/applied-mechanics.html')

@mod.route('facilities')
def facilities():
    return render_template('student/facilities.html')

@mod.route('placement')
def placement():
    return render_template('student/placement.html')

@mod.route('about-us')
def about_us():
    return render_template('student/about-us.html')

@mod.route('contacts')
def contacts():
    return render_template('student/contacts.html')

@mod.route('apply')
def apply():
    return render_template('student/apply.html')

@mod.route('campus-life')
def campus_life():
    return render_template('student/campus-life.html')
