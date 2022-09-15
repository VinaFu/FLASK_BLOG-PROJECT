from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page=request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)

    # add new dummy posts
    # with open('posts.json') as f:
    #     data = json.load(f)
    
    # for x in data:
    #     post = Post(title=x.get('title'), content=x.get('content'), user_id=x.get('user_id')) 
    #     db.session.add(post)
    # db.session.commit()
    # end new dummy json crying 
    return render_template('home.html', posts=posts)


@main.route("/about")
def about ():
    return render_template('about.html',title="About Page")