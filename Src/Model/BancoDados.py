from confg import db

class Registro(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  rfid = db.Column(db.String(8))
  dt = db.Column(db.String(15))
  hr = db.Column(db.String(15))
  statusReg = db.Column(db.String(150))

  def __init__(self, _rfid, _dt,_hr, _statusReg):
    self.rfid = _rfid
    self.dt = _dt
    self.hr = _hr
    self.statusReg = _statusReg

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  mat = db.Column(db.Integer)
  rfid = db.Column(db.String(8))
  nome = db.Column(db.String(150))
  endereco = db.Column(db.String(150))
  contato = db.Column(db.String(150))

  def __init__(self, _mat, _rfid, _nome, _endereco, _contato):    
    self.mat = _mat
    self.rfid = _rfid
    self.nome = _nome
    self.endereco = _endereco
    self.contato = _contato

class CartaoRFID(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  rfidCartao = db.Column(db.String(8))

  def __init__(self,_matCad,_rfidCartao):
    self.mat = _matCad
    self.rfidCartao = _rfidCartao