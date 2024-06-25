import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

# Conectando:
conexao = sqlite3.connect(ROOT_PATH / "db" / "meu_banco.sqlite")

# Cursor:
cursor = conexao.cursor()

# Converte a saída para dict ao invés de (tupla,)
cursor.row_factory = sqlite3.Row


# Criando uma tabela
def criar_tabela(conexao, cursor):
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome VARCHAR(100), 
        email VARCHAR(150))"""
    )
    conexao.commit()


# Inserindo dados em uma tabela
def inserir_registro(conexao, cursor, nome, email):
    dados = (nome, email)
    cursor.execute(
        f"""
        INSERT INTO clientes (nome, email)
        VALUES (?,?)""",
        dados,
    )
    # Faz a inserção dos dados, se não houver não realiza a operação de inserção.
    conexao.commit()


# Update
def atualizar_registro(conexao, cursor, nome, email, id):
    dados = (nome, email, id)
    cursor.execute(
        """
    UPDATE clientes 
    SET nome = ?,
    email = ? 
    WHERE id = ?;
    """,
        dados,
    )
    conexao.commit()


# Exlusão
def excluir_registro(conexao, cursor, id):
    dados = (id,)
    cursor.execute(
        """
    DELETE FROM clientes  
    WHERE id = ?;
    """,
        dados,
    )
    conexao.commit()


# Inserindo vários dados
def inserir_muitos(conexao, cursor):
    dados = [
        ("Elizete", "elizlurena@gmail.com"),
        ("Renato", "ranaugusto.ra@gmail.com"),
        ("Rick", "drunkrick@gmail.com"),
        ("Morty", "morty_smith@gmail.com"),
        ("Summer", "summer_smith@gmail.com"),
    ]

    cursor.executemany(
        """
    INSERT INTO clientes (nome, email)
    VALUES(?,?);
    """,
        dados,
    )
    conexao.commit()


# Consultas
def consultar_cliente(cursor, id):
    cursor.execute(
        """
    SELECT * FROM clientes 
    WHERE id=?;""",
        (id,),
    )
    # Retorn uma tupla com todos as colunas
    return cursor.fetchone()


# ROW
def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")
    return cursor.fetchone()


# BOAS PRÁTICAS
# EVITANDO *SQL INJECTION*

# *Não utilizar:
#! consulta_sql = cursor.execute('SELECT * FROM <tabela> WHERE id = ' + str(id))


# *Utilizar ao invés
# ? consulta_sql = cursor.execute('SELECT * FROM <tabela> WHERE id = ?' , (id,))
def consulta_vulneravel(cursor):
    id_cliente = input("Entrecom o id do cliente: ")
    cursor.execute(
        f"""
    SELECT * FROM clientes 
    WHERE id={id_cliente};"""
    )
    return cursor.fetchall()
    # * O USUÁRIO PODE ENTRAR COM O COMANDO A BAIXO, POR EXEMPLO:
    #! 1' OR 1=1; DROP DATABASE;


# Gerenciamento
def insere_com_gerenciamento(conexao, cursor):
    # Se algo der erro antes do commit, não será efetuado nenhuma operação
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES('Teste1', teste1@gmail.com)"
        )
        cursor.execute(
            "INSERT INTO clientes (id, nome, email) VALUES(2, 'Teste2', teste2@gmail.com)"
        )
        cursor.execute("DELETE FROM clientes WHERE id = 1")
        conexao.commit()
    except Exception as error:
        print(f"[ERRO]: {error}\nNão foi possível realizar a operação")
        # Retorna todas operações
        conexao.rollback()


if __name__ == "__main__":
    # #ROW
    # cliente = listar_clientes(cursor)
    # cliente_dict = dict(cliente)
    # print(cliente_dict["nome"])
    # for row in cliente:
    #     print(row)
    pass
