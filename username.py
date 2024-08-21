from flask import Flask,render_template
app = Flask(__name__)
@app.route('/username/<name>')
def user(name):
    return render_template('username.html',name=name)
@app.errorhandler(404)
def errorone(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def errorone(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.run(debug=True)