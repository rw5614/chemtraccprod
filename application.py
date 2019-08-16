from flask import Flask, render_template, g, redirect, url_for, abort, session, request, jsonify
# from flask_login import LoginManager, current_user, login_required
from AmazonCognito.AmazonCognito import AmazonCognito
from functools import wraps
import time
from urllib.parse import quote
import requests

app = Flask(__name__, static_url_path='/static')
# login_manager = LoginManager()
# login_manager.init_app(app)
auth_base_url = "https://labtracc.auth.us-east-1.amazoncognito.com"
# TODO: change to herokuapp and whitelist
# current_website_addr = 'https://labtracc.herokuapp.com'  # http://localhost:5000
current_website_addr = 'http://localhost:5000'  # https://labtracc.herokuapp.com
amazonCognito = AmazonCognito("7m1prek8gppfutbgs11kukg8tg",
                              "176k6jem77d561vgmcp8gnkadapm5vcoi1vt4c4ukdfnre2soioi",
                              "https://labtracc.auth.us-east-1.amazoncognito.com",
                              current_website_addr + "/users/callback")
app.secret_key = b'o29asdgjdfglsklksfgkkjlkfdkjhkcsjdjsl;kfbhvjijioejweqjsfdsdjfoijicj%sdfd3r3f0a*'

base_api_url = 'https://0b8noolotb.execute-api.us-east-1.amazonaws.com/dev/'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # TODO: Redundandant checking logged in, when refresh_sessions does it already
        # FIX: refresh_session should run first (crossing fingers) and then it'll clear any stale sessions
        # TODO: Is this a security vulnerability? Maybe the client could refuse to clear sessions?
        # if 'jwt' in session.keys() and session['jwt'] is not None and amazonCognito.check_logged_in(
        # 		session['jwt']['access_token']):
        if 'jwt' in session.keys() and session['jwt'] is not None:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return decorated_function


@app.errorhandler(401)
def not_authorized(e):
    return render_template("401.html"), 401


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def refresh_session():
    print("base_url is ")
    print(request.base_url)
    # Checks if the session cookie has a jwt, and if it's valid.
    # Then, proceeds to refresh it if it is. If not valid, then clear the session cookie again, for safe measure.
    if 'jwt' in session.keys() and session['jwt'] is not None \
            and 'access_token' in session['jwt'] \
            and session['jwt']['access_token'] is not None \
            and amazonCognito.check_logged_in(session['jwt']['access_token']):
        # TODO: check_logged_in and get_user_info both check if the user is logged in. COuld we combine these into one?
        print(session['jwt'])
        # The user is logged in at the moment.
        g.user = amazonCognito.get_user_info(session['jwt']['access_token'])
        if 'refresh_token' in session['jwt'] and session['jwt']['refresh_token'] is not None:
            # Only refresh the token if there's less than 15 minutes left.
            if 'time_of_refresh' in session['jwt'] and int(time.time()) > session['jwt']['time_of_refresh'] + 2700:
                new_tokens = amazonCognito.refresh(
                    session['jwt']['refresh_token'])
                if new_tokens:
                    # Because the new response doesn't contain a refresh_token, we must resupply it ourselves
                    new_tokens['refresh_token'] = session['jwt']['refresh_token']
                    session['jwt'] = new_tokens

                    # Add the time of refresh to the session cookie
                    session['time_of_refresh'] = int(time.time())
                    session.modified = True

    else:
        # Just in case there is a stale session cookie out there, we don't keep running amazonCognito.check_logged_in
        session.clear()
    # session.modified = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def redirdashboard():
    # Find the default groupID and redirect to that.
    get_groups_url = base_api_url + 'qa/group'

    r = requests.get(get_groups_url, json={'userName': g.user['username']})

    print(r.json())
    # Will throw an error if there are no groups!!
    first_group = r.json()[0]

    return redirect(url_for('dashboard', groupID=first_group))


