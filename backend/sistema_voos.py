from app.services.passageiro_service import PassageiroService
from app.services.companhia_service import CompanhiaService
from app.services.voo_service import VooService
from app.services.aeronave_services import AeronaveService
from app.services.auditoria_service import executar_auditoria, Auditor
from app.services.funcionario_service import FuncionarioService
from app.database.session import SessionLocal
from app.services.auditoria_service import executar_auditoria

def criar_companhias_e_voos(companhia_service, aeronave_service, voo_service):
    companhia1 = companhia_service.criar_companhia("Azul")
    companhia2 = companhia_service.criar_companhia("Gol")

    aeronave1 = aeronave_service.criar_aeronave("Airbus A320", 180)
    aeronave2 = aeronave_service.criar_aeronave("Boeing 737", 200)

    voo_service.criar_voo("AZ101", "São Paulo", "Rio de Janeiro", aeronave1.id)
    voo_service.criar_voo("AZ102", "Belo Horizonte", "Brasília", aeronave1.id)
    voo_service.criar_voo("G3101", "Porto Alegre", "Recife", aeronave2.id)
    voo_service.criar_voo("G3102", "Curitiba", "Salvador", aeronave2.id)

    return "Companhias, aeronaves e voos criados com sucesso."

def listar_voos(voo_service):
    voos_da_companhia = voo_service.listar_todos_voos()
    return [f"Número Voo: {v.id} | Origem: {v.origem} | Destino: {v.destino}" for v in voos_da_companhia]

def listar_companhias(companhia_service):
    companhias = companhia_service.listar_todas_companhias()
    return [f"ID: {c.id} | Nome: {c.nome}" for c in companhias]


def criar_passageiro(passageiro_service, nome, cpf):
    passageiro = passageiro_service.criar_passageiro(nome, cpf)
    return f"Passageiro {passageiro.nome} cadastrado com sucesso!"


def criar_funcionario(funcionario_service, nome, matricula, cargo, cpf):
    funcionario = funcionario_service.criar_funcionario(nome, matricula, cargo, cpf)
    return f"Funcionário {funcionario.nome} cadastrado com sucesso!"


def adicionar_bagagem(passageiro_service, cpf, descricao, peso):
    passageiro_service.adicionar_bagagem(cpf, descricao, peso)
    return "Bagagem adicionada com sucesso."


def listar_passageiros_do_voo(voo_service, numero_voo):
    passageiros = voo_service.listar_passageiros_por_voo(numero_voo)
    return [f"- {p.nome} ({p.cpf})" for p in passageiros]


def auditar_voo(numero_voo):
    executar_auditoria(numero_voo)
    return "Auditoria concluída."

def main():
    db = SessionLocal()

    companhia_service = CompanhiaService(db)
    voo_service = VooService(db)
    passageiro_service = PassageiroService(db)
    funcionario_service = FuncionarioService(db)
    aeronave_service = AeronaveService(db)
    auditor = Auditor("Samukadev")


    while True:
        print("\n=== MENU SISTEMA AÉREO ===")
        print("1. Criar companhias e voos iniciais")
        print("2. Listar companhias")
        print("3. Criar passageiro")
        print("4. Criar funcionário")
        print("5. Adicionar bagagem ao passageiro")
        print("6. Listar passageiros de um voo")
        print("7. Listar todos os voos")
        print("8. Auditar voo")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        try:
            if escolha == "1":
                msg = criar_companhias_e_voos(companhia_service, aeronave_service, voo_service)
                print(msg)

            elif escolha == "2":
                linhas = listar_companhias(companhia_service)
                print("\nCompanhias cadastradas:")
                for linha in linhas:
                    print(linha)

            elif escolha == "3":
                nome = input("Nome do passageiro: ")
                cpf = input("CPF do passageiro: ")
                msg = criar_passageiro(passageiro_service, nome, cpf)
                print(msg)

            elif escolha == "4":
                nome = input("Nome do funcionário: ")
                matricula = input("Matrícula: ")
                cargo = input("Insira o cargo: ")
                cpf = input("CPF: ")
                msg = criar_funcionario(funcionario_service, nome, matricula, cargo, cpf)
                print(msg)

            elif escolha == "5":
                cpf = input("CPF do passageiro: ")
                descricao = input("Descrição da bagagem: ")
                peso = float(input("Peso da bagagem (kg): "))
                msg = adicionar_bagagem(passageiro_service, cpf, descricao, peso)
                print(msg)

            elif escolha == "6":
                numero_voo = input("Número do voo: ")
                linhas = listar_passageiros_do_voo(voo_service, numero_voo)
                print(f"\nPassageiros no voo {numero_voo}:")
                for linha in linhas:
                    print(linha)

            elif escolha == "7":
                linhas = listar_voos(voo_service)
                print(f"\nVoos disponíveis: ")
                for linha in linhas:
                    print(linha)        

            elif escolha == "8":
                numero_voo = input("Número do voo para auditoria: ")
                msg = auditar_voo(numero_voo)
                print(msg)

            elif escolha == "0":
                print("Saindo do sistema...")
                db.close()
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()