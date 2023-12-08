from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user



#My db connection
local_server=True
app = Flask(__name__)
app.secret_key='abhinandan'

#this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/database_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/criminal_database'
db=SQLAlchemy(app)

#here we will create db models that is tables

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))

class Police(db.Model):
    email=db.Column(db.String(50))
    pol_id=db.Column(db.Integer,primary_key=True)
    pol_name=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    pol_dob=db.Column(db.String(50))
    designation=db.Column(db.String(50))
    pol_phno=db.Column(db.Integer)
    pol_addr=db.Column(db.String(50))
    stat_id=db.Column(db.Integer)

class Station(db.Model):
    stat_id=db.Column(db.Integer,primary_key=True)	
    stat_name=db.Column(db.String(50))
    stat_phno=db.Column(db.Integer)
    stat_city=db.Column(db.String(50))

class Fir(db.Model):
    fir_id=db.Column(db.Integer,primary_key=True)
    fir_date=db.Column(db.String(50))
    stat_id=db.Column(db.Integer)
    vict_name=db.Column(db.String(50))
    fir_desc=db.Column(db.Text)


class Criminal(db.Model):
    crmnl_id=db.Column(db.Integer,primary_key=True)
    crmnl_name=db.Column(db.String(50))
    crmnl_gender=db.Column(db.String(50))
    crm_date=db.Column(db.String(50))
    crm_type=db.Column(db.String(50))
    crmnl_phno=db.Column(db.Integer)
    crmnl_addr=db.Column(db.String(50))
    fir_id=db.Column(db.Integer)


