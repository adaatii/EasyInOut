from Src.Model.BancoDados import FuncBd
from confg import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

class FuncsController:  
  def createFunc(mat,nome,endereco,contato,email,senha):
    passwd=generate_password_hash(senha)
    func = FuncBd(mat.upper(),nome.upper(),endereco.upper(),contato.upper(),email.upper(),passwd.upper())
    db.session.add(func) 
    try:
      db.session.commit()
      return True
    except IntegrityError:
      db.session.rollback()
      return False

  def updateFunc(id, _registro, _nome, _endereco, _contato, _email, _senha):   
    try:
      FuncBd.query.filter_by(id=id).update({'mat':_registro.upper(),'nome':_nome.upper(), 'endereco':_endereco.upper(),'contato':_contato.upper(),'email':_email.upper(),'senha':_senha.upper() })
      db.session.commit()
      return True
    except IntegrityError:
      db.session.rollback()
      return False
      
  def removeFunc(id):   
    _func = FuncBd.query.filter_by(id=id).first()    
    db.session.delete(_func)
    db.session.commit()
    
  def List(page,_funcFilter, per_page=15):
    print(_funcFilter)
    if _funcFilter == None or len(_funcFilter)<1 :
      query = FuncBd.query.paginate(page=page, per_page=per_page)
      queryCount = FuncBd.query.count()
    else: 
      query = FuncBd.query.filter(FuncBd.nome.like('%'+_funcFilter+'%')).paginate(page=page, per_page=per_page)        
      queryCount = FuncBd.query.count()

    return {
      "regFunc": query,
      "count": queryCount,
      "page": page,
      "per_page": per_page
    }