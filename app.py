# from flask import Flask, render_template
import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from data import Articles
from test import animation

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    #test.readData("./data.ndbay.txt")
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id = id)


UPLOAD_FOLDER = './'

@app.route('/test', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            print('myfile', filename, UPLOAD_FOLDER)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('test.html')
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''
@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = 'http://127.0.0.1:5000/uploads/' + filename
    return render_template('test.html', filename=filename)

#
# @app.route('/test/image')
# def drawGif():
#     anim = animation("./data.ndbay.txt")
#     # TODO: How to convert anim to gif?
#     img = StringIO()
#     #fig.savefig(img)
#     #img.seek(0)
#
#     # return send_file(img, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True)
