from flask import Blueprint, render_template, request, flash, redirect, url_for
from Src.Controller.Funcs import FuncsController
from Src.Model.BancoDados import FuncBd

Func = Blueprint('func', __name__)

@Func.route('/list', defaults={'page':1})
@Func.route('/list/<int:page>')
def listFunc(page):
  return render_template('listaFuncionario.html', listData=FuncsController.List(page))

@Func.route('/createFunc', methods=['GET', 'POST'])
def createFunc():
  _registro=request.form.get('mat') 
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')
  _email=request.form.get('email')
  _senha=request.form.get('senha')

  if request.method == 'POST':
    if not _registro or not _nome or not _endereco or not _contato or not _email or not _senha:     
      flash('Preencha todos os campos do formulário', 'error')
    else:
      if FuncsController.createFunc(_registro,_nome,_endereco,_contato,_email,_senha):      
        return redirect(url_for('router.func.listFunc'))
      else:
        flash('Funcionário já cadastrado', 'error')
  return render_template('criarFuncionario.html')

@Func.route('/<int:id>/updateFunc', methods=['GET','POST'])
def updateFunc(id):
  _registro=request.form.get('mat')  
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')
  _email=request.form.get('email')
  _senha=request.form.get('senha')

  _func = FuncBd.query.filter_by(id=id).first()
  if request.method == 'POST':
    if not _registro or not _nome or not _endereco or not _contato or not _email or not _senha:     
        flash('Preencha todos os campos do formulário', 'error')
    else:
        if FuncsController.updateFunc(id, _registro,_nome,_endereco,_contato,_email,_senha):
          return redirect(url_for('router.func.listFunc'))
        else:
          flash('Funcionário já cadastrado', 'error')
  return render_template('atualizarFuncionario.html', func=_func) 

@Func.route('/<int:id>/removeFunc', methods=['GET','POST'])
def removeFunc(id):
  FuncsController.removeFunc(id) 
  return redirect(url_for('router.func.listFunc'))