@app.route("/dashboard/<groupID>")
@login_required
def dashboard(groupID):
    q = request.args.get('q')

    pageNum = request.args.get('pagenum')

    if q is None:
        q = ""

    if pageNum is None:
        pageNum = 1
    else:
        pageNum = int(pageNum)

    print(q)
    groupID
    userName = g.user['username']
    frm = (pageNum - 1) * 10

    search_url = base_api_url + 'qa/search'

    r = requests.get(search_url, json={
        'q': q,
        'groupID': groupID,
        'userName': userName,
        'from': frm
    })

    returned_search_results = r.json()

    print(returned_search_results)

    count = int(returned_search_results['count'])
    maxpage = int(count/10)

    hits = returned_search_results['docs']
    returned_hits = []
    for item in hits:
        returned_hits.append(item['_id'])

    print(returned_hits)

    # get the returned_hits using a get request
    get_questions_url = base_api_url + 'qa/question'

    r = requests.get(get_questions_url, params={"_id": returned_hits})

    print(r.text)

    questions = r.json()

    # get whether or not the user liked each question
    get_likes_url = base_api_url + 'qa/likes'
    r = requests.get(get_likes_url, json={
                     'userName': userName, 'inputIDs': returned_hits})

    like_stats = r.json()

    # iterate through and fill in the questions
    list_of_questions = []
    for question in questions:
        if question is None:
            continue

        liked = False
        if question["_id"]["$oid"] in like_stats:
            liked = like_stats[question["_id"]["$oid"]]

        question_dict = {
            'questiontext': question['question'],
            'questionurl': 'question?id=' + question["_id"]["$oid"],
            'moreinfo': question["body"],
            'username': question["email"],
            'userurl': 'users?id=' + question['userName'],
            'numcomments': len(question['answers']) if 'answers' in question else 0,
            'timestamp': time.ctime(question['timestamp']),
            'liked': liked,
            'numberlikes': len(question['upvotes']) if 'upvotes' in question else 0,
            'tags': question['tags']
        }
        list_of_questions.append(question_dict)

    print(list_of_questions)

    page_props = {
        'currentpage': pageNum,
        'maxpage': maxpage,
        'query': quote(q)
    }

    return render_template("dashboard.html", questions=list_of_questions, paginator=page_props)


@app.route("/search")
@login_required
def search():
    # if 'jwt' in session.keys() and session['jwt'] is not None and amazonCognito.check_logged_in(
    # 		session['jwt']['access_token']):
    # print(amazonCognito.get_user_info(session['jwt']['access_token']))

    # TODO:I just hardcoded some items here. So this is obv not good.
    items = [{'name': 'steve', 'location': 'here',
              'description': 'a dude', 'timestamp': 12353224}]
    return render_template("search.html", items=items)


@app.route("/add")
@login_required
def add():
    # if 'jwt' in session.keys() and session['jwt'] is not None and amazonCognito.check_logged_in(
    # 		session['jwt']['access_token']):
    # print(amazonCognito.get_user_info(session['jwt']['access_token']))
    return render_template("add.html")


@app.route("/login")
def login():
    return redirect(
        auth_base_url + "/login?response_type=code&client_id=7m1prek8gppfutbgs11kukg8tg&redirect_uri=" + current_website_addr + "/users/callback")


@app.route("/logout")
def logout():
    # Remove the session cookie and log out.
    session.clear()
    # session.modified = True

    # TODO: Perhaps interesting (bad) things could happen if the user directly calls this endpoint and doesn't use /logout?
    return redirect(
        auth_base_url + "/logout?client_id=7m1prek8gppfutbgs11kukg8tg&logout_uri=" + current_website_addr)


@app.route("/users/callback")
def callback():
    # print(request.args['code'])
    # print(type(request.args['code']))
    # print(request.args)

    # Get the auth token, which we proceed to store in the user session cookie.
    # The existence of a valid auth token in the session cookie determines if the user is logged in or not.
    if 'code' in request.args.keys():
        tokens = amazonCognito.get_auth_token(request.args['code'])
        print(tokens)
        session['jwt'] = tokens
        session.modified = True

    return redirect("../")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/chartdata")
def chartdata():
    return jsonify(something=1, other=2)


@app.route("/question")
def show_question():
    return render_template('question.html')


@app.route("/user")
def user_page():
    return render_template('user.html')


@app.route("/postlike", methods=['POST'])
@login_required
def post_like():
    print(request.form.to_dict())
    print(request.json)
    return '', 200


if __name__ == '__main__':
    app.run()
