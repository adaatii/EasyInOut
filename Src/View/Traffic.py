from flask import Blueprint, render_template
from Src.Controller.RFID import RFID

Traffic = Blueprint('traffic', __name__)

@Traffic.route('/register/<rfid>', methods=['GET', 'POST'])    
def register(rfid):
  return "1" if RFID.Register(rfid) else "0"

@Traffic.route('/list', defaults={'page': 1})
@Traffic.route('/list/<int:page>')
def list(page):
  return render_template('lista.html', listData=RFID.List(page))
