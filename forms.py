from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms.validators import ValidationError, DataRequired, Length



class QuestionForm(FlaskForm):
    user_answer = StringField('Мой ответ:', validators=[DataRequired(message = "Заполните это поле")])
    submit = SubmitField('Проверить')
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.question = question
        # self.user_answer = StringField('Мой ответ:', validators=[DataRequired(),
        #                                                          EqualTo(self.question.answer,
        #                                                                  message = 'Неверный ответ, попробуйте снова')])
        # self.user_answer = StringField('Мой ответ:', validators=[DataRequired()])
    def validate_user_answer(self, form):
        if self.question.answer != form.data:
            raise ValidationError('Неверный ответ, попробуйте снова')


#
# class QuestionForm(FlaskForm):
#
#     user_answer = StringField('Мой ответ:', validators=[DataRequired()])
#     submit = SubmitField('Проверить')
