import sqlite3 as sql
from PyQt5 import QtWidgets


class Sqldatabaserh:

    def __init__(self):
        self.conn = sql.connect("corpomasa_rh.db")

    def createDB(self):
        self.conn.commit()
        self.conn.close()

    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE corpomasa_rh (
                nombre text,
                apellido text,
                genero text,
                edad integer,
                fecha_de_nacimiento integer,
                dpi integer,
                nit integer,
                direccion text,
                telefono integer,
                tipo_de_sangre text,
                contacto_de_emergencia integer,
                alergico text,
                fecha_de_inicio_laboral text,
                puesto text,
                sueldo integer,
                dias_laborados integer,
                sueldo_quincenal integer,
                iggs integer,
                horas_extra integer,
                total integer
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def insertRow(self, nombre, apellido, genero, edad, fecha_de_nacimiento, dpi, nit, direccion, telefono,
                  tipo_de_sangre, contacto_de_emergencia, alergico, fecha_de_inicio_laboral, puesto, sueldo,
                  dias_laborados, sueldo_quincenal, iggs, horas_extra, total):
        cursor = self.conn.cursor()
        instruccion = f"INSERT INTO corpomasa_rh VALUES ('{nombre}', '{apellido}', '{genero}', {edad}, " \
                      f"'{fecha_de_nacimiento}', {dpi}, {nit}, '{direccion}', {telefono}, '{tipo_de_sangre}', " \
                      f"{contacto_de_emergencia}, '{alergico}', '{fecha_de_inicio_laboral}', '{puesto}', {sueldo}, " \
                      f"{dias_laborados}, {sueldo_quincenal}, {iggs}, {horas_extra}, {total}) "
        cursor.execute(instruccion)
        self.conn.commit()

    def updateFields(self, nombre, apellido, genero, edad, fecha_de_nacimiento, nit, direccion, telefono,
                     tipo_de_sangre, contacto_de_emergencia, alergico, fecha_de_inicio_laboral, puesto,
                     sueldo, dpi):
        cursor = self.conn.cursor()
        instruccion = f"UPDATE corpomasa_rh SET nombre = '{nombre}' WHERE dpi = {dpi} "
        instruccion_2 = f"UPDATE corpomasa_rh SET apellido = '{apellido}' WHERE dpi = {dpi} "
        instruccion_3 = f"UPDATE corpomasa_rh SET genero = '{genero}' WHERE dpi = {dpi} "
        instruccion_4 = f"UPDATE corpomasa_rh SET edad = {edad} WHERE dpi = {dpi} "
        instruccion_5 = f"UPDATE corpomasa_rh SET fecha_de_nacimiento = '{fecha_de_nacimiento}' WHERE dpi = {dpi} "
        instruccion_6 = f"UPDATE corpomasa_rh SET nit = {nit} WHERE dpi = {dpi} "
        instruccion_7 = f"UPDATE corpomasa_rh SET direccion = '{direccion}' WHERE dpi = {dpi} "
        instruccion_8 = f"UPDATE corpomasa_rh SET telefono = {telefono} WHERE dpi = {dpi} "
        instruccion_9 = f"UPDATE corpomasa_rh SET tipo_de_sangre = '{tipo_de_sangre}' WHERE dpi = {dpi} "
        instruccion_10 = f"UPDATE corpomasa_rh SET contacto_de_emergencia = {contacto_de_emergencia} WHERE dpi = " \
                         f"{dpi} "
        instruccion_11 = f"UPDATE corpomasa_rh SET alergico = '{alergico}' WHERE dpi = {dpi} "
        instruccion_12 = f"UPDATE corpomasa_rh SET fecha_de_inicio_laboral = '{fecha_de_inicio_laboral}' WHERE dpi =" \
                         f"{dpi} "
        instruccion_13 = f"UPDATE corpomasa_rh SET puesto = '{puesto}' WHERE dpi = {dpi} "
        instruccion_14 = f"UPDATE corpomasa_rh SET sueldo = {sueldo} WHERE dpi = {dpi} "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)
        cursor.execute(instruccion_4)
        cursor.execute(instruccion_5)
        cursor.execute(instruccion_6)
        cursor.execute(instruccion_7)
        cursor.execute(instruccion_8)
        cursor.execute(instruccion_9)
        cursor.execute(instruccion_10)
        cursor.execute(instruccion_11)
        cursor.execute(instruccion_12)
        cursor.execute(instruccion_13)
        cursor.execute(instruccion_14)
        self.conn.commit()

    def deleteRow(self, dpi):
        cursor = self.conn.cursor()
        instruccion = f"DELETE FROM corpomasa_rh WHERE dpi = {dpi}"
        cursor.execute(instruccion)
        self.conn.commit()

    def recursos_humanos(self, tableWidget_rh):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_rh"
        result = cursor.execute(instruccion)
        tableWidget_rh.setRowCount(0)

        for row_number, row_data in enumerate(result):
            tableWidget_rh.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidget_rh.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def planilla(self, tableWidget_planilla):
        cursor = self.conn.cursor()
        instruccion = "SELECT * FROM corpomasa_rh LIMIT 100"
        tableWidget_planilla.setRowCount(100)
        tablerow = 0

        for row in cursor.execute(instruccion):
            tableWidget_planilla.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            tableWidget_planilla.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[12])))
            tableWidget_planilla.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[13])))
            tableWidget_planilla.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[14])))
            tableWidget_planilla.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[15])))
            tableWidget_planilla.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[16])))
            tableWidget_planilla.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[17])))
            tableWidget_planilla.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[18])))
            tableWidget_planilla.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[19])))
            tablerow += 1
        cursor.close()

    def updateFieldsP(self, dpi, sueldo, total):
        cursor = self.conn.cursor()
        sueldo_quincenal = sueldo / 2
        iggs = 0.0483 * sueldo
        instruccion = f"UPDATE corpomasa_rh SET sueldo_quincenal = {sueldo_quincenal} WHERE dpi = {dpi} "
        instruccion_2 = f"UPDATE corpomasa_rh SET iggs = {iggs} WHERE dpi = {dpi} "
        instruccion_3 = f"UPDATE corpomasa_rh SET total = {total} WHERE dpi = {dpi} "
        cursor.execute(instruccion)
        cursor.execute(instruccion_2)
        cursor.execute(instruccion_3)

    def get_monto(self):
        cursor = self.conn.cursor()
        instruccion = "SELECT total FROM corpomasa_rh"
        result = cursor.execute(instruccion)
        monto_total = 0

        for result in enumerate(result):
            result_content = result[1][0]
            monto_total += int(result_content)

        return int(monto_total)
