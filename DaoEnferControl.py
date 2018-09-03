
import sqlite3
from sqlite3 import DatabaseError, ProgrammingError
import pandas as pd

conexao = sqlite3.connect('enfermagem.db')
cursor = conexao.cursor()


def criar_tabela():
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS estudantes (
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL,
           titulo TEXT NOT NULL,
           turma TEXT NOT NULL,
           local TEXT NOT NULL,
           data_inicio DATE NOT NULL,
           data_fim DATE NOT NULL,
           setor TEXT NOT NULL,
           horas INTEGER NOT NULL,
           atividades TEXT NOT NULL
       );
       """)


def registrar_dados(*lista):
    try:
        cursor.execute("""
                    INSERT INTO estudantes (nome, titulo, turma, local, data_inicio, data_fim, setor, horas, atividades)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (*lista,))
        conexao.commit()
        saida = "Seu formulário foi enviado com sucesso!"
    except ProgrammingError:
        saida = "Dados incorretos!"
        raise print("Teste")
    return saida


def consultar_dados(ident):
    try:
        cursor.execute("""
                SELECT * FROM estudantes WHERE id = '%s'
            """%ident)
        for x in cursor.fetchall():
            x = x
        saida = x
    except DatabaseError:
        raise print("Database Error!")
    except ProgrammingError:
        raise print("Programming Error!")
    except BaseException:
        raise print("Erro!")
    return saida


def atualizar_dados(*lista):
    try:
        cursor.execute("""UPDATE estudantes
        SET nome = ?, titulo = ?, turma = ?, local = ?, data_inicio = ?, data_fim = ?, setor = ?, horas = ?, atividades = ?
        WHERE id = ?""", (*lista,))
        conexao.commit()
        saida = "Relatório atualizado com sucesso!"
    except DatabaseError:
        saida = "Impossível atualizar os dados"
    return saida


def imprimir_relatorio():
    cursor.execute("SELECT * FROM estudantes Where id = '%s'"%1)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    writer = pd.ExcelWriter("%s.xlsx"%data[0][1])
    df.to_excel(writer, sheet_name='bar')
    writer.save()


def contar_linhas():
    cursor.execute("""
                    SELECT * from estudantes
                """)
    for x in cursor.description:
        print(x[-1])




