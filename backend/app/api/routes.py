from flask import Blueprint, request, jsonify
from app.database.session import SessionLocal
from app.database.crud import buscar_voo
from app.models.pessoa import Funcionario
from app.services.voo_service import criar_voo, listar_todos_voos, adicionar_passageiro_ao_voo, buscar_passageiro_por_cpf

routes = Blueprint("routes", __name__)

@routes.route("/voos", methods=["POST"])
def criar_voo_route():
    """
    Criar um novo voo
    ---
    tags:
      - Voos
    parameters:
      - in: body
        name: body
        schema:
          properties:
            numero_voo:
              type: string
            origem:
              type: string
            destino:
              type: string
    responses:
      201:
        description: Voo criado com sucesso
      400:
        description: Erro na criação
    """
    db = SessionLocal()
    try:
        data = request.get_json()
        novo_voo = criar_voo(db, data)
        return jsonify({
            "mensagem": "Voo criado com sucesso.",
            "numero_voo": novo_voo.numero_voo
        }), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        db.close()

@routes.route("/voos", methods=["GET"])
def lista_voos_route():
    """
    Listar todos os voos
    ---
    tags:
      - Voos
    responses:
      200:
        description: Lista de voos
    """
    db = SessionLocal()
    try:
        voos = listar_todos_voos(db)
        resultado = []
        for voo in voos:
            resultado.append({
                "numero_voo": voo.numero_voo,
                "origem": voo.origem,
                "destino": voo.destino,
                "modelo": voo.aeronave.modelo,
                "capacidade": voo.aeronave.capacidade,
                "quantidade_passageiros": len(voo.passageiros),
                "quantidade_tripulacao": len(voo.tripulacao)
            })
        return jsonify(resultado)
    finally:
        db.close()

@routes.route("/passageiros/<cpf>", methods=["GET"])
def buscar_passageiro_route(cpf):
    """
    Buscar passageiro por CPF
    ---
    tags:
      - Passageiros
    parameters:
      - in: path
        name: cpf
        type: string
        required: true
    responses:
      200:
        description: Passageiro encontrado
      404:
        description: Passageiro não encontrado
    """
    db = SessionLocal()
    try:
        passageiro = buscar_passageiro_por_cpf(db, cpf)
        return jsonify({
            "nome": passageiro._nome,
            "cpf": passageiro._cpf,
            "bagagens": passageiro.bagagens
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 404
    finally:
        db.close()

@routes.route("/voos/<numero_voo>/passageiros", methods=["POST"])
def adicionar_passageiro_route(numero_voo):
    """
    Adicionar passageiro ao voo
    ---
    tags:
      - Passageiros
    parameters:
      - in: path
        name: numero_voo
        required: true
        type: string
      - in: body
        name: body
        schema:
          properties:
            nome:
              type: string
            cpf:
              type: string
    responses:
      200:
        description: Passageiro adicionado
    """
    db = SessionLocal()
    try:
        data = request.get_json()
        nome = data.get("nome")
        cpf = data.get("cpf")

        voo = buscar_voo(db, numero_voo)
        if not voo:
            return jsonify({"erro": "Voo não encontrado."}), 404

        class PassageiroMock:
            def __init__(self, nome, cpf):
                self.nome = nome
                self.cpf = cpf
        
        passageiro = PassageiroMock(nome, cpf)
        voo_atualizado = adicionar_passageiro_ao_voo(db, voo, passageiro)

        return jsonify({
            "mensagem": f"Passageiro {nome} adicionado ao voo {numero_voo}.",
            "total_passageiros": len(voo_atualizado.passageiros)
        }), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        db.close()

@routes.route("/voos/<numero_voo>/tripulantes", methods=["POST"])
def adicionar_tripulante_route(numero_voo):
    """
    Adicionar tripulante ao voo
    ---
    tags:
      - Tripulantes
    parameters:
      - in: path
        name: numero_voo
        required: true
        type: string
      - in: body
        name: body
        schema:
          properties:
            nome:
              type: string
            cpf:
              type: string
            cargo:
              type: string
            matricula:
              type: string
    responses:
      200:
        description: Tripulante adicionado
    """
    db = SessionLocal()
    try:
        voo = buscar_voo(db, numero_voo)
        if not voo:
            return jsonify({"erro": "Voo não encontrado"}), 404
        
        data = request.get_json()
        nome = data.get("nome")
        cpf = data.get("cpf")
        cargo = data.get("cargo")
        matricula = data.get("matricula")

        tripulante = Funcionario(cargo, matricula, nome, cpf)
        voo.tripulacao.append(tripulante)

        db.commit()
        db.refresh(voo)

        return jsonify({"mensagem": f"Tripulante {nome} adicionado ao voo {numero_voo}."}), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        db.close()

