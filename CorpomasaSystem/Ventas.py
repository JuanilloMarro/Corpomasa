import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabasev:

    def __init__(self):
        self.conn = sql.connect("corpomasa_v.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa_v (
                usuario text,
                fecha text,
                hora text,
                producto text,
                cantidad integer,
                total integer
            )""")
        self.conn.commit()
        self.conn.close()

    def insertRow(self, usuario, fecha, hora, producto, cantidad, total):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa_v VALUES ('{usuario}', '{fecha}', '{hora}','{producto}', {cantidad}, " \
                      f"{total}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def ventas(self, tableWidget_ventas):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_v"
        result = cursor.execute(instruccion)
        tableWidget_ventas.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget_ventas.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget_ventas.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_monto(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT total FROM corpomasa_v"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)
