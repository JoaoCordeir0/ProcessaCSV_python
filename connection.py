def conexao():
    import pyodbc 
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=...;'
                          'Database=...;'
                          'UID=...;'
                          'PWD=...')
    cursor = conn.cursor()
    return cursor, conn