#connections

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')


    return render_template('login.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        
        encpassword=generate_password_hash(password)
        # new_user=db.engine.execute(f"INSERT INTO 'user' ('username','email','password') VALUES ('{username}','{email}','{encpassword}')")
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Success Please Login","success")


        return render_template('/login.html')



    return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return render_template('/login.html')


@app.route('/police',methods=['POST','GET'])
@login_required
def police():
    if request.method=="POST":
        email=request.form.get('email')
        pol_id=request.form.get('police_id')
        pol_name=request.form.get('name')
        gender=request.form.get('gender')
        pol_dob=request.form.get('pol_dob')
        designation=request.form.get('desg')
        pol_phno=request.form.get('number')
        pol_addr=request.form.get('addr')
        stat_id=request.form.get('station_id')

        query=db.engine.execute(f"INSERT INTO police(email,pol_id,pol_name,gender,pol_dob,designation,pol_phno,pol_addr,stat_id)VALUES('{email}','{pol_id}','{pol_name}','{gender}','{pol_dob}','{designation}','{pol_phno}','{pol_addr}','{stat_id}')")

        # newpolice=Police(email=email,pol_id=pol_id,pol_name=pol_name,gender=gender,pol_dob=pol_dob,pol_phno=pol_phno,pol_addr=pol_addr,stat_id=stat_id)
        # db.session.add(newpolice)
        # db.session.commit()
        flash("Registered Successfully","info")
        return redirect('/station')
            
    return render_template('police.html')


@app.route('/station',methods=['POST','GET'])
@login_required
def station():
    if request.method=="POST":
        stat_id=request.form.get('stat_id')
        stat_name=request.form.get('name')
        stat_phno=request.form.get('number')
        stat_city=request.form.get('addr')

        newstation=Station(stat_id=stat_id,stat_name=stat_name,stat_phno=stat_phno,stat_city=stat_city)
        db.session.add(newstation)
        db.session.commit()
        flash("Registered Successfully","info")

    return render_template('station.html')


@app.route('/fir',methods=['POST','GET'])
@login_required
def fir():
    if request.method=="POST":
        fir_id=request.form.get('fid')
        fir_date=request.form.get('fdate')
        stat_id=request.form.get('sid')
        vict_name=request.form.get('vname')
        fir_desc=request.form.get('fdesc')

        # print(fir_id,fir_date,stat_id,vict_name,fir_desc)

        newfir=Fir(fir_id=fir_id,fir_date=fir_date,stat_id=stat_id,vict_name=vict_name,fir_desc=fir_desc)
        db.session.add(newfir)
        db.session.commit()
        flash("Submmited Successfully","info")

    return render_template('fir.html')

@app.route('/firdetails')
@login_required
def firdetails():
    # em=current_user.email
    query=db.engine.execute(f"SELECT *FROM fir")
   
    return render_template('firdetails.html',query=query)


@app.route('/crime',methods=['POST','GET'])
@login_required
def crime():
    if request.method=="POST":
        crmnl_id=request.form.get('cid')
        crmnl_name=request.form.get('name')
        crmnl_gender=request.form.get('gender')
        crm_date=request.form.get('date')
        crm_type=request.form.get('ctype')
        crmnl_phno=request.form.get('number')
        crmnl_addr=request.form.get('addr')
        fir_id=request.form.get('fid')

        query=db.engine.execute(f"INSERT INTO criminal (crmnl_id,crmnl_name,crmnl_gender,crm_date,crm_type,crmnl_phno,crmnl_addr,fir_id)VALUES('{crmnl_id}','{crmnl_name}','{crmnl_gender}','{crm_date}','{crm_type}','{crmnl_phno}','{crmnl_addr}','{fir_id}')")

        # print(crmnl_id,crmnl_name,crmnl_gender,crm_date,crm_type,crmnl_phno,crmnl_addr,fir_id)
        # newcrime=Criminal(crmnl_id=crmnl_id,crmnl_name=crmnl_name,crmnl_gender=crmnl_gender,crm_date=crm_date,crm_type=crm_type,crmnl_phno=crmnl_phno,crmnl_addr=crmnl_addr,fir_id=fir_id)
        # db.session.add(newcrime)
        # db.session.commit()
        flash("Saved Successfully","info")


    return render_template('crime.html')


@app.route('/criminaldetails')
@login_required
def criminaldetails():
    # em=current_user.email
    query=db.engine.execute(f"SELECT *FROM criminal")
   
    return render_template('criminaldetails.html',query=query)

@app.route('/edit/<string:crmnl_id>',methods=['POST','GET'])
@login_required
def edit(crmnl_id):
    posts=Criminal.query.filter_by(crmnl_id=crmnl_id).first()
    if request.method=="POST":

        crmnl_id=request.form.get('cid')
        crmnl_name=request.form.get('name')
        crmnl_gender=request.form.get('gender')
        crm_date=request.form.get('date')
        crm_type=request.form.get('ctype')
        crmnl_phno=request.form.get('number')
        crmnl_addr=request.form.get('addr')
        fir_id=request.form.get('fid')
        db.engine.execute(f"UPDATE criminal SET crmnl_id = '{crmnl_id}', crmnl_name = '{crmnl_name}', crmnl_gender = '{crmnl_gender}', crm_date = '{crm_date}', crm_type = '{crm_type}', crmnl_phno = '{crmnl_phno}', crmnl_addr = '{crmnl_addr}', fir_id = '{fir_id}' WHERE criminal.crmnl_id = '{crmnl_id}';")
        flash("Criminal Details is Updated","success")
        return redirect('/criminaldetails')

    return render_template('edit.html',posts=posts)

@app.route('/delete/<string:crmnl_id>',methods=['POST','GET'])
@login_required
def delete(crmnl_id):
    db.engine.execute(f"DELETE FROM criminal WHERE criminal.crmnl_id='{crmnl_id}'")
    flash("Details Deleted Successfully","danger")
    return redirect('/criminaldetails')


@app.route('/search',methods=['POST','GET'])
@login_required
def search():
    query=request.form.get('search')
    crmnl_name=Criminal.query.filter_by(crmnl_name=query).first()
    if crmnl_name:
        flash("Criminal is Available","info")
    else:
        flash("Criminal is Not Available","danger")
    return render_template('index.html')

app.run(debug=True)