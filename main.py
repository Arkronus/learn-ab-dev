from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    text = db.Column(db.Text, nullable = False)
    created_at  =db.Column(db.DateTime, default = datetime.utcnow())

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/test')
def test():
    return render_template("user.html")

@app.route('/sumbit-results', methods = ['POST', 'GET'])
def sumbit_results():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        article = Article(title = title, text = text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Что-то пошло не так, попробуйте еще раз"
    return render_template("sumbit-results.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template("posts.html", articles = articles)

@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article = article)


if __name__ == "__main__":
    app.run(debug=True)
