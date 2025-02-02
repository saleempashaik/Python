import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SSP\SSP;"
                      "Database=Test;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM branch')

for row in cursor:
    print('row = %r' % (row,))
