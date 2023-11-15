import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import datetime
from inventory import Sqldatabase
from recursos_humanos import Sqldatabaserh
from Ventas import Sqldatabasev
from cuentas_x_cobrar import Sqldatabasecxc
from cuentas_x_pagar import Sqldatabasecxp
from deudas import Sqldatabased
from gastos_fijos import Sqldatabasegj
from intereses import Sqldatabasei
from impuestos import Sqldatabaseimp
from inmobiliario import Sqldatabaseinb
from balance_general import Sqldatabasebg

DataBase = Sqldatabase()
DataBaseRH = Sqldatabaserh()
DataBaseV = Sqldatabasev()
DataBaseCXC = Sqldatabasecxc()
DataBaseCXP = Sqldatabasecxp()
DataBaseD = Sqldatabased()
DataBaseGJ = Sqldatabasegj()
DataBaseI = Sqldatabasei()
DataBaseIMP = Sqldatabaseimp()
DataBaseINB = Sqldatabaseinb()
DataBaseBG = Sqldatabasebg()

time = datetime.datetime.now()
fecha = str(time.strftime('%d/%m/%Y'))
hora = str(time.strftime('%H:%M:%S'))

usuario = 'gerente'
contra = '123'
usuario_v = 'vendedor'
contra_v = '123'
usuario_s = 'supervisor'
contra_s = '123'


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('proyectoTS.ui', self)

        self.btn_principal_inventario.hide()
        self.btn_ventas.hide()
        self.btn_recursos_humanos.hide()
        self.btn_finanzas.hide()
        self.btn_inicio_de_sesion.show()
        self.btn_bienvenido.clicked.connect(self.iniciar_sesion)
        # Botones que modifican la interfaz
        self.btn_minimizar.clicked.connect(self.minimizar)
        self.btn_restaurar.clicked.connect(self.normal)
        self.btn_maximizar.clicked.connect(self.maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())
        # Paginas Inventario
        self.btn_inicio.clicked.connect(self.show_inicio)
        self.btn_principal_inventario.clicked.connect(self.show_page_inventario)
        self.btn_registrar_principal.clicked.connect(self.show_page_registar)
        self.btn_actualizar_principal.clicked.connect(self.show_page_actualizar)
        self.btn_eliminar_principal.clicked.connect(self.show_page_eliminar)
        self.btn_inicio_de_sesion.clicked.connect(self.show_page_iniciar_sesion)
        # Paginas RH
        self.btn_recursos_humanos.clicked.connect(self.show_page_RH)
        self.btn_registrar_rh.clicked.connect(self.show_page_registrar_rh)
        self.btn_actualizar_rh.clicked.connect(self.show_page_actualizar_rh)
        self.btn_eliminar_rh.clicked.connect(self.show_page_eliminar_rh)
        self.btn_plantilla.clicked.connect(self.show_page_planilla)
        # Modificaciones inventario
        self.btn_actualiza_productos.clicked.connect(self.loaddata)
        self.btn_registrar_inventario.clicked.connect(self.registrar_inventario)
        self.btn_actualizar_inventario.clicked.connect(self.actualizar_inventario)
        self.btn_eliminar_inventario.clicked.connect(self.eliminar_inventario)
        # Modificaciones RH
        self.btn_registrar_rh_2.clicked.connect(self.registrar_rh)
        self.btn_actualiza_usuarios_rh.clicked.connect(self.loaddata_rh)
        self.btn_actualiza_usuarios_rh.clicked.connect(self.prueba)
        self.btn_actualizar_info_rh.clicked.connect(self.actualizar_rh)
        self.btn_eliminar_info_rh.clicked.connect(self.eliminar_rh)
        self.btn_actualiza_planilla.clicked.connect(self.loaddata_planilla)
        # Volver
        self.btn_volver.clicked.connect(self.volver)
        self.btn_volver_2.clicked.connect(self.volver)
        self.btn_volver_3.clicked.connect(self.volver)
        # Volver RH
        self.btn_volver_7.clicked.connect(self.volver_2)
        self.btn_volver_8.clicked.connect(self.volver_2)
        self.btn_volver_9.clicked.connect(self.volver_2)
        self.btn_volver_10.clicked.connect(self.volver_2)
        # Ventas
        self.btn_ventas.clicked.connect(self.show_ventas)
        self.btn_volver_11.clicked.connect(self.show_ventas)
        self.btn_detalles_venta.clicked.connect(self.show_detalles_ventas)
        self.btn_actualiza_ventas.clicked.connect(self.loaddata_ventas)
        self.btn.clicked.connect(self.calcular_ventas)
        self.label_fecha.setText(fecha)
        self.label_hora.setText(hora)
        self.btn_pagar.clicked.connect(self.registrar_ventas)
        self.btn_actualizar_detalles.clicked.connect(self.loaddata_detalles)
        self.btn_nueva_venta.clicked.connect(self.nueva_venta)
        # Finanzas
        self.btn_finanzas.clicked.connect(self.show_finanzas)
        self.btn_cuentas_pagar.clicked.connect(self.show_cuenta_pagar)
        self.btn_cuentas_cobrar.clicked.connect(self.show_cuentas_cobrar)
        self.btn_deudas.clicked.connect(self.show_deudas)
        self.btn_gastos_fijos.clicked.connect(self.show_gastos_fijos)
        self.btn_impuestos.clicked.connect(self.show_impuestos)
        self.btn_intereses.clicked.connect(self.show_intereses)
        self.btn_inmobiliario.clicked.connect(self.show_inmobiliario)
        self.btn_actualiza_cuentas_cobrar.clicked.connect(self.loaddata_cxc)
        self.btn_reg_cuentas_cobrar.clicked.connect(self.registrar_cxc)
        self.btn_actu_cuentas_cobrar.clicked.connect(self.actualizar_cxc)
        self.btn_eli_cuentas_cobrar.clicked.connect(self.eliminar_cxc)
        self.btn_actualiza_cuentas_pagar.clicked.connect(self.loaddata_cxp)
        self.btn_reg_cuentas_pagar.clicked.connect(self.registrar_cxp)
        self.btn_actu_cuentas_pagar.clicked.connect(self.actualizar_cxp)
        self.btn_eli_cuentas_pagar.clicked.connect(self.eliminar_cxp)
        self.btn_actualiza_deudas.clicked.connect(self.loaddata_d)
        self.btn_reg_deudas.clicked.connect(self.registrar_d)
        self.btn_actu_deudas.clicked.connect(self.actualizar_d)
        self.btn_eli_deudas.clicked.connect(self.eliminar_d)
        self.btn_actualiza_gastos_fijos.clicked.connect(self.loaddata_gj)
        self.btn_reg_gastos_fijos.clicked.connect(self.registrar_gj)
        self.btn_actu_gastos_fijos.clicked.connect(self.actualizar_gj)
        self.btn_eli_gastos_fijos.clicked.connect(self.eliminar_gj)
        self.btn_actualiza_intereses.clicked.connect(self.loaddata_i)
        self.btn_reg_intereses.clicked.connect(self.registrar_i)
        self.btn_actu_intereses.clicked.connect(self.actualizar_i)
        self.btn_eli_intereses.clicked.connect(self.eliminar_i)
        self.btn_actualiza_impuestos.clicked.connect(self.loaddata_imp)
        self.btn_reg_impuestos.clicked.connect(self.registrar_imp)
        self.btn_actu_impuestos.clicked.connect(self.actualizar_imp)
        self.btn_eli_impuestos.clicked.connect(self.eliminar_imp)
        self.btn_actualiza_inmobiliario.clicked.connect(self.loaddata_inb)
        self.btn_reg_inmobiliario.clicked.connect(self.registrar_inb)
        self.btn_actu_inmobiliario.clicked.connect(self.actualizar_inb)
        self.btn_eli_inmobiliario.clicked.connect(self.eliminar_inb)
        self.btn_actualiza_finanzas.clicked.connect(self.loaddata_bg)

        # Volver finanzas
        self.btn_volver_12.clicked.connect(self.show_finanzas)
        self.btn_volver_14.clicked.connect(self.show_finanzas)
        self.btn_volver_15.clicked.connect(self.show_finanzas)
        self.btn_volver_16.clicked.connect(self.show_finanzas)
        self.btn_volver_17.clicked.connect(self.show_finanzas)
        self.btn_volver_18.clicked.connect(self.show_finanzas)
        self.btn_volver_19.clicked.connect(self.show_finanzas)

    def iniciar_sesion(self):
        usuario_ = str(self.lbl_usuario.text())
        contra_ = str(self.lbl_contrasena.text())
        if usuario_ == usuario and contra_ == contra:
            self.btn_principal_inventario.show()
            self.btn_ventas.show()
            self.btn_recursos_humanos.show()
            self.btn_finanzas.show()
            self.btn_inicio_de_sesion.hide()
            self.stackedWidget.setCurrentWidget(self.page_inicio)
        elif usuario_ == usuario_v and contra_ == contra_v:
            self.btn_ventas.show()
            self.btn_principal_inventario.show()
            self.btn_inicio_de_sesion.hide()
            self.btn_detalles_venta.hide()
            self.btn_registrar_principal.hide()
            self.btn_actualizar_principal.hide()
            self.btn_eliminar_principal.hide()

            self.stackedWidget.setCurrentWidget(self.page_inicio)
        elif usuario_ == usuario_s and contra_ == contra_s:
            self.btn_ventas.show()
            self.btn_principal_inventario.show()
            self.btn_recursos_humanos.show()
            self.btn_finanzas.show()
            self.btn_detalles_venta.show()
            self.btn_inicio_de_sesion.hide()
            self.btn_registrar_principal.hide()
            self.btn_actualizar_principal.hide()
            self.btn_eliminar_principal.hide()
            self.btn_cuentas_cobrar.hide()
            self.btn_cuentas_pagar.hide()
            self.btn_deudas.hide()
            self.btn_gastos_fijos.hide()
            self.btn_intereses.hide()
            self.btn_impuestos.hide()
            self.btn_inmobiliario.hide()
            self.btn_registrar_rh.hide()
            self.btn_actualizar_rh.hide()
            self.btn_eliminar_rh.hide()
            self.label_134.hide()

        else:
            self.label_inicio_de_sesion.setText('Usuario o contraseña incorrectos!')

    def prueba(self):
        self.btn_actualiza_usuarios_rh.setText('Los productos se han cargado')
        self.btn_actualiza_usuarios_rh.setEnabled(True)

    def show_inicio(self):
        self.stackedWidget.setCurrentWidget(self.page_inicio)

    def show_page_inventario(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def show_page_registar(self):
        self.stackedWidget.setCurrentWidget(self.page_registrar)

    def show_page_actualizar(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar)

    def show_page_eliminar(self):
        self.stackedWidget.setCurrentWidget(self.page_eliminar)

    def show_page_iniciar_sesion(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_sesion)

    def show_page_RH(self):
        self.stackedWidget.setCurrentWidget(self.page_recursos_humanos)

    def show_page_registrar_rh(self):
        self.stackedWidget.setCurrentWidget(self.page_registrar_rh)

    def show_page_actualizar_rh(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar_rh)

    def show_page_eliminar_rh(self):
        self.stackedWidget.setCurrentWidget(self.page_eliminar_rh)

    def show_page_planilla(self):
        self.stackedWidget.setCurrentWidget(self.page_planilla)

    def show_ventas(self):
        self.stackedWidget.setCurrentWidget(self.page_ventas)

    def show_detalles_ventas(self):
        self.stackedWidget.setCurrentWidget(self.page_detalles_ventas)

    def show_finanzas(self):
        self.stackedWidget.setCurrentWidget(self.page_finanzas)

    def show_cuenta_pagar(self):
        self.stackedWidget.setCurrentWidget(self.page_cuentas_pagar)

    def show_cuentas_cobrar(self):
        self.stackedWidget.setCurrentWidget(self.page_cuentas_cobrar)

    def show_deudas(self):
        self.stackedWidget.setCurrentWidget(self.page_deudas)

    def show_gastos_fijos(self):
        self.stackedWidget.setCurrentWidget(self.page_gastos_fijos)

    def show_intereses(self):
        self.stackedWidget.setCurrentWidget(self.page_intereses)

    def show_impuestos(self):
        self.stackedWidget.setCurrentWidget(self.page_impuestos)

    def show_inmobiliario(self):
        self.stackedWidget.setCurrentWidget(self.page_inmobiliario)

    def minimizar(self):
        self.showMinimized()

    def normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()

    def volver(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def volver_2(self):
        self.stackedWidget.setCurrentWidget(self.page_recursos_humanos)

    def registrar_inventario(self):
        codigo = int(self.info_codigo.text())
        producto = str(self.info_producto.text())
        costo = int(self.info_costo.text())
        precio = int(self.info_precio.text())
        existencia = int(self.info_existencia.text())
        DataBase.insertRow(codigo, producto, costo, precio, existencia)
        self.label_inventario.setText("Los productos se han registrado con exito :)")
        self.info_codigo.setText(" ")
        self.info_producto.setText(" ")
        self.info_costo.setText(" ")
        self.info_precio.setText(" ")
        self.info_existencia.setText(" ")

    def actualizar_inventario(self):
        codigo = int(self.actu_codigo.text())
        producto = str(self.actu_producto.text())
        costo = int(self.actu_costo.text())
        precio = int(self.actu_precio.text())
        existencia = int(self.actu_existencia.text())
        DataBase.updateFields(codigo, costo, precio, existencia, producto)
        self.label_inventario.setText("Los productos se han actualizado con exito :)")
        self.actu_codigo.setText(" ")
        self.actu_producto.setText(" ")
        self.actu_costo.setText(" ")
        self.actu_precio.setText(" ")
        self.actu_existencia.setText(" ")

    def eliminar_inventario(self):
        producto = str(self.eli_producto.text())
        DataBase.deleteRow(producto)
        self.label_inventario.setText("El productos se ha eliminado con exito :)")
        self.eli_producto.setText(" ")

    def loaddata(self):
        tableWidget = self.tableWidget
        DataBase.inventario(tableWidget)
        self.label_inventario.setText("Los productos se han cargado...")

    def loaddata_rh(self):
        tableWidget_rh = self.tableWidget_rh
        DataBaseRH.recursos_humanos(tableWidget_rh)
        self.label_rh.setText("Los usuarios se han cargado...")

    def loaddata_planilla(self):
        tableWidget_planilla = self.tableWidget_planilla
        DataBaseRH.planilla(tableWidget_planilla)
        self.label_planilla.setText("La planilla se ha cargado...")

    def loaddata_ventas(self):
        tableWidget_fac = self.tableWidget_fac
        DataBase.inventario(tableWidget_fac)
        self.label_ventas.setText("Los productos se han cargado...")

    def loaddata_detalles(self):
        tableWidget_ventas = self.tableWidget_ventas
        DataBaseV.ventas(tableWidget_ventas)
        self.label_detalle_ventas.setText("Se han cargado los detalles de las ventas...")

    def loaddata_cxc(self):
        tableWidget_cxc = self.tableWidget_cxc
        DataBaseCXC.cuentas_por_cobrar(tableWidget_cxc)
        monto_total_cxc = int(DataBaseCXC.get_monto())
        self.label_cxc.setText(str(monto_total_cxc))

    def loaddata_cxp(self):
        tableWidget_cxp = self.tableWidget_cxp
        DataBaseCXP.cuentas_por_pagar(tableWidget_cxp)
        monto_total_cxp = int(DataBaseCXP.get_monto())
        self.label_cxp.setText(str(monto_total_cxp))

    def loaddata_d(self):
        tableWidget_d = self.tableWidget_d
        DataBaseD.deudas(tableWidget_d)
        monto_total_d = int(DataBaseD.get_monto())
        self.label_d.setText(str(monto_total_d))

    def loaddata_gj(self):
        tableWidget_gj = self.tableWidget_gj
        DataBaseGJ.gastos_fijos(tableWidget_gj)
        monto_total_gj = int(DataBaseGJ.get_monto())
        self.label_gj.setText(str(monto_total_gj))

    def loaddata_i(self):
        tableWidget_i = self.tableWidget_i
        DataBaseI.intereses(tableWidget_i)
        monto_total_i = int(DataBaseI.get_monto())
        self.label_i.setText(str(monto_total_i))

    def loaddata_imp(self):
        tableWidget_imp = self.tableWidget_imp
        DataBaseIMP.impuestos(tableWidget_imp)
        monto_total_imp = int(DataBaseIMP.get_monto())
        self.label_imp.setText(str(monto_total_imp))

    def loaddata_inb(self):
        tableWidget_inb = self.tableWidget_inb
        DataBaseINB.inmobiliario(tableWidget_inb)
        monto_total_inb = int(DataBaseINB.get_monto())
        self.label_inb.setText(str(monto_total_inb))

    def loaddata_bg(self):
        tableWidget_finanzas = self.tableWidget_finanzas
        DataBaseBG.balance_general(tableWidget_finanzas)
        monto_total_cxc = int(DataBaseCXC.get_monto())
        monto_total_cxp = int(DataBaseCXP.get_monto())
        monto_total_d = int(DataBaseD.get_monto())
        monto_total_gj = int(DataBaseGJ.get_monto())
        monto_total_i = int(DataBaseI.get_monto())
        monto_total_imp = int(DataBaseIMP.get_monto())
        monto_total_inb = int(DataBaseINB.get_monto())
        monto_total_inv = int(DataBase.get_monto())
        monto_total_v = int(DataBaseV.get_monto())
        monto_total_rh = int(DataBaseRH.get_monto())
        activo = int(DataBaseBG.get_activo())
        pasivo = int(DataBaseBG.get_pasivo())
        total = activo + pasivo
        DataBaseBG.updateFields('Inventario', monto_total_inv, 0)
        DataBaseBG.updateFields('Ventas', monto_total_v, 0)
        DataBaseBG.updateFields('Cuentas por cobrar', monto_total_cxc, 0)
        DataBaseBG.updateFields('Cuentas por pagar', 0, monto_total_cxp)
        DataBaseBG.updateFields('Deudas', 0, monto_total_d)
        DataBaseBG.updateFields('Gastos fijos', 0, monto_total_gj)
        DataBaseBG.updateFields('Intereses', 0, monto_total_i)
        DataBaseBG.updateFields('Impuestos', 0, monto_total_imp)
        DataBaseBG.updateFields('Inmobiliario', monto_total_inb, 0)
        DataBaseBG.updateFields('Planilla', 0, monto_total_rh)
        self.lbl_activo.setText(str(f"Q{activo}"))
        self.lbl_pasivo.setText(str(f"Q{pasivo}"))
        self.lbl_total_finanzas.setText(str(f"Q{total}"))

    def registrar_rh(self):
        nombre = str(self.info_nombre.text())
        apellido = str(self.info_apellido.text())
        genero = str(self.info_genero.currentText())
        edad = int(self.info_edad.text())
        fdn_dia = str(self.fdn_dia.currentText())
        fdn_mes = str(self.fdn_mes.currentText())
        fdn_ano = str(self.fdn_ano.currentText())
        fecha_de_nacimiento = str(f"{fdn_dia} / {fdn_mes} / {fdn_ano}")
        dpi = int(self.info_dpi.text())
        nit = int(self.info_nit.text())
        direccion = str(self.info_direccion.text())
        telefono = int(self.info_telefono.text())
        tipo_de_sangre = str(self.info_sangre.currentText())
        contacto_de_emergencia = int(self.info_cde.text())
        alergico = str(self.info_alergico.text())
        fdil_dia = str(self.fdil_dia.currentText())
        fdil_mes = str(self.fdil_mes.currentText())
        fdil_ano = str(self.fdil_ano.currentText())
        fecha_de_inicio_laboral = str(f"{fdil_dia} / {fdil_mes} / {fdil_ano}")
        puesto = str(self.info_puesto.currentText())
        sueldo = int(self.info_sueldo.text())
        sueldo_quincenal = sueldo / 2
        int(sueldo_quincenal)
        dias_laborados = int(0)
        iggs = int(0.0483 * sueldo)
        horas_extra = int(0)
        total_sueldo = int(sueldo)
        DataBaseRH.insertRow(nombre, apellido, genero, edad, fecha_de_nacimiento, dpi, nit, direccion, telefono,
                             tipo_de_sangre, contacto_de_emergencia, alergico, fecha_de_inicio_laboral, puesto, sueldo,
                             dias_laborados, sueldo_quincenal, iggs, horas_extra, total_sueldo)
        self.label_rh.setText("El usuario se ha registrado con exito :)")
        self.info_nombre.setText(" ")
        self.info_apellido.setText(" ")
        self.info_edad.setText(" ")
        self.info_dpi.setText(" ")
        self.info_nit.setText(" ")
        self.info_direccion.setText(" ")
        self.info_telefono.setText(" ")
        self.info_cde.setText(" ")
        self.info_alergico.setText(" ")
        self.info_sueldo.setText(" ")

    def actualizar_rh(self):
        nombre = str(self.actu_nombre.text())
        apellido = str(self.actu_apellido.text())
        genero = str(self.actu_genero.currentText())
        edad = int(self.actu_edad.text())
        fdn_dia = str(self.fdn_dia_2.currentText())
        fdn_mes = str(self.fdn_mes_2.currentText())
        fdn_ano = str(self.fdn_ano_2.currentText())
        fecha_de_nacimiento = str(f"{fdn_dia} / {fdn_mes} / {fdn_ano}")
        dpi = int(self.actu_dpi.text())
        nit = int(self.actu_nit.text())
        direccion = str(self.actu_direccion.text())
        telefono = int(self.actu_telefono.text())
        tipo_de_sangre = str(self.actu_sangre.currentText())
        contacto_de_emergencia = int(self.actu_cde.text())
        alergico = str(self.actu_alergico.text())
        fdil_dia = str(self.fdil_dia_2.currentText())
        fdil_mes = str(self.fdil_mes_2.currentText())
        fdil_ano = str(self.fdil_ano_2.currentText())
        fecha_de_inicio_laboral = str(f"{fdil_dia} / {fdil_mes} / {fdil_ano}")
        puesto = str(self.actu_puesto.currentText())
        sueldo = int(self.actu_sueldo.text())
        total_sueldo = int(sueldo)
        DataBaseRH.updateFields(nombre, apellido, genero, edad, fecha_de_nacimiento, nit, direccion, telefono,
                                tipo_de_sangre, contacto_de_emergencia, alergico, fecha_de_inicio_laboral, puesto,
                                sueldo, dpi)
        DataBaseRH.updateFieldsP(dpi, sueldo, total_sueldo)
        self.label_rh.setText("Los usuarios se han actualizado con exito :)")
        self.actu_nombre.setText(" ")
        self.actu_apellido.setText(" ")
        self.actu_edad.setText(" ")
        self.actu_dpi.setText(" ")
        self.actu_nit.setText(" ")
        self.actu_direccion.setText(" ")
        self.actu_telefono.setText(" ")
        self.actu_cde.setText(" ")
        self.actu_alergico.setText(" ")
        self.actu_sueldo.setText(" ")

    def eliminar_rh(self):
        dpi = int(self.eli_trabajador.text())
        DataBaseRH.deleteRow(dpi)
        self.eli_trabajador.setText(" ")

    def calcular_ventas(self):
        codigo = int(self.ventas_codigo.text())
        cantidad = int(self.info_cantidad.text())
        precio = DataBase.get_precio(codigo)
        total = precio * cantidad
        existencia = DataBase.get_existencias(codigo)
        existencia_total = existencia - cantidad
        DataBase.updateExistencias(codigo, existencia_total)
        self.label_total.setText(str(total))

    def registrar_ventas(self):
        total = int(self.label_total.text())
        recibido = int(self.info_recibido.text())
        vuelto = recibido - total
        self.label_vuelto.setText(str(vuelto))
        usuario_vendedor = 'Juan Diego'
        codigo = int(self.ventas_codigo.text())
        producto = DataBase.get_name(codigo)
        cantidad = int(self.info_cantidad.text())
        total_registro = int(self.label_total.text())
        DataBaseV.insertRow(usuario_vendedor, fecha, hora, producto, cantidad, total_registro)
        self.label_ventas.setText("Se han registrado con exito :)")

    def nueva_venta(self):
        self.label_total.setText(" ")
        self.label_vuelto.setText(" ")
        self.info_cantidad.setText(" ")
        self.ventas_codigo.setText(" ")
        self.info_recibido.setText(" ")

    def registrar_cxc(self):
        descripcion = str(self.info_descripcion_cxc.text())
        monto = int(self.info_monto_cxc.text())
        DataBaseCXC.insertRow(descripcion, monto)
        self.info_descripcion_cxc.setText(" ")
        self.info_monto_cxc.setText(" ")

    def actualizar_cxc(self):
        descripcion = str(self.actu_descripcion_cxc.text())
        monto = int(self.actu_monto_cxc.text())
        DataBaseCXC.updateFields(descripcion, monto)
        self.actu_descripcion_cxc.setText(" ")
        self.actu_monto_cxc.setText(" ")

    def eliminar_cxc(self):
        descripcion = str(self.eli_descripcion_cxc.text())
        DataBaseCXC.deleteRow(descripcion)
        self.eli_descripcion_cxc.setText(" ")

    def registrar_cxp(self):
        descripcion = str(self.info_descripcion_cxp.text())
        monto = int(self.info_monto_cxp.text())
        DataBaseCXP.insertRow(descripcion, monto)
        self.info_descripcion_cxp.setText(" ")
        self.info_monto_cxp.setText(" ")

    def actualizar_cxp(self):
        descripcion = str(self.actu_descripcion_cxp.text())
        monto = int(self.actu_monto_cxp.text())
        DataBaseCXP.updateFields(descripcion, monto)
        self.info_descripcion_cxp.setText(" ")
        self.info_monto_cxp.setText(" ")

    def eliminar_cxp(self):
        descripcion = str(self.eli_descripcion_cxp.text())
        DataBaseCXP.deleteRow(descripcion)
        self.eli_descripcion_cxp.setText(" ")

    def registrar_d(self):
        descripcion = str(self.info_descripcion_d.text())
        monto = int(self.info_monto_d.text())
        DataBaseD.insertRow(descripcion, monto)
        self.info_descripcion_d.setText(" ")
        self.info_monto_d.setText(" ")

    def actualizar_d(self):
        descripcion = str(self.actu_descripcion_d.text())
        monto = int(self.actu_monto_d.text())
        DataBaseD.updateFields(descripcion, monto)
        self.info_descripcion_d.setText(" ")
        self.info_monto_d.setText(" ")

    def eliminar_d(self):
        descripcion = str(self.eli_descripcion_d.text())
        DataBaseD.deleteRow(descripcion)
        self.eli_descripcion_d.setText(" ")

    def registrar_gj(self):
        descripcion = str(self.info_descripcion_gj.text())
        monto = int(self.info_monto_gj.text())
        DataBaseGJ.insertRow(descripcion, monto)
        self.info_descripcion_gj.setText(" ")
        self.info_monto_gj.setText(" ")

    def actualizar_gj(self):
        descripcion = str(self.actu_descripcion_gj.text())
        monto = int(self.actu_monto_gj.text())
        DataBaseGJ.updateFields(descripcion, monto)
        self.info_descripcion_gj.setText(" ")
        self.info_monto_gj.setText(" ")

    def eliminar_gj(self):
        descripcion = str(self.eli_descripcion_gj.text())
        DataBaseGJ.deleteRow(descripcion)
        self.eli_descripcion_gj.setText(" ")

    def registrar_i(self):
        descripcion = str(self.info_descripcion_i.text())
        monto = int(self.info_monto_i.text())
        DataBaseI.insertRow(descripcion, monto)
        self.info_descripcion_i.setText(" ")
        self.info_monto_i.setText(" ")

    def actualizar_i(self):
        descripcion = str(self.actu_descripcion_i.text())
        monto = int(self.actu_monto_i.text())
        DataBaseI.updateFields(descripcion, monto)
        self.info_descripcion_i.setText(" ")
        self.info_monto_i.setText(" ")

    def eliminar_i(self):
        descripcion = str(self.eli_descripcion_i.text())
        DataBaseI.deleteRow(descripcion)
        self.eli_descripcion_i.setText(" ")

    def registrar_imp(self):
        descripcion = str(self.info_descripcion_imp.text())
        monto = int(self.info_monto_imp.text())
        DataBaseIMP.insertRow(descripcion, monto)
        self.info_descripcion_imp.setText(" ")
        self.info_monto_imp.setText(" ")

    def actualizar_imp(self):
        descripcion = str(self.actu_descripcion_imp.text())
        monto = int(self.actu_monto_imp.text())
        DataBaseIMP.updateFields(descripcion, monto)
        self.info_descripcion_imp.setText(" ")
        self.info_monto_imp.setText(" ")

    def eliminar_imp(self):
        descripcion = str(self.eli_descripcion_imp.text())
        DataBaseIMP.deleteRow(descripcion)
        self.eli_descripcion_imp.setText(" ")

    def registrar_inb(self):
        descripcion = str(self.info_descripcion_inb.text())
        monto = int(self.info_monto_inb.text())
        DataBaseINB.insertRow(descripcion, monto)
        self.info_descripcion_inb.setText(" ")
        self.info_monto_inb.setText(" ")

    def actualizar_inb(self):
        descripcion = str(self.actu_descripcion_inb.text())
        monto = int(self.actu_monto_inb.text())
        DataBaseINB.updateFields(descripcion, monto)
        self.info_descripcion_inb.setText(" ")
        self.info_monto_inbc.setText(" ")

    def eliminar_inb(self):
        descripcion = str(self.eli_descripcion_inb.text())
        DataBaseINB.deleteRow(descripcion)
        self.eli_descripcion_inb.setText(" ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec())
