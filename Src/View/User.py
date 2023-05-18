from flask import Blueprint, render_template, request, flash, redirect, url_for
from Src.Controller.Users import UsersController
from Src.Model.BancoDados import UserBd

User = Blueprint('user', __name__)

@User.route('/list', defaults={'page':1})
@User.route('/list/<int:page>')
def listUser(page):
  return render_template('listaUsuario.html', listData=UsersController.List(page))

@User.route('/createUser', methods=['GET', 'POST'])
def createUser():
  _registro=request.form.get('mat')
  _rfid=request.form.get('rfid')  
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')

  if request.method == 'POST':
    if not _rfid or not _registro or not _nome or not _endereco or not _contato:     
      flash('Preencha todos os campos do formulário', 'error')
    else:
      if UsersController.createUser(_registro,_rfid,_nome,_endereco,_contato) :      
        return redirect(url_for('router.user.listUser'))
      else:
        flash('Cartão RFID ou Usuário já cadastrado', 'error')
  return render_template('criarUsuario.html')

@User.route('/<int:id>/updateUser', methods=['GET','POST'])
def updateUser(id):
  _registro=request.form.get('mat')
  _rfid=request.form.get('rfid')  
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')

  _user = UserBd.query.filter_by(id=id).first()
  if request.method == 'POST':
    if not _rfid or not _registro or not _nome or not _endereco or not _contato:      
        flash('Preencha todos os campos do formulário', 'error')
    else:
        if UsersController.updateUser(id, _registro, _rfid, _nome, _endereco, _contato):
          return redirect(url_for('router.user.listUser'))
        else:
          flash('Cartão RFID ou Usuário já cadastrado', 'error')
  return render_template('atualizarUsuario.html', user=_user) 

@User.route('/<int:id>/removeUser', methods=['GET','POST'])
def removeUser(id):
  UsersController.removeUser(id) 
  return redirect(url_for('router.user.listUser'))

