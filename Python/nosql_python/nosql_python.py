from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
import os

HOST_PATH = Path(__file__).parent

load_dotenv(HOST_PATH / ".env")

mongo_uri = os.environ["CONNECTION"]
cliente = MongoClient(mongo_uri)

cliente.get_database()


# ?  CONEXÃO
def conectar(func):
    # connection = f'mongodb+srv://{username}:{senha}@learning.opfeas5.mongodb.net/?retryWrites=true&w=majority&appName=Learning'
    conexao = True
    while conexao:
        conexao = func(cliente)
    cliente.close()


# ? Criação
def criar_db(cliente):
    nome = "destinos"
    cliente._run_operation(f"use {nome}")
    return False


def visualisar_dbs(cliente):
    cliente._run_operation(f"show databases")


# *  `use 'database'`

# ? Criação de um arquivo
# Documento Vazio
# * `db.usuarios.insertOne({})`

# ? Criando uma coleção

# * `db.creareteCollection("destinos")`

# ? Criando Documentos
# * `db.usuarios.insertOne({<chave>:<valor>,<chave>:<valor>,...})`
# * `db.usuarios.insertMany([{<chave>:<valor>,<chave>:<valor>,...},{<chave>:<valor>,<chave>:<valor>,...}])`

# ? Consultas
# retorna todos os dados da collection
# * `db.<coleção>.find({"chave": "valor"})`
# Retorna apenas a primeira referência que localizar, de acordo com o critério de busca
# * `db.<coleção>.findOne({})`
# Encontra e atualiza, (retorna o dado atualizado)
# * `db.<coleção>.findOneAndUpdate({}, {$set: {"chave": "novo_valor"}})`
# Encontra e exclui, (retorna o valor excluido)
# * `db.<coleção>.findOneAndDelete({})`

# ? Updates
# Altera a apenas a primeira referência que localizar
# * `db.<coleção>.updateOne({"<chave>":"<valor>"},{$set: {"<chave>":"<novo_valor>"}})`
# Altera TODAS as correspondências
# Pode adicionar novas COLUNAS à COLEÇÃO
# * `db.<coleção>.updateMany({"<chave>":"<valor>"},{$set: {"<nova_chave>":"<novo_valor>"}})`
# *                                                 $inc: {}
# `$inc:` define um incremento(soma)

# ? Inserindo info em um array
# Inserindo um Array
#                          Busca             operador       valor
# * `db.<coleção>.updateOne({"<chave>":"<valor>"}, {$set: {"<nova_chave>": ["<valor_1>"]}})`
# Inserindo um item no Array já existente
# * `db.<coleção>.updateOne({"<chave>":"<valor>"}, {$push: {"<chave>": ["<valor_2>"]}})`

# ? Excluindo
# Exclui a primeira ocorrência
# * `db.<coleção>.updateOne({"<chave>":"<valor>"})`
# Exclui todas as ocorrências
# * `db.<coleção>.updateMany({"<chave>":"<valor>"})`


# ? Consultas com operações
# IGUALDADE(CasaSensitivy)
# * `db.<coleção>.find({"<chave>":"<valor>"})`

# OPERADORES LÓGICOS
# *`$and`
# *`$or`
# *`$not`

# OPERADORES DE COMPARAÇÃO
#!     MONGO    |   PYTHON
#!-------------------------------
# *     `$eq`    |       ==
# *     `$ne`    |       !=
# *     `$gt`    |       >
# *     `$gte`   |       >=
# *     `$lt`    |       <
# *     `$lte`   |       <=
# *     `$in`    |       in[]
# *     `$nin`   |       not in[]

# ? CONSULTAS NA PRÁTICA

# * condição*n = {<chave>:<valor>}
# Traz os valores com base na condição (AND)
# *`db.<coleção>.find({$and: [{condição1}, {condição2}]})`
# OU

# * `db.<coleção>.find({$and: [{<chave>: {$eq: <valor>}}, {condição2}]})`
# Traz os valor que não são iguais

# * `db.<coleção>.find({<chave>: {$ne:<valor>}})`

# Junção de condições
# * `db.<coleção>.find(
# *     {$or:
# *         [
# *            {
# *                 {$and:
# *                     [
# *                         {<chave>:<valor>},
# *                         {<chave>:<valor>}
# *                     ]
# *                 },
# *
# *             },
# *             {
# *                 {<chave>:<valor>}
# *             }
# *         ]
# *     }
# * )`

# Traz mairo que...
# *`db.<coleção>.find({<valor> : {$gt: <valor>}})`
# Traz mairo/igual que...
# *`db.<coleção>.find({<valor> : {$gte: <valor>}})`

# Traz menor que...
# *`db.<coleção>.find({<valor> : {$lt: <valor>}})`
# Traz menor/igual que...
# *`db.<coleção>.find({<valor> : {$lte: <valor>}})`

# Traz o que NÃO é (retorna todos menos registros que não forem conforme o parâmetro)
# *`db.<coleção>.find({<chave>:{$ne:<valor>}})`
# OU
# *`db.<coleção>.find({<chave>: {$not: {$eq: <valor>}}})`

# Traz resultados de diversas buscas da lista
# *`db.<coleção>.find({<chave>: {$in:[<valor_1>, <valor_2>]}})`
# Traz o que não estiver na lista
# *`db.<coleção>.find({<chave>: {$nin:[<valor_1>, <valor_2>]}})`

# ? PROJEÇÃO
# Retorna somente o campo solicitado
#                                                            (*         *         *)
# *db.<coleções>.find({<chave>: {$nin:[<valor_1>, <valor_2>]}}, {<campo_desejado>:1})

# ? ORDENAÇÃO
# Ordena do menor para o maior
# * `db.<coleção>.find({}).sort(<chave> : 1)`
# Ordena do maior para o menor
# * `db.<coleção>.find({}).sort(<chave> : -1)`

# ? LIMITE
# Limita quantos dados resultados irá trazer
# * `db.<coleção>.find({}).limite(n)`
