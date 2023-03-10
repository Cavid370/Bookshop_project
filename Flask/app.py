from flask import Flask, request,render_template, url_for,redirect
from flask_login import login_user,login_required,logout_user
from werkzeug.security import check_password_hash



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/products_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "ABCDEF"

from extensions import *
from models import *
from forms import *



if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug=True)




@app.route("/")
def index():
    r = book.query.all()
    return render_template("homepage.html", books = r)


@app.route("/book/<int:book_id>", methods=['GET','POST'])
def bookid(book_id):
    r = book.query.filter(book.id==book_id).first()
    post_data=request.form
    print(post_data)
    form=CommentForm()    
    if request.method == "POST":
        form =CommentForm(data=post_data)
        print("fdsgsg")
        if form.validate_on_submit():    
            record = CommentModel(fullname=form.fullname.data,language = form.language.data,message= form.message.data)    
            record.save()
    return render_template('book.html',books = r, form=form)
    



@app.route("/product")
def product():
    name="Incognito"
    price=12.00
    old_price=15.00
    text="Kitab"
    image_book=url_for('static',filename="images/Inkognito.png")
    book_count=2
    book_language="Azərbaycan"
    book_genre="Psixologiya"
    book_author="David Eagleman"
    book_publish="Qanun nəşriyyat"
    return render_template("product.html",name=name,price=price,old_price=old_price,text=text,image_book=image_book,book_count=book_count,book_language=book_language,book_genre=book_genre,book_author=book_author,book_publish=book_publish)

@app.route("/newpage")
def newpage():
    return render_template("newpage.html")





@app.route('/register', methods=['GET','POST'])
def register():
        post_data=request.form
        print(post_data)
    
        form=RegisterForm()
        
        if request.method == "POST":
            form =RegisterForm(data=post_data)
            
            if form.validate_on_submit():
                
                record = User(first_name=form.first_name.data,email = form.email.data,last_name= form.last_name.data,password= form.password.data,username= form.username.data)
                
                record.save()
                return redirect('/login')
        return render_template('sign_up.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
        post_data=request.form    
        form=LoginForm()
        if request.method == "POST":
            post_data = request.data
            form = LoginForm(data=post_data)
            if form.validate_on_submit():
                user =User.query.filter_by(username=form.username.data).first()
                if check_password_hash(user.password,form.password.data):
                        login_user(user)
                        print("İstifadəçi daxil oldu")
                        return redirect("/")
                else:
                        print("İstifadəçi daxil ola bilmədi")
                
                
        
        return render_template('sign_in.html', form=form)


@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
        logout_user()
        return redirect('/login')
