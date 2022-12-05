from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Trip_Advisor_Reviews
import sqlite3 as sql
from . import db
import json

views = Blueprint('views', __name__)
hotelNames=""

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/about')
def about():
    return render_template("about.html", user=current_user)

@views.route('/projectdescription')
def projectdescription():
    return render_template("projectdescription.html", user=current_user)

@views.route('/findhotels',methods=['GET'])
@login_required
def findhotels():
    con1 = sql.connect("instance/database.db")
    
    con1.row_factory = sql.Row
   
    cur1 = con1.cursor()
    cur1.execute("select  id,name from finalsentiment_all order by name ")
   
    hotelNames = cur1.fetchall(); 
    
    return render_template("findhotels.html", user=current_user, hotels=hotelNames)


@views.route('/explorationdata')
def explorationdata():
    return render_template("explorationdata.html", user=current_user)

@views.route('/visualization')
def visualization():
    return render_template("visualization.html", user=current_user)


@views.route('/findhotels',methods=['Post'])
def ShowRating():
    findhotels()
    postid= request.form.get('option')
    con = sql.connect("instance/database.db")
    
    con.row_factory = sql.Row
    qid =str.format("select *  from finalsentiment_all Where id={0}" , postid)
    cur = con.cursor()
    cur.execute(qid)
    cur1 = con.cursor()
    cur1.execute("select  id,name from finalsentiment_all order by name ")
   
    Ratings = cur.fetchall();    
    hotelNames = cur1.fetchall(); 


    return render_template("findhotels.html", user=current_user, hotelRatings=Ratings, hotels=hotelNames)





    # return render_template("about.html", user=current_user,pid=postid)