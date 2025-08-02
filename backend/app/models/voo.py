#Voo, Miniaeronave, Companhia Aérea
from app.database.models import Passageiro, Funcionario
            
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo 
        self.capacidade = capacidade 
    
    def resumo_voo(self):
        return f"{self.modelo} com capacidade para {self.capacidade} passageiros. "

class Voo:
    def __init__(self, voo_db):
        self._db = voo_db
        self.numero_voo = voo_db.numero_voo
        self.origem = voo_db.origem
        self.destino = voo_db.destino
        self.aeronave = MiniAeronave(voo_db.aeronave.modelo, voo_db.aeronave.capacidade)
        self.passageiros = [Passageiro(p.nome, p.cpf) for p in voo_db.passageiros]
        self.tripulacao = [Funcionario(f.cargo, f.matricula, f.nome, f.cpf) for f in voo_db.tripulacao]

        # implementar database nas listas 

    def adicionar_passageiro(self, passageiro):
        if len(self.passageiros) >= self.aeronave.capacidade:
            raise ValueError("Capacidade da aeronave excedida.")
        if any(p.cpf == passageiro.cpf for p in self.passageiros):
            raise ValueError("Passageiro já presente no voo.")
        self.passageiros.append(passageiro)

        passageiro_db = self._db_session.query(Passageiro).filter_by(cpf=passageiro.cpf).first()
        if not passageiro_db:
            passageiro_db = Passageiro(nome=passageiro.nome, cpf=passageiro.cpf)
            self._db_session.add(passageiro_db)
            self._db_session.commit()
            self._db_session.refresh(passageiro_db)

        self._db.passageiros.append(passageiro_db)
        self._db_session.commit()

    def adicionar_tripulante(self, tripulante):
        if any(t.cpf == tripulante.cpf for t in self.tripulacao):
            raise ValueError("Tripulante já presente na tripulação.")

        self.tripulacao.append(tripulante)

        funcionario_db = self._db_session.query(Funcionario).filter_by(cpf=tripulante.cpf).first()
        if not funcionario_db:
            funcionario_db = Funcionario(
                nome=tripulante.nome,
                cpf=tripulante.cpf,
                cargo=tripulante.cargo,
                matricula=tripulante.matricula
            )
            self._db_session.add(funcionario_db)
            self._db_session.commit()
            self._db_session.refresh(funcionario_db)

        self._db.tripulacao.append(funcionario_db)
        self._db_session.commit()

    def listar_passageiros(self):
        for passageiro in self.passageiros:
            print(passageiro)
    
    def listar_tripulantes(self):
        for tripulante in self.tripulação:
            print(tripulante)    

class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, companhia_db, db_session):
        self._db = companhia_db
        self._db_session = db_session
        self._nome = companhia_db.nome
        self._voos = [Voo(voo_db, db_session) for voo_db in companhia_db.voos]

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        novo_nome = novo_nome.strip()
        if len(novo_nome) < 3:
            raise ValueError("o nome da companhia deve ter pelo menos 3 letras.")
        self._nome = novo_nome
        self._db.nome = novo_nome
        self._db_session.commit()
       
    def adicionar_voo(self, voo):
        self._voos.append(voo)
        self._db.voos.append(voo._db)
        self._db_session.commit()
        
    def buscar_voo(self, numero: str):
        for voo in self._voos:
            if voo.numero_voo == numero:
                return voo
        return None
        
    def listar_voos(self):
        for voo in self._voos:
            print(voo)


