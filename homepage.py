from  flask import Flask,redirect ,url_for,render_template
app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Welcome to Yogesh's webstie admin page"
#@app.route('/notallowed')
# def notallowed():
#     return"You are not allowed to view this page"
# @app.route('/admin')
# def admin():
#     return redirect(url_for('user',name="Admin"))
# @app.route('/<name>')
# def user(name):
#     return f"Hello {name}!"
@app.route('/<name>')
def username(name):
    return render_template('index.html',content=["Yogesh","Ace","King"])
if __name__=='__main__':
    app.run(debug=True)