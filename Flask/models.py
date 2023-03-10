from extensions import db,login_manager
from app import app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class book(db.Model):   
    __tablename__ = "book"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(40))
    author=db.Column(db.String(40))
    image_url=db.Column(db.String(255))
    price=db.Column(db.Float, default=0.00)
    description=db.Column(db.Text, nullable=True)
    stock=db.Column(db.Boolean, default=False)
    genre=db.Column(db.String(40))
    language=db.Column(db.String(40))
    publisher=db.Column(db.String(40))


    def __repr__(self):
        return self.title


    def save(self):
        db.session.add(self)
        db.session.commit()


    def __init__(self,title,author,description, image_url, price,  stock, genre,language,publisher):
        self.title = title
        self.description = description
        self.author = author
        self.image_url = image_url
        self.price = price
        self.genre = genre
        self.language = language
        self.publisher = publisher
        self.stock = stock
    
class CommentModel(db.Model):   
    
    id=db.Column(db.Integer,primary_key=True)
    fullname=db.Column(db.String(40))
    language=db.Column(db.String(40))
    message=db.Column(db.Text)
    # create_at = db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self):
        return self.fullname


    def save(self):
        db.session.add(self)
        db.session.commit()


    def __init__(self,fullname,message,language):
        self.fullname = fullname
        self.message = message
        self.language = language
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name= db.Column(db.String(30),nullable=False)
    last_name= db.Column(db.String(40),nullable=False)
    email= db.Column(db.String(30),nullable=False)
    username= db.Column(db.String(30),nullable=False)
    password= db.Column(db.String(255),nullable=False)
    is_active= db.Column(db.Boolean,nullable=False)
    is_superuser = db.Column(db.Boolean,nullable=False)


    def __init__(self,first_name,last_name,email,username,password,is_active=True,is_superuser=False) :
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self.password=generate_password_hash(password)
        self.is_active=is_active
        self.is_superuser=is_superuser

    def save(self):
        db.session.add(self)
        db.session.commit()


    def check_password(self,password):
        return check_password_hash(self.password,password)