from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import Length , EqualTo ,Email, DataRequired ,ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self ,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("username already exist")

    def validate_email_id(self ,email_id_to_check):
        user = User.query.filter_by(email_id=email_id_to_check.data).first()
        if user:
            raise ValidationError("Email Address already exist already exist")





    username = StringField(label="User Name:" , validators=[Length(min=5,max=30) ,DataRequired()])
    email_id = StringField(label="Email Address:", validators=[Length(max=50),Email(),DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(max=6),DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo("password1")])
    submit = SubmitField(label="Create Account:")
