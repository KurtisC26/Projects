from flask import Blueprint, render_template,request, flash, redirect, url_for
from .modles import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        t_name = request.form.get("team_select")
        team_abbr = t_name[0:3]
        team_name = t_name[6:]
        print(team_abbr)
        print(team_name)

        new_team = User(email = team_abbr, first_name = team_name)
        team_in_db = User.query.filter_by(email = team_abbr).first()

        if team_in_db:
            login_user(team_in_db, remember=True)
            flash('Welcome Back!', category='success')
            return redirect(url_for('views.home'))
        else: 
            # Add user to the database
            new_team = User(email = team_abbr, first_name = team_name)
            db.session.add(new_team)
            db.session.commit()
            login_user(new_team, remember=True)
            flash('First Login!', category='success')
            return redirect(url_for('views.home'))
    else: 
            flash('Please select a team to proceed', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))








# @auth.route('/sign-up', methods = ['GET','POST'])
# def signup():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         firstName = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')


#         user = User.query.filter_by(email = email).first()

#         if user:
#             flash('Email already exists', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 1 characters', category='error')
#         elif len(firstName) < 2:
#             flash('First Name must be greater than 1 characters', category='error')
#         elif password1 != password2:
#             flash('Passwords must match', category='error')
#         elif len(password1) < 7:
#             flash('Passwords must longer than 7 characters', category='error')
#         else:
#             # Add user to the database
#             new_user = User(email = email, first_name = firstName, password = generate_password_hash(password1,method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account Created!', category='success')
#             return redirect(url_for('views.home'))
        
#     return render_template("signup.html", user = current_user)




