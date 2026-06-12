"""
pf_Algoritmos - PrestaFácil: Gestor de Préstamos
Proyecto Integrador Algoritmia y Programación 2026-1
Universidad de Antioquia - Facultad de Ingeniería
Profesora: Cindy Estrada
"""

import os
import csv
import json
import re
import random
import string
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# CLASE: clsUsuarios
# ─────────────────────────────────────────────
class clsUsuarios:
    """
    pf_Algoritmos - Clase que representa un usuario del sistema PrestaFácil.
    Almacena información personal y tiempo de préstamo autorizado.
    """

    TIEMPOS_PERMITIDOS = [5, 10, 15, 30]

    def __init__(self, nombre: str, apellido: str, documento: str, correo: str, tiempo_prestamo: int):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.tiempo_prestamo = tiempo_prestamo

    # ── Validaciones ──────────────────────────
    @staticmethod
    def validar_nombre(nombre: str) -> tuple[bool, str]:
        """pf_Algoritmos - Valida que el nombre/apellido tenga al menos 3 letras y no contenga números."""
        if len(nombre) < 3:
            return False, "El nombre/apellido debe tener al menos 3 caracteres."
        if any(c.isdigit() for c in nombre):
            return False, "El nombre/apellido no puede contener números."
        return True, ""

    @staticmethod
    def validar_documento(doc: str) -> tuple[bool, str]:
        """pf_Algoritmos - Valida que el documento tenga entre 3 y 15 dígitos numéricos."""
        if not doc.isdigit():
            return False, "El documento solo puede contener números."
        if not (3 <= len(doc) <= 15):
            return False, "El documento debe tener entre 3 y 15 dígitos."
        return True, ""

    @staticmethod
    def validar_correo(correo: str) -> tuple[bool, str]:
        """pf_Algoritmos - Valida formato básico de correo electrónico."""
        patron = r'^[^@]+@[^@]+\.[^@]*com$'
        if not re.match(patron, correo):
            return False, "Correo inválido. Debe contener '@' y terminar en '.com'."
        return True, ""

    @staticmethod
    def validar_tiempo(tiempo: int) -> tuple[bool, str]:
        """pf_Algoritmos - Valida que el tiempo de préstamo sea uno de los valores permitidos."""
        if tiempo not in clsUsuarios.TIEMPOS_PERMITIDOS:
            return False, f"Tiempo inválido. Opciones: {clsUsuarios.TIEMPOS_PERMITIDOS}"
        return True, ""

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "documento": self.documento,
            "correo": self.correo,
            "tiempo_prestamo": self.tiempo_prestamo
        }

    @staticmethod
    def from_dict(d: dict) -> "clsUsuarios":
        return clsUsuarios(d["nombre"], d["apellido"], d["documento"], d["correo"], int(d["tiempo_prestamo"]))


# ─────────────────────────────────────────────
# CLASE: clsPrestamo
# ─────────────────────────────────────────────
class clsPrestamo:
    """
    pf_Algoritmos - Clase que representa un préstamo en el sistema PrestaFácil.
    Gestiona fechas, estado y cálculo de vencimientos.
    """

    CATEGORIAS = {
        "1": "VJ",   # Videojuegos
        "2": "LB",   # Libros
        "3": "MV",   # Música y video
        "4": "HE",   # Herramientas
        "5": "DN",   # Dinero
        "6": "MS"    # Misceláneo y varios
    }
    CATEGORIAS_NOMBRES = {
        "1": "Videojuegos",
        "2": "Libros",
        "3": "Música y video",
        "4": "Herramientas",
        "5": "Dinero",
        "6": "Misceláneo y varios"
    }
    ESTADOS_FUZZY = {
        "1": ("Excelente", 1.0),
        "2": ("Bueno", 0.75),
        "3": ("Regular", 0.5),
        "4": ("Malo", 0.25),
        "5": ("Deteriorado", 0.1)
    }

    def __init__(self, id_item: str, nombre_item: str, categoria: str, precio: float,
                 estado: str, documento_usuario: str, fecha_prestamo: str, activo: bool = True,
                 fecha_devolucion: str = ""):
        self.id_item = id_item
        self.nombre_item = nombre_item
        self.categoria = categoria
        self.precio = precio
        self.estado = estado
        self.documento_usuario = documento_usuario
        self.fecha_prestamo = fecha_prestamo
        self.activo = activo
        self.fecha_devolucion = fecha_devolucion

    @staticmethod
    def generar_id(categoria_codigo: str) -> str:
        """pf_Algoritmos - Genera un ID único basado en la categoría + caracteres aleatorios."""
        prefijo = clsPrestamo.CATEGORIAS.get(categoria_codigo, "XX")
        sufijo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"{prefijo}-{sufijo}"

    def dias_prestado(self) -> int:
        """pf_Algoritmos - Calcula cuántos días lleva prestado el ítem."""
        fecha = datetime.strptime(self.fecha_prestamo, "%Y-%m-%d")
        return (datetime.today() - fecha).days

    def to_dict(self) -> dict:
        return {
            "id_item": self.id_item,
            "nombre_item": self.nombre_item,
            "categoria": self.categoria,
            "precio": self.precio,
            "estado": self.estado,
            "documento_usuario": self.documento_usuario,
            "fecha_prestamo": self.fecha_prestamo,
            "activo": self.activo,
            "fecha_devolucion": self.fecha_devolucion
        }

    @staticmethod
    def from_dict(d: dict) -> "clsPrestamo":
        return clsPrestamo(
            d["id_item"], d["nombre_item"], d["categoria"], float(d["precio"]),
            d["estado"], d["documento_usuario"], d["fecha_prestamo"],
            d["activo"] if isinstance(d["activo"], bool) else d["activo"] == "True",
            d.get("fecha_devolucion", "")
        )


