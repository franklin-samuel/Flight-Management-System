from app.services.passageiro_service import PassageiroService
from app.services.companhia_service import CompanhiaService
from app.services.voo_service import VooService
from app.services.aeronave_services import AeronaveService
from app.services.auditoria_service import executar_auditoria, Auditor
from app.services.funcionario_service import FuncionarioService
from app.database.session import SessionLocal


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
        print("7. Auditar voo")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                companhia1 = companhia_service.criar_companhia("Azul")
                companhia2 = companhia_service.criar_companhia("Gol")

                aeronave1 = aeronave_service.criar_aeronave("Airbus A320", 180)
                aeronave2 = aeronave_service.criar_aeronave("Boeing 737", 200)

                voo_service.criar_voo("AZ101", "São Paulo", "Rio de Janeiro", aeronave1.id)
                voo_service.criar_voo("AZ102", "Belo Horizonte", "Brasília", aeronave1.id)

                voo_service.criar_voo("G3101", "Porto Alegre", "Recife", aeronave2.id)
                voo_service.criar_voo("G3102", "Curitiba", "Salvador", aeronave2.id)

                print("Companhias, aeronaves e voos criados com sucesso.")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "2":
            companhias = companhia_service.listar_todas_companhias()
            print("\nCompanhias cadastradas:")
            for c in companhias:
                print(f"ID: {c.id} | Nome: {c.nome}")

        elif escolha == "3":
            nome = input("Nome do passageiro: ")
            cpf = input("CPF do passageiro: ")
            try:
                passageiro = passageiro_service.criar_passageiro(nome, cpf)
                print(f"Passageiro {passageiro.nome} cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "4":
            nome = input("Nome do funcionário: ")
            matricula = input("Matrícula: ")
            cargo = input("Cargo: ")
            cpf = input("CPF: ")
            try:
                funcionario = funcionario_service.criar_funcionario(nome, matricula, cargo, cpf)
                print(f"Funcionário {funcionario.nome} cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "5":
            cpf = input("CPF do passageiro: ")
            descricao = input("Descrição da bagagem: ")
            try:
                peso = float(input("Peso da bagagem (kg): "))
                bagagem = passageiro_service.adicionar_bagagem(cpf, descricao, peso)
                print("Bagagem adicionada com sucesso.")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "6":
            numero_voo = input("Número do voo: ")
            try:
                passageiros = voo_service.listar_passageiros_por_voo(numero_voo)
                print(f"\nPassageiros no voo {numero_voo}:")
                for p in passageiros:
                    print(f"- {p.nome} ({p.cpf})")
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "7":
            numero_voo = input("Número do voo para auditoria: ")
            try:
                executar_auditoria(numero_voo)
            except Exception as e:
                print(f"Erro: {e}")

        elif escolha == "0":
            print("Saindo do sistema...")
            db.close()
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
