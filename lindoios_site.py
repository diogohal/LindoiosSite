from flask import Flask, render_template, request
from meme_generator import meme_generator
import os
app = Flask(__name__)

if __name__ == 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)

pictureFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = pictureFolder

@app.route('/', methods=['POST', 'GET'])
def lindois():
    if request.method == 'POST':
        meme_generator()
        picture = os.path.join(app.config['UPLOAD_FOLDER'], 'result.png')
        return render_template('index.html', picture=picture)
    return render_template('index.html')
    
