from flask import Blueprint, render_template, url_for, request, flash, redirect
from Src.Controller.Users import Users

User = Blueprint('user', __name__)

@User.route('/user', defaults={'page':1})
@User.route('/user/<int:page>')

def user(page):
  return render_template('listaUsuario.html', listData=Users.List(page))

@User.route('/createUser', methods=['GET', 'POST'])
def createUser():
  _rfid=request.form.get('rfid')
  _registro=request.form.get('mat')
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')

  if request.method == 'POST':
    if not _rfid or not _registro or not _nome or not _endereco or not _contato:
      print("estou aki")
      flash('Preencha todos os campos do formulário', 'error')
    else:
      Users.createUser(_rfid,_registro,_nome,_endereco,_contato)
      ## return redirect(url_for('listaUsuarios.html'))
  return render_template('criarUsuario.html')

  

#def ConsultaCartao(rfid):
#  cartaoCAD = CartaoRFID.query.filter_by(rfidCartao=rfid).all()
#  if cartaoCAD==[]:
#    return False
#  else:
#    return True