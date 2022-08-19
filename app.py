from flask import Flask, flash, request, redirect, url_for, render_template, session
#import urllib.request
import os
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
#from tensorflow.keras.preprocessing import image
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'

MODEL_PATH = 'model/stylecombining.py'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_content():
    if not any(f in ['content_file', 'style_file'] for f in request.files):
        flash('No file part')
        return redirect(request.url)
    submitted_file = 'content_file' if 'content_file' in request.files else 'style_file'
    file = request.files[submitted_file]
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session[submitted_file] = filename
        print('upload_image filename: ' + filename, os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html')
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
   
#def GAUSseg(img):
#    segmented6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,5,2)
#    return print(cv2.imshow('',segmented6))

def MEANseg(img, n): #value should be passed here for "n" (5) from the slider in index
    segmented8 = cv2.adaptiveThreshold(np.asarray(img, dtype=np.uint8),255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, n, 2)
    segmented8 = np.array(segmented8)
    return segmented8

@app.route('/maskInter/', methods=['POST', 'GET'])
def maskInter():
    import numpy.ma as ma
    n = int(request.args.get("n"))
    cm = str(request.args.get("cm"))
    cm2 = str(request.args.get("cm2"))
    print(cm, cm2)
    print(n)
    content_img = cv2.imread(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']+'/'+session['content_file']))
    content_img = cv2.cvtColor(content_img, cv2.COLOR_BGR2RGB)
    content_img2 = cv2.imread(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']+'/'+session['content_file']), cv2.IMREAD_GRAYSCALE)
    im = MEANseg(content_img2, n)
    mask = ma.masked_where(im>0, im)
    segmented_mask = ma.masked_array(im,mask)
    plt.figure(figsize=(7.50,7.50))
    plt.axis('off')
    if cm == 'None':
        if cm2 == 'None':
            plt.imshow(content_img)
            plt.imshow(segmented_mask, cmap="gist_gray")
    if cm == 'None' and cm2 != 'None':
        plt.imshow(content_img)
        plt.imshow(segmented_mask, cmap=cm2, interpolation='bilinear', alpha=0.7)
    if cm2 == 'None':
        if cm != 'None':
            plt.imshow(content_img2, cmap=cm, interpolation='bilinear')
            plt.imshow(segmented_mask)
    elif cm != 'None' and cm2 !='None':
        plt.imshow(content_img2, cmap=cm, interpolation='bilinear')
        plt.imshow(segmented_mask, cmap=cm2, interpolation='bilinear', alpha=0.7)
    filename = os.path.join(app.config['UPLOAD_FOLDER'], f'this_plot{time.time()}.png')
    plt.savefig(filename, dpi=72)
    print(filename)
    return '/'+filename


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run()