import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabasebg:

    def __init__(self):
        self.conn = sql.connect("corpomasa_bg.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa_bg (
                descripcion text,
                activo integer,
                pasivo integer
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insertRow(self, descripcion, activo, pasivo):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa_bg VALUES ('{descripcion}', {activo}, {pasivo}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def updateFields(self, descripcion, activo, pasivo):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa_bg SET activo = {activo} WHERE descripcion like '{descripcion}%' "
        instruccion_2 = f"UPDATE corpomasa_bg SET pasivo = {pasivo} WHERE descripcion like '{descripcion}%' "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        self.conn.commit()

    def balance_general(self, tableWidget_finanzas):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_bg"
        result = cursor.execute(instruccion)
        tableWidget_finanzas.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget_finanzas.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget_finanzas.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_activo(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT activo FROM corpomasa_bg"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)

    def get_pasivo(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT pasivo FROM corpomasa_bg"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)