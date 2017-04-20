from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import AnonymousUserMixin
from flask_mongoengine import MongoEngine
db = SQLAlchemy()
mongo = MongoEngine()
roles = db.Table(
    'role_users',
    db.Column('user_name',db.String(80),db.ForeignKey('users.username')),
    db.Column('role_id',db.Integer,db.ForeignKey('role.id'))

)
class stock_basics(db.Model):
    __tablename__='stock_basics'
    trade_code = db.Column(db.String(20),primary_key=True)
    sec_name = db.Column(db.String(20))
    ipo_date = db.Column(db.DateTime())
    exch_city = db.Column(db.String(20))
    industry_gics = db.Column(db.String(20))
    concept = db.Column(db.String(200))
    curr = db.Column(db.String(20))
    fiscaldate = db.Column(db.String(20))
    auditor = db.Column(db.String(200))
    province = db.Column(db.String(20))
    city = db.Column(db.String(20))
    founddate = db.Column(db.DateTime())
    nature1 = db.Column(db.String(20))
    boardchairmen = db.Column(db.String(20))
    holder_controller = db.Column(db.String(20))
    website = db.Column(db.String(10000))
    phone = db.Column(db.String(200))
    majorproducttype = db.Column(db.String(200))
    majorproductname = db.Column(db.String(2000))

class users(db.Model):
    __tablename__='users'
    username = db.Column(db.String(20),primary_key=True)
    password = db.Column(db.String(45))
    roles = db.relationship(
        'Role',
        secondary=roles,
        backref=db.backref('users',lazy='dynamic')
    )
    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password)
    def is_authenticated(self):
        if isinstance(self,AnonymousUserMixin):
            return False
        else:
            return True
    def is_active(self):
        return True
    def is_anonymous(self):
        if isinstance(self,AnonymousUserMixin):
            return True
        else:
            return False
    def get_id(self):
        return unicode(self.username)
class Role(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(80),unique=True)
    description = db.Column(db.String(255))

available_roles = ('admin','finance_analyst','default')
class User(mongo.Document):
    username = mongo.StringField(required=True)
    password = mongo.StringField(required=True)
    roles = mongo.ListField(mongo.StringField(choices=available_roles))
    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password)
    def is_authenticated(self):
        if isinstance(self,AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True
    def is_anonymous(self):
        if isinstance(self,AnonymousUserMixin):
            return True
        else:
            return False
    def get_id(self):
        return unicode(self.username)
class stock_basicsm(mongo.Document):
    trade_code = mongo.StringField()
    SEC_NAME = mongo.StringField()
    IPO_DATE = mongo.DateTimeField()
    EXCH_CITY = mongo.StringField()
    INDUSTRY_GICS = mongo.StringField()
    CONCEPT = mongo.StringField()
    CURR = mongo.StringField()
    FISCALDATE = mongo.StringField()
    AUDITOR = mongo.StringField()
    PROVINCE = mongo.StringField()
    CITY = mongo.StringField()
    FOUNDDATE = mongo.DateTimeField()
    NATURE1 = mongo.StringField()
    BOARDCHAIRMEN = mongo.StringField()
    HOLDER_CONTROLLER = mongo.StringField()
    WEBSITE = mongo.StringField()
    PHONE = mongo.StringField()
    MAJORPRODUCTTYPE = mongo.StringField()
    MAJORPRODUCTNAME = mongo.StringField()
    meta = {'collection':'stock_basics'}