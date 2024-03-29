from flask import Blueprint, render_template, request
from Src.Controller.RFID import RFID
from flask_login import login_required
from datetime import datetime
from pytz import timezone


Traffic = Blueprint('traffic', __name__)

@Traffic.route('/register/<rfid>', methods=['GET', 'POST'])    
def register(rfid):
  return RFID.Register(rfid)

@Traffic.route('/list', defaults={'page': 1}, methods=['GET','POST'])
@Traffic.route('/list/<int:page>', methods=['GET','POST'])
@login_required
def list(page):
  _date=request.values.get('filtroData')   
  return render_template('lista.html', listData=RFID.List(page,_date),_data=_date)