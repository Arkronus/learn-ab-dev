from app import db
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


practice_post_question = db.Table('practice_post_question',
                                  db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                                  db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
                                  )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    title = db.Column(db.String(255))
    text = db.Column(db.Text, nullable=True)
    #preview_text = db.Column(db.Text, nullable=False)
    preview_text = db.Column(db.Text)
    is_practice = db.Column(db.Boolean, nullable=False)
    sorting_column = db.Column(db.Integer)

    custom_html_file = db.Column(db.Text, nullable=True)
    slug = db.Column(db.String(100))
    questions = db.relationship('Question', secondary=practice_post_question, backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return 'Post id {} \n Post Title {}'.format(self.id, self.title)


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    text = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    sorting_column = db.Column(db.Integer)



    def __repr__(self):
        return 'Question id {} \n Text {}'.format(self.id, self.text)

