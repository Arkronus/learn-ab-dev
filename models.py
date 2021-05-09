from app import db
from datetime import datetime

practice_post_question = db.Table('practice_post_question',
                                  db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                                  db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
                                  )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text, nullable=False)
    is_practice = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return 'Post id {} \n Post Title {}'.format(self.id, self.title)

    questions = db.relationship('Question', secondary=practice_post_question, backref=db.backref('posts', lazy='dynamic'))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return 'Question id {} \n Text {}'.format(self.id, self.text)