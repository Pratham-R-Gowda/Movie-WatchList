from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField, URLField,PasswordField
from wtforms.validators import InputRequired, NumberRange,Email,Length,EqualTo,Optional

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director",  validators=[InputRequired()])

    year = IntegerField("Year",
                        validators=[
                            InputRequired(),
                            NumberRange(min=1900, message="Please enter a legitamate year!")
                            ]
                        )

    submit = SubmitField("Add Movie")

class StringListField(TextAreaField):
    def _value(self):
        if self.data is None:
            return ""
        else:
            return "\n".join(self.data)
        
    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    actors = StringListField("Actors")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description", validators=[Optional()])
    video_link = URLField("Video link", validators=[Optional()])
    submit = SubmitField("Submit")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(),Length(min=8, max=20, message="Password must be between 8 and 20 characters.")])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message="Password did not match.")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")