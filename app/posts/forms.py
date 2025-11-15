from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, DateTimeLocalField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=150)])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField(
        'Category',
        choices=[
            ('news', 'News'),
            ('publication', 'Publication'),
            ('tech', 'Tech'),
            ('other', 'Other')
        ],
        validators=[DataRequired()]
    )
    is_active = BooleanField('Active', default=True)
    publish_date = DateTimeLocalField('Publish Date', format='%Y-%m-%dT%H:%M')
    submit = SubmitField('Save')