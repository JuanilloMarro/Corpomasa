import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabased:

    def __init__(self):
        self.conn = sql.connect("corpomasa_d.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa_d (
                descripcion text,
                monto integer
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insertRow(self, descripcion, monto):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa_d VALUES ('{descripcion}', {monto}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def updateFields(self, descripcion, monto):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa_d SET monto = {monto} WHERE descripcion like '{descripcion}%'  "
        cursor.execute(instruccion)
        self.conn.commit()

    def deleteRow(self, descripcion):
        cursor = self.conn.cursor()
        instruccion = f"DELETE FROM corpomasa_d WHERE descripcion like '{descripcion}%'"
        cursor.execute(instruccion)
        self.conn.commit()

    def deudas(self, tableWidget_d):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_d"
        result = cursor.execute(instruccion)
        tableWidget_d.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget_d.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget_d.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_monto(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT monto FROM corpomasa_d"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)
