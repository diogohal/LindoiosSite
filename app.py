from flask import Flask, render_template, request
# from meme_generator import meme_generator
import os
app = Flask(__name__)

pictureFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = pictureFolder

@app.route('/', methods=['POST', 'GET'])
def lindois():
    if request.method == 'POST':
        # meme_generator()
        picture = os.path.join(app.config['UPLOAD_FOLDER'], 'result.png')
        return render_template('index.html', picture=picture)
    return render_template('index.html')
    
