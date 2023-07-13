from flask import Blueprint, render_template, request, flash, redirect, url_for
from Src.Controller.Employees import EmployeeController
from Src.Model.BancoDados import FuncBd
from flask_login import login_required
from Src.Model import Regex

Employee = Blueprint('employee', __name__)

@Employee.route('/list', defaults={'page':1}, methods=['GET'])
@Employee.route('/list/<int:page>', methods=['GET'])
@login_required
def listEmployee(page):
  _employeeFilter=request.values.get('nomeFuncionario')
  if _employeeFilter == 'None' or _employeeFilter is None:
    _employeeFilter=""  
  return render_template('listaFuncionario.html', listData=EmployeeController.List(page,_employeeFilter),_nameEmployee=_employeeFilter)

@Employee.route('/createEmployee', methods=['GET', 'POST'])
@login_required
def createEmployee():
  _registro=request.form.get('mat') 
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')
  _email=request.form.get('email')
  _senha=request.form.get('senha')
  
  if request.method == 'POST':
    if EmployeeController.checkEmail(_email):
      flash('Email já cadastrado', 'error')
    else:
      if any((x is None or len(x)<1) for x in [_registro, _nome, _endereco, _contato , _email, _senha]):
        flash('Preencha todos os campos do formulário', 'error')
      else:
        if Regex.contatoRegex(_contato):
          if Regex.emailRegex(_email):
            if EmployeeController.createEmployee(_registro,_nome,_endereco,_contato,_email,_senha):      
              return redirect(url_for('router.employee.listEmployee'))
            else:
              flash('Funcionário já cadastrado', 'error')
          else:
            flash('E-mail inválido', 'error')
        else:
            flash('Celular inválido', 'error')
  return render_template('criarFuncionario.html')

@Employee.route('/<int:id>/updateEmployee', methods=['GET','POST'])
@login_required
def updateEmployee(id):
  _registro=request.form.get('mat')  
  _nome=request.form.get('nome')
  _endereco=request.form.get('endereco')
  _contato=request.form.get('contato')
  _email=request.form.get('email')
  _senha=request.form.get('senha')

  _employee = FuncBd.query.filter_by(id=id).first()
  if request.method == 'POST':
    if any((x is None or len(x)<1) for x in [_registro, _nome, _endereco, _contato , _email, _senha]):
        flash('Preencha todos os campos do formulário', 'error')
    else:
        if EmployeeController.updateEmployee(id, _registro,_nome,_endereco,_contato,_email,_senha):
          return redirect(url_for('router.employee.listEmployee'))
        else:
          flash('Funcionário já cadastrado', 'error')
  return render_template('atualizarFuncionario.html', employee=_employee) 

@Employee.route('/<int:id>/removeEmployee', methods=['GET','POST'])
@login_required
def removeEmployee(id):
  EmployeeController.removeEmployee(id) 
  return redirect(url_for('router.employee.listEmployee'))

