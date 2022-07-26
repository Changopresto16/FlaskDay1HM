from app import app 
from flask import render_template
import requests

@app.route('/')
def index():
    staff = [{'name':'Com Truise', 'img': 'https://f4.bcbits.com/img/a4006172154_10.jpg', 'Genre':'Melodic retro future synthwave'},
    {'name':'Khrungbin', 'img': 'https://www.bricartsmedia.org/sites/default/files/paragraphs/cico/Khruangbin_JackieLeeYoung_Stubbs_9.18.21-09771_0.jpg', 'Genre':'pan Asian jazz funk'},
    {'name':'DeathFromAbove 1979', 'img': 'https://www.ajournalofmusicalthings.com/wp-content/uploads/Death-from-Above-1979-logo.jpg', 'Genre':'Blister punk/post punk'},
    {'name':'Beastie Boys', 'img': 'https://s3.amazonaws.com/criterion-production/films/5d4e823b0423c12ee26cc989dfc1b576/hXfCsS5uWKrEmRzTRFosLsvJgxLie4_large.jpg', 'Genre':'Hiphop/Rap'},
    {'name':'Mr. Oizo', 'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGI-ujPlxdt0IQdKQF_N0vSfVFG8LEXIOYIw&usqp=CAU', 'Genre':'French House/Electronic'}]

    return render_template('index.html', names=staff)

@app.route('/contact')
def contact():
    return

@app.route('/', methods=['GET', 'POST'])
def index():
    if requests.method == 'POST':
        return render_template('Index.html')