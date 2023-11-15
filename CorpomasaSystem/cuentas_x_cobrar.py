import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabasecxc:

    def __init__(self):
        self.conn = sql.connect("corpomasa_cxc.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa_cxc (
                descripcion text,
                monto integer
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insertRow(self, descripcion, monto):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa_cxc VALUES ('{descripcion}', {monto}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def updateFields(self, descripcion, monto):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa_cxc SET monto = {monto} WHERE descripcion like '{descripcion}%'  "
        cursor.execute(instruccion)
        self.conn.commit()

    def deleteRow(self, descripcion):
        cursor = self.conn.cursor()
        instruccion = f"DELETE FROM corpomasa_cxc WHERE descripcion like '{descripcion}%'"
        cursor.execute(instruccion)
        self.conn.commit()

    def cuentas_por_cobrar(self, tableWidget_cxc):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_cxc"
        result = cursor.execute(instruccion)
        tableWidget_cxc.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget_cxc.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget_cxc.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_monto(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT monto FROM corpomasa_cxc"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)