# ─────────────────────────────────────────────
# GESTIÓN DE ARCHIVOS
# ─────────────────────────────────────────────
RUTA_USUARIOS  = os.path.join("data", "usuarios.json")
RUTA_PRESTAMOS = os.path.join("data", "prestamos.json")
RUTA_ADMINS    = os.path.join("data", "admins.json")
RUTA_DOCS      = "doc"

def _cargar_json(ruta: str) -> list:
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def _guardar_json(ruta: str, datos: list):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

def cargar_usuarios() -> list[clsUsuarios]:
    return [clsUsuarios.from_dict(d) for d in _cargar_json(RUTA_USUARIOS)]

def guardar_usuarios(usuarios: list[clsUsuarios]):
    _guardar_json(RUTA_USUARIOS, [u.to_dict() for u in usuarios])

def cargar_prestamos() -> list[clsPrestamo]:
    return [clsPrestamo.from_dict(d) for d in _cargar_json(RUTA_PRESTAMOS)]

def guardar_prestamos(prestamos: list[clsPrestamo]):
    _guardar_json(RUTA_PRESTAMOS, [p.to_dict() for p in prestamos])

def cargar_admins() -> dict:
    datos = _cargar_json(RUTA_ADMINS)
    if not datos:
        # Admin por defecto
        admin_default = [{"usuario": "admin", "clave": "1234"}]
        _guardar_json(RUTA_ADMINS, admin_default)
        return {a["usuario"]: a["clave"] for a in admin_default}
    return {a["usuario"]: a["clave"] for a in datos}

def exportar_csv():
    """pf_Algoritmos - Exporta préstamos activos a CSV."""
    prestamos = cargar_prestamos()
    ruta_csv = os.path.join("data", "prestamos_export.csv")
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id_item","nombre_item","categoria","precio","estado","documento_usuario","fecha_prestamo","activo","fecha_devolucion"])
        writer.writeheader()
        writer.writerows([p.to_dict() for p in prestamos])
    print(f"\n  ✔ CSV exportado en: {ruta_csv}")


