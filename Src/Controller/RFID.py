from Src.Model.BancoDados import Registro, UserBd
from datetime import datetime
from pytz import timezone
from confg import db

class RFID:
    def Register(rfidCode):
        # Grab date/time
        sao_paulo = timezone("America/Sao_Paulo")
        now = datetime.now(sao_paulo)
        data = now.strftime("%d/%m/%Y")
        hora = now.strftime("%H:%M:%S")

        # Filter user (Unique register)
        user = UserBd.query.filter_by(rfid=rfidCode).first()
        if user == None:
            print("Não existe cadastro")
            return "0"
        else:
            # Filter rfid regiters
            query = Registro.query.filter_by(rfid=rfidCode, dt=data).all()
            status = (
                "Saída"
                if query != [] and query[-1].statusReg == "Entrada" else "Entrada"
            )
            # Create an obj of Register and add in DB
            reg = Registro(rfidCode, data, hora, status)
            db.session.add(reg)
            db.session.commit()
            return "1"

    def List(page, _data, per_page=10):
        sao_paulo = timezone("America/Sao_Paulo")
        now = datetime.now(sao_paulo)
        data = now.strftime("%d/%m/%Y")
        print(data)
        if _data == "None" or _data is None or len(_data) < 1:
            query = (
                Registro.query.join(UserBd, Registro.rfid == UserBd.rfid)
                .add_columns(UserBd.nome, Registro.dt, Registro.hr, Registro.statusReg)
                .filter(Registro.dt == data)
                .paginate(page=page, per_page=per_page)
            )

        else:
            _dataFilter = datetime.strptime(_data, "%Y-%m-%d").strftime("%d/%m/%Y")
            query = (
                Registro.query.join(UserBd, Registro.rfid == UserBd.rfid)
                .add_columns(UserBd.nome, Registro.dt, Registro.hr, Registro.statusReg)
                .filter(Registro.dt == _dataFilter)
                .paginate(page=page, per_page=per_page)
            )

        queryCount = Registro.query.count()

        return {
            "registros": query,
            "page": page,
            "per_page": per_page,
            "count": queryCount,
        }
