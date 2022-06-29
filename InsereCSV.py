import connection
import pandas as pd

print("\nConectando ao banco...")

cursor, conn = connection.conexao()

print("\nConectado com sucesso! \n")
op = str(input("Deseja inserir no banco [S] [N] ?\n"))
nome_arquivo = str(input("Digite o nome do arquivo para ser inserido -> "))

if op == "S" or op == "s":
    print("Processando...\n")
    data = pd.read_csv (r'csv/' + nome_arquivo + '.csv')   
    df = pd.DataFrame(data)

    for row in df.itertuples():    
        cursor.execute("INSERT INTO usuarios (usuario, senha, acesso) VALUES(?,?,?)", "-", row.email, 4) 
    conn.commit()
    print("\nCSV inserido com sucesso no banco de dados!")