# ─────────────────────────────────────────────
# UTILIDADES DE CONSOLA
# ─────────────────────────────────────────────
VERDE  = "\033[92m"
ROJO   = "\033[91m"
CYAN   = "\033[96m"
AMARILLO = "\033[93m"
RESET  = "\033[0m"
NEGRITA = "\033[1m"

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    limpiar()
    print(CYAN + NEGRITA)
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║   ██████╗ ██████╗ ███████╗███████╗████████╗ █████╗  ║")
    print("  ║   ██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗ ║")
    print("  ║   ██████╔╝██████╔╝█████╗  ███████╗   ██║   ███████║ ║")
    print("  ║   ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║ ║")
    print("  ║   ██║     ██║  ██║███████╗███████║   ██║   ██║  ██║ ║")
    print("  ║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ║")
    print("  ║          F Á C I L  -  Gestor  de  Préstamos         ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    print(RESET)

def separador():
    print(CYAN + "  " + "─" * 56 + RESET)

def ok(msg):  print(f"  {VERDE}✔ {msg}{RESET}")
def error(msg): print(f"  {ROJO}✘ {msg}{RESET}")
def info(msg):  print(f"  {AMARILLO}ℹ {msg}{RESET}")

def pedir(prompt: str) -> str:
    return input(f"  {CYAN}► {prompt}: {RESET}").strip()

def menu_principal():
    banner()
    print(f"  {NEGRITA}Bienvenido a PrestaFácil{RESET}\n")
    opciones = [
        "1. Registrar Usuario",
        "2. Registrar Ítem",
        "3. Registrar Préstamo",
        "4. Registrar Devolución",
        "5. Consultar ítems con más de 30 días",
        "6. Consultar Artículos Prestados",
        "7. Administrador",
        "8. Salir"
    ]
    for o in opciones:
        print(f"  {o}")
    separador()
    return pedir("Seleccione una opción")


# ─────────────────────────────────────────────
# MÓDULO 1: REGISTRAR USUARIO
# ─────────────────────────────────────────────
def registrar_usuario():
    banner()
    print(f"  {NEGRITA}── REGISTRAR USUARIO ──{RESET}\n")
    usuarios = cargar_usuarios()

    # Nombre
    while True:
        nombre = pedir("Nombre")
        ok_val, msg = clsUsuarios.validar_nombre(nombre)
        if ok_val: break
        error(msg)

    # Apellido
    while True:
        apellido = pedir("Apellido")
        ok_val, msg = clsUsuarios.validar_nombre(apellido)
        if ok_val: break
        error(msg)

    # Documento
    while True:
        doc = pedir("Documento (solo números, 3-15 dígitos)")
        ok_val, msg = clsUsuarios.validar_documento(doc)
        if ok_val: break
        error(msg)
    if any(u.documento == doc for u in usuarios):
        error("El documento ya está registrado.")
        input("  Presione Enter para continuar...")
        return

    # Correo
    while True:
        correo = pedir("Correo electrónico")
        ok_val, msg = clsUsuarios.validar_correo(correo)
        if ok_val: break
        error(msg)

    # Tiempo de préstamo
    while True:
        info(f"Tiempos permitidos: {clsUsuarios.TIEMPOS_PERMITIDOS} días")
        try:
            tiempo = int(pedir("Tiempo de préstamo (días)"))
            ok_val, msg = clsUsuarios.validar_tiempo(tiempo)
            if ok_val: break
            error(msg)
        except ValueError:
            error("Ingrese un número válido.")

    nuevo = clsUsuarios(nombre, apellido, doc, correo, tiempo)
    usuarios.append(nuevo)
    guardar_usuarios(usuarios)
    ok(f"Usuario '{nombre} {apellido}' registrado exitosamente.")
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 2: REGISTRAR ÍTEM
# ─────────────────────────────────────────────
def registrar_item():
    banner()
    print(f"  {NEGRITA}── REGISTRAR ÍTEM ──{RESET}\n")

    # Nombre del ítem (puede tener números)
    while True:
        nombre = pedir("Nombre del ítem")
        if len(nombre) < 3:
            error("El nombre debe tener al menos 3 caracteres.")
        else:
            break

    # Categoría
    print()
    for k, v in clsPrestamo.CATEGORIAS_NOMBRES.items():
        print(f"  {k}. {v}")
    while True:
        cat = pedir("Seleccione categoría")
        if cat in clsPrestamo.CATEGORIAS:
            break
        error("Categoría inválida.")

    # Precio
    while True:
        try:
            precio = float(pedir("Precio de compra ($)"))
            if precio < 0: raise ValueError
            break
        except ValueError:
            error("Ingrese un precio válido.")

    # Estado (lógica difusa)
    print()
    info("Estado del ítem (lógica difusa):")
    for k, (nombre_estado, valor) in clsPrestamo.ESTADOS_FUZZY.items():
        print(f"  {k}. {nombre_estado} (μ={valor})")
    while True:
        est = pedir("Seleccione estado")
        if est in clsPrestamo.ESTADOS_FUZZY:
            break
        error("Estado inválido.")
    estado_nombre = clsPrestamo.ESTADOS_FUZZY[est][0]

    # Generar ID
    id_item = clsPrestamo.generar_id(cat)
    ok(f"ID generado: {id_item}")

    # Guardar como ítem disponible (préstamo sin usuario asignado aún)
    prestamos = cargar_prestamos()
    nuevo_item = clsPrestamo(
        id_item=id_item,
        nombre_item=nombre,
        categoria=clsPrestamo.CATEGORIAS_NOMBRES[cat],
        precio=precio,
        estado=estado_nombre,
        documento_usuario="",
        fecha_prestamo="",
        activo=False
    )
    prestamos.append(nuevo_item)
    guardar_prestamos(prestamos)
    ok(f"Ítem '{nombre}' registrado con ID {id_item}.")
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 3: REGISTRAR PRÉSTAMO
# ─────────────────────────────────────────────
def registrar_prestamo():
    banner()
    print(f"  {NEGRITA}── REGISTRAR PRÉSTAMO ──{RESET}\n")
    usuarios  = cargar_usuarios()
    prestamos = cargar_prestamos()

    # Listar ítems disponibles
    disponibles = [p for p in prestamos if not p.activo and p.documento_usuario == ""]
    if not disponibles:
        info("No hay ítems disponibles para prestar.")
        input("  Presione Enter para continuar...")
        return

    print(f"  {'ID':<12} {'Nombre':<20} {'Categoría':<18} {'Precio':>10}  {'Estado'}")
    separador()
    for item in disponibles:
        print(f"  {item.id_item:<12} {item.nombre_item:<20} {item.categoria:<18} ${item.precio:>9,.0f}  {item.estado}")
    separador()

    id_sel = pedir("ID del ítem a prestar").upper()
    item_sel = next((p for p in disponibles if p.id_item == id_sel), None)
    if not item_sel:
        error("ID no encontrado.")
        input("  Presione Enter para continuar...")
        return

    doc = pedir("Documento del usuario a quien se presta")
    usuario = next((u for u in usuarios if u.documento == doc), None)
    if not usuario:
        error("Usuario no encontrado. Debe registrarlo primero (Opción 1).")
        input("  Presione Enter para continuar...")
        return

    # Activar préstamo
    for p in prestamos:
        if p.id_item == id_sel:
            p.documento_usuario = doc
            p.fecha_prestamo = datetime.today().strftime("%Y-%m-%d")
            p.activo = True
            break

    guardar_prestamos(prestamos)
    ok(f"Préstamo registrado: {item_sel.nombre_item} → {usuario.nombre} {usuario.apellido}")
    info(f"Fecha: {datetime.today().strftime('%Y-%m-%d')} | Tiempo máx: {usuario.tiempo_prestamo} días")
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 4: REGISTRAR DEVOLUCIÓN
# ─────────────────────────────────────────────
def registrar_devolucion():
    banner()
    print(f"  {NEGRITA}── REGISTRAR DEVOLUCIÓN ──{RESET}\n")
    usuarios  = cargar_usuarios()
    prestamos = cargar_prestamos()

    doc = pedir("Documento del usuario")
    usuario = next((u for u in usuarios if u.documento == doc), None)
    if not usuario:
        error("Usuario no encontrado.")
        input("  Presione Enter para continuar...")
        return

    activos = [p for p in prestamos if p.documento_usuario == doc and p.activo]
    if not activos:
        error(f"El usuario {usuario.nombre} no tiene préstamos activos.")
        input("  Presione Enter para continuar...")
        return

    print(f"\n  {'ID':<12} {'Nombre':<20} {'Fecha préstamo':<16} {'Días'}")
    separador()
    for p in activos:
        print(f"  {p.id_item:<12} {p.nombre_item:<20} {p.fecha_prestamo:<16} {p.dias_prestado()} días")
    separador()

    id_dev = pedir("ID del ítem a devolver").upper()
    item_dev = next((p for p in activos if p.id_item == id_dev), None)
    if not item_dev:
        error("ID no válido o no activo.")
        input("  Presione Enter para continuar...")
        return

    hoy = datetime.today().strftime("%Y-%m-%d")
    for p in prestamos:
        if p.id_item == id_dev:
            p.activo = False
            p.fecha_devolucion = hoy
            break
    guardar_prestamos(prestamos)

    # Generar certificado
    os.makedirs(RUTA_DOCS, exist_ok=True)
    nombre_doc = f"{usuario.apellido}_{hoy}_{id_dev}.txt"
    ruta_cert  = os.path.join(RUTA_DOCS, nombre_doc)
    with open(ruta_cert, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("       CERTIFICADO DE DEVOLUCIÓN - PrestaFácil\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Fecha de emisión  : {hoy}\n")
        f.write(f"Usuario           : {usuario.nombre} {usuario.apellido}\n")
        f.write(f"Documento         : {usuario.documento}\n")
        f.write(f"Correo            : {usuario.correo}\n\n")
        f.write(f"Ítem devuelto     : {item_dev.nombre_item}\n")
        f.write(f"ID del ítem       : {item_dev.id_item}\n")
        f.write(f"Categoría         : {item_dev.categoria}\n")
        f.write(f"Fecha de préstamo : {item_dev.fecha_prestamo}\n")
        f.write(f"Fecha devolución  : {hoy}\n")
        f.write(f"Días prestado     : {item_dev.dias_prestado()}\n\n")
        f.write("Estado: DEVOLUCIÓN EXITOSA\n")
        f.write("=" * 60 + "\n")

    ok(f"Devolución registrada. Certificado: {ruta_cert}")
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 5: ÍTEMS CON MÁS DE 30 DÍAS (GENERAR VENTA)
# ─────────────────────────────────────────────
def consultar_vencidos():
    banner()
    print(f"  {NEGRITA}── ÍTEMS CON MÁS DE 30 DÍAS (GENERAR VENTA) ──{RESET}\n")
    usuarios  = cargar_usuarios()
    prestamos = cargar_prestamos()
    IMPUESTO  = 0.23

    vencidos = [p for p in prestamos if p.activo and p.dias_prestado() > 30]
    if not vencidos:
        info("No hay ítems con más de 30 días prestados.")
        input("  Presione Enter para continuar...")
        return

    hoy = datetime.today().strftime("%Y-%m-%d")
    os.makedirs(RUTA_DOCS, exist_ok=True)

    for p in vencidos:
        usuario = next((u for u in usuarios if u.documento == p.documento_usuario), None)
        nombre_u = f"{usuario.nombre} {usuario.apellido}" if usuario else p.documento_usuario
        subtotal = p.precio
        impuesto = subtotal * IMPUESTO
        total    = subtotal + impuesto

        print(f"  {AMARILLO}► {p.nombre_item} ({p.id_item}) — {p.dias_prestado()} días — {nombre_u}{RESET}")
        print(f"    Precio base: ${subtotal:,.0f}  |  Impuesto 23%: ${impuesto:,.0f}  |  Total: ${total:,.0f}")

        nombre_doc = f"{nombre_u.replace(' ','_')}_{p.id_item}_VENTA.txt"
        ruta_fact  = os.path.join(RUTA_DOCS, nombre_doc)
        with open(ruta_fact, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write("         FACTURA DE VENTA - PrestaFácil\n")
            f.write("=" * 60 + "\n\n")
            f.write("MOTIVACIÓN: El ítem fue prestado por más de 30 días sin\n")
            f.write("devolución, por lo que según acuerdo previo, se procede\n")
            f.write("a generar factura de compra al precio de adquisición.\n\n")
            f.write(f"Fecha emisión     : {hoy}\n")
            f.write(f"Comprador         : {nombre_u}\n")
            f.write(f"Documento         : {p.documento_usuario}\n\n")
            f.write(f"Ítem              : {p.nombre_item}\n")
            f.write(f"ID                : {p.id_item}\n")
            f.write(f"Categoría         : {p.categoria}\n")
            f.write(f"Días prestado     : {p.dias_prestado()}\n\n")
            f.write(f"{'Subtotal':<30} ${subtotal:>12,.0f}\n")
            f.write(f"{'Impuesto por conchudez (23%)':<30} ${impuesto:>12,.0f}\n")
            f.write("-" * 45 + "\n")
            f.write(f"{'TOTAL A PAGAR':<30} ${total:>12,.0f}\n")
            f.write("=" * 60 + "\n")
        ok(f"Factura generada: {ruta_fact}")

    exportar_csv()
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 6: CONSULTAR ARTÍCULOS PRESTADOS
# ─────────────────────────────────────────────
def consultar_prestados():
    banner()
    print(f"  {NEGRITA}── ARTÍCULOS PRESTADOS (orden por días) ──{RESET}\n")
    usuarios  = cargar_usuarios()
    prestamos = cargar_prestamos()

    activos = [p for p in prestamos if p.activo]
    if not activos:
        info("No hay préstamos activos.")
        input("  Presione Enter para continuar...")
        return

    activos.sort(key=lambda x: x.dias_prestado(), reverse=True)
    print(f"  {'#':<4} {'ID':<12} {'Ítem':<20} {'Días':>6}  {'Estado':<10} {'Usuario'}")
    separador()
    for i, p in enumerate(activos, 1):
        usuario = next((u for u in usuarios if u.documento == p.documento_usuario), None)
        nombre_u = f"{usuario.nombre} {usuario.apellido}" if usuario else p.documento_usuario
        alerta = f"{ROJO}⚠ VENCIDO{RESET}" if p.dias_prestado() > 30 else \
                 (f"{AMARILLO}⚡ PRONTO{RESET}" if p.dias_prestado() > 20 else "")
        print(f"  {i:<4} {p.id_item:<12} {p.nombre_item:<20} {p.dias_prestado():>6}  {p.estado:<10} {nombre_u} {alerta}")

    separador()
    info(f"Total activos: {len(activos)}")
    input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MÓDULO 7: ADMINISTRADOR
# ─────────────────────────────────────────────
def modulo_administrador():
    banner()
    print(f"  {NEGRITA}── MÓDULO ADMINISTRADOR ──{RESET}\n")
    admins = cargar_admins()

    usuario_adm = pedir("Usuario administrador")
    clave_adm   = pedir("Contraseña")

    if admins.get(usuario_adm) != clave_adm:
        error("Credenciales incorrectas.")
        input("  Presione Enter para continuar...")
        return

    while True:
        banner()
        print(f"  {NEGRITA}── PANEL ADMINISTRADOR ──{RESET}\n")
        print("  1. Total de préstamos registrados")
        print("  2. Total de ítems devueltos")
        print("  3. Total de ventas realizadas")
        print("  4. Total pago realizado")
        print("  5. Lista de usuarios")
        print("  6. Usuario con mayor/menor préstamos")
        print("  7. Exportar CSV")
        print("  8. Volver")
        separador()
        op = pedir("Opción")

        prestamos = cargar_prestamos()
        usuarios  = cargar_usuarios()

        if op == "1":
            activos = [p for p in prestamos if p.activo]
            ok(f"Total préstamos activos: {len(activos)}")

        elif op == "2":
            devueltos = [p for p in prestamos if not p.activo and p.fecha_devolucion]
            ok(f"Total ítems devueltos: {len(devueltos)}")

        elif op == "3":
            ventas = [p for p in prestamos if p.activo and p.dias_prestado() > 30]
            ok(f"Total ventas generadas: {len(ventas)}")

        elif op == "4":
            total_pago = sum(p.precio * 1.23 for p in prestamos if p.activo and p.dias_prestado() > 30)
            ok(f"Total pagos generados: ${total_pago:,.0f}")

        elif op == "5":
            print()
            for u in usuarios:
                print(f"  • {u.nombre} {u.apellido} | Doc: {u.documento} | {u.correo}")

        elif op == "6":
            conteo = {}
            for p in prestamos:
                if p.documento_usuario:
                    conteo[p.documento_usuario] = conteo.get(p.documento_usuario, 0) + 1
            if conteo:
                max_doc = max(conteo, key=conteo.get)
                min_doc = min(conteo, key=conteo.get)
                max_u = next((u for u in usuarios if u.documento == max_doc), None)
                min_u = next((u for u in usuarios if u.documento == min_doc), None)
                ok(f"Mayor cantidad: {max_u.nombre if max_u else max_doc} ({conteo[max_doc]} préstamos)")
                ok(f"Menor cantidad: {min_u.nombre if min_u else min_doc} ({conteo[min_doc]} préstamos)")
            else:
                info("Sin datos de préstamos.")

        elif op == "7":
            exportar_csv()

        elif op == "8":
            break

        input("\n  Presione Enter para continuar...")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    """pf_Algoritmos - Punto de entrada principal de PrestaFácil."""
    os.makedirs("data", exist_ok=True)
    os.makedirs("doc", exist_ok=True)
    cargar_admins()  # inicializa admin por defecto si no existe

    while True:
        op = menu_principal()
        if op == "1":
            registrar_usuario()
        elif op == "2":
            registrar_item()
        elif op == "3":
            registrar_prestamo()
        elif op == "4":
            registrar_devolucion()
        elif op == "5":
            consultar_vencidos()
        elif op == "6":
            consultar_prestados()
        elif op == "7":
            modulo_administrador()
        elif op == "8":
            banner()
            print(f"  {VERDE}¡Hasta luego! Gracias por usar PrestaFácil.{RESET}\n")
            break
        else:
            error("Opción inválida.")
            input("  Presione Enter para continuar...")


if __name__ == "__main__":
    main()