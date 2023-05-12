from Src.Model.BancoDados import Registro, User
from datetime import datetime
from pytz import timezone
from confg import db

class RFID:

  def Register(rfidCode): 
    #Grab date/time
    sao_paulo = timezone('America/Sao_Paulo')
    now = datetime.now(sao_paulo)
    data = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M:%S")

    #Filter user (Unique register) 
    user = User.query.filter_by(rfid=rfidCode).first()   
    if user == None:
      print("Não existe cadastro")
    else:
      query = Registro.query.filter_by(rfid=rfidCode, dt=data).all()
      status = "Saída" if query != [] and query[-1].statusReg == "Entrada" else "Entrada"     
      reg = Registro(rfidCode, data,hora, status)      
      db.session.add(reg)
      db.session.commit()
      

  def List(page, per_page=15):
    query = Registro.query.paginate(page=page, per_page=per_page)
    queryCount = Registro.query.count()
    return {
      "registros": query,
      "count": queryCount,
      "page": page,
      "per_page": per_page
    }

  
