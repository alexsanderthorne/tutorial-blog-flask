from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        new_post = Post(
            title=request.form['title'],
            content=request.form['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('post', post_id=new_post.id))
    return render_template('new_post.html', title='Novo Post')

if __name__ == '__main__': #</ arquivo principal do app-->
    with app.app_context():
        db.create_all() #execute o python app.py para criar o banco de dados
    app.run(debug=True)