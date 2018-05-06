# from flask import Flask, render_template
import os
import hashlib
from flask import Flask, jsonify, request, redirect, url_for, send_file, send_from_directory, render_template
from data import Articles
from spectraplot import animation

app = Flask(__name__)

Articles = Articles()

def content_type_error(item):
    return jsonify(error="Unsupported Content Type %s" % item.content_type), 415

def create_gif(filenames, samples, durationSec):
    hasher = hashlib.md5()
    #samples is int, but update can recieve only bytes
    #here we update hasher with values from sliders:
    hasher.update(str(samples).encode())
    hasher.update(str(durationSec).encode())
    #now we again update hasher with content of each file:
    for filename in filenames:
        print('Hashing', filename)
        hasher.update(open(filename, "r").read().encode())
    output_file = 'static/images/plot.%s.gif' % hasher.hexdigest()
    print('Output hash-based filename created:', output_file)
    if not os.path.isfile(output_file):
        anim = animation(filenames, samples, durationSec * 1000)
        print('Animation created')
        anim.save(output_file, writer='imagemagick', fps=24)
        print('Animation saved')
    else:
        print('Animation exists')
    return output_file

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

@app.route('/spectra')
def spectrum_page():
    return render_template("spectra.html")

@app.route('/spectra/show', methods=['POST'])
def generate_gif():
    print('imagepage: form', request.form)
    print('imagepage: files', request.files)
    inputFiles = request.files.getlist('inputFiles')
    print('imagepage: inputFiles', inputFiles)
    filenames = []
    for item in inputFiles:
        print('  filename:%s, content_type:%s, name:%s, mimetype:%s' %
         (item.filename,item.content_type,item.name,item.mimetype))
        #we check content type, must be only txt
        if item.content_type != 'text/plain':
            return content_type_error(item)
        #we create filename and add to it index
        filename = './db/temp/data%s.txt' % len(filenames)
        filenames.append(filename)
        item.save(filename)
    # generate gif (or default)
    points = int(request.form.get('points'))
    time = int(request.form.get('time'))
    output_file = create_gif(filenames, points, time) if filenames else "static/images/sample2.jpg"
    return jsonify(image=output_file)


if __name__ == '__main__':
    app.run(debug=True)
