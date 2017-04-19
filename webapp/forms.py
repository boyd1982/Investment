from flask_wtf import Form
from wtforms import StringField, TextAreaField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,URL
from models import users
class CodeForm(Form):
    code = StringField('Stock Code',validators=[DataRequired()])
class LoginForm(Form):
    username = StringField('Username',[DataRequired(),Length(max=20)])
    password = PasswordField('Password',[DataRequired()])
    remember = BooleanField("Remember Me")
    def validate(self):
        check_validate = super(LoginForm,self).validate()
        if not check_validate:
            return False
        user = users.query.filter_by(username = self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False
        return True
class RegisterForm(Form):
    username = StringField('Username',[DataRequired(),Length(max=255)])
    password = PasswordField('Password',[DataRequired()])
    confirm = PasswordField('Confirm Password',[DataRequired(),EqualTo('password')])
    def validate(self):
        check_validate = super(RegisterForm,self).validate()
        if not check_validate:
            return False
        user = users.query.filter_by(username = self.username.data).first()
        if user:
            self.username.errors.append("Users with that name already exists")
            return False
        return True