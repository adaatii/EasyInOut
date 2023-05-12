from Src.Model.BancoDados import User
from confg import db


class Users:  
  def createUser(mat,rfid,nome,endereco,contato):
    user = User(mat,rfid,nome,endereco,contato)
    db.session.add(user)
    db.session.commit()   


  def List(page, per_page=15):
    query = User.query.paginate(page=page, per_page=per_page)
    queryCount = User.query.count()
    return {
      "regUser": query,
      "count": queryCount,
      "page": page,
      "per_page": per_page
    }