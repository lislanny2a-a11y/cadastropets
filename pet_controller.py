from flask import jsonify, request
import models.pet as PetModel

# Criar um pet
def criar_pet():
    dados = request.json
    
    # Verificações simples (validações)
    if "nome" not in dados or dados["nome"] == "":
        return jsonify({"erro": "O nome do pet é obrigatório!"}), 400

    if "idade" not in dados or type(dados["idade"]) != int:
        return jsonify({"erro": "A idade do pet deve ser um número inteiro!"}), 400

    if "tipo" not in dados or dados["tipo"] == "":
        return jsonify({"erro": "O tipo do pet é obrigatório!"}), 400

    # Chamando o model para salvar o pet
    PetModel.criar_pet(dados["nome"], dados["idade"], dados["tipo"], dados.get("dono_id"))
    
    return jsonify({"mensagem": "Pet criado com sucesso!"}), 201


# Listar todos os pets
def listar_pets():
    pets = PetModel.listar_pets()
    return jsonify([dict(pet) for pet in pets]), 200


# Buscar pet por ID
def buscar_pet(id):
    pet = PetModel.buscar_pet_por_id(id)

    if pet:
        return jsonify(dict(pet)), 200
    else:
        return jsonify({"erro": "Pet não encontrado!"}), 404


# Atualizar pet
def atualizar_pet(id):
    dados = request.json
    pet = PetModel.buscar_pet_por_id(id)

    if not pet:
        return jsonify({"erro": "Pet não encontrado!"}), 404

    # Atualiza os dados recebidos
    nome = dados.get("nome", pet["nome"])
    idade = dados.get("idade", pet["idade"])
    tipo = dados.get("tipo", pet["tipo"])

    PetModel.atualizar_pet(id, nome, idade, tipo)

    return jsonify({"mensagem": "Pet atualizado com sucesso!"}), 200


# Deletar pet
def deletar_pet(id):
    pet = PetModel.buscar_pet_por_id(id)

    if not pet:
        return jsonify({"erro": "Pet não encontrado!"}), 404

    PetModel.deletar_pet(id)
    return jsonify({"mensagem": "Pet deletado com sucesso!"}), 200
