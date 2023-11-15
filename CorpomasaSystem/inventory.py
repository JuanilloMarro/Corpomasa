import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabase:

    def __init__(self):
        self.conn = sql.connect("corpomasa.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa (
                codigo integer,
                producto text,
                costo integer,
                precio integer,
                existencia integer
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insertRow(self, codigo, producto, costo, precio, existencia):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa VALUES ({codigo}, '{producto}', {costo}, {precio}, {existencia}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def updateFields(self, codigo, costo, precio, existencia, nombre_producto):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa SET codigo = {codigo} WHERE producto like '{nombre_producto}%'  "
        instruccion_2 = f"UPDATE corpomasa SET costo = {costo} WHERE producto like '{nombre_producto}%'  "
        instruccion_3 = f"UPDATE corpomasa SET precio = {precio} WHERE producto like '{nombre_producto}%'  "
        instruccion_4 = f"UPDATE corpomasa SET existencia = {existencia} WHERE producto like '{nombre_producto}%'  "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        self.conn.commit()

    def deleteRow(self, producto):
        cursor = self.conn.cursor()
        instruccion = f"DELETE FROM corpomasa WHERE producto like '{producto}%'"
        cursor.execute(instruccion)
        self.conn.commit()

    def inventario(self, tableWidget):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa"
        result = cursor.execute(instruccion)
        tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_name(self, codigo):
        cursor = self.conn.cursor()
        instruccion = f"SELECT producto FROM corpomasa Where codigo = {codigo}"
        cursor.execute(instruccion)
        result = cursor.fetchall()
        result = result[0][0]
        return str(result)

    def get_precio(self, codigo):
        cursor = self.conn.cursor()
        instruccion = f"SELECT precio FROM corpomasa Where codigo = {codigo}"
        cursor.execute(instruccion)
        result = cursor.fetchall()
        result_content = result[0][0]
        return int(result_content)

    def get_existencias(self, codigo):
        cursor = self.conn.cursor()
        instruccion = f"SELECT existencia FROM corpomasa Where codigo = {codigo}"
        cursor.execute(instruccion)
        result = cursor.fetchall()
        result_content = result[0][0]
        return int(result_content)

    def updateExistencias(self, codigo, existencia):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa SET existencia = {existencia} WHERE codigo = {codigo} "
        cursor.execute(instruccion)
        self.conn.commit()

    def get_monto(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT precio FROM corpomasa"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)
