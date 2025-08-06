# tests/routes/test_voo_completo.py
from app.tests.limpar_tabelas import limpar_database
from app.database.session import SessionLocal

db = SessionLocal()

def test_fluxo_voo_completo(client):
    # Criar companhia
    limpar_database(db)
    resp = client.post("/companhias", params={"nome": "Blue"})
    assert resp.status_code == 201
    companhia_id = resp.json()["id"]

    # Criar aeronave
    resp = client.post("/aeronaves", json={"modelo": "Falcon", "capacidade": 400})
    assert resp.status_code == 200
    aeronave_id = resp.json()["id"]

    # Criar voo
    resp = client.post("/voos", json={
        "numero_voo": "AZ123",
        "origem": "GRU",
        "destino": "REC",
        "aeronave_id": aeronave_id
    })
    assert resp.status_code == 201
    voo = resp.json()
    assert voo["numero_voo"] == "AZ123"

    # Adicionar voo à companhia
    resp = client.post(f"/companhias/{companhia_id}/voos", json={
        "numero_voo": "AZ123",
        "origem": "GRU",
        "destino": "REC",
        "aeronave_id": aeronave_id
    })
    assert resp.status_code == 201

    # Criar passageiro
    resp = client.post("/passageiros", params={"nome": "Carlos", "cpf": "00011122233"})
    assert resp.status_code == 201
    passageiro_id = resp.json()["id"]

    # Adicionar passageiro ao voo
    resp = client.post(f"/voos/AZ123/passageiro/00011122233")
    assert resp.status_code == 200

    # Adicionar bagagem
    resp = client.post(f"/passageiros/00011122233/bagagem)", params={
        "descricao": "Mala 23kg",
        "peso": 23.0
    })
    assert resp.status_code == 200
    bagagem = resp.json()
    assert bagagem["peso"] == 23.0

    # Verificar listagem de passageiros no voo
    resp = client.get(f"/voos/AZ123/passageiros")
    assert resp.status_code == 200
    passageiros = resp.json()
    assert any(p["cpf"] == "00011122233" for p in passageiros)

    # Verificar bagagens do passageiro
    resp = client.get(f"/voos/AZ123/00011122233/bagagens")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

    # Deletar passageiro
    resp = client.delete(f"/voos/AZ123/00011122233")
    assert resp.status_code == 204

    # Verificar que o passageiro não está mais no voo
    resp = client.get(f"/voos/AZ123/passageiros")
    assert resp.status_code == 404
