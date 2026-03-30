"""
Contestador Automático - Sistema de Ventas y Soporte Técnico
Un programa interactivo que simula un sistema de atención telefónica automática
con opciones completas de Ventas y Soporte Técnico en Sistemas.
"""

import hashlib
import time
import datetime


# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────

def limpiar_pantalla():
    print("\n" + "=" * 60)


def pausa(segundos: float = 1.0):
    time.sleep(segundos)


def obtener_opcion(opciones_validas: list) -> str:
    """Solicita entrada al usuario y la valida contra una lista de opciones."""
    while True:
        opcion = input("\n  👉  Ingrese su opción: ").strip()
        if opcion in opciones_validas:
            return opcion
        print(f"  ⚠️  Opción inválida. Por favor elija entre: {', '.join(opciones_validas)}")


def encabezado(titulo: str):
    limpiar_pantalla()
    print(f"  {'─' * 56}")
    print(f"  {'CONTESTADOR AUTOMÁTICO':^56}")
    print(f"  {titulo:^56}")
    print(f"  {'─' * 56}")


def generar_ticket() -> str:
    """Genera un número de ticket único basado en la fecha y hora actual."""
    ahora = datetime.datetime.now()
    return f"TKT-{ahora.strftime('%Y%m%d%H%M%S')}"


# ─────────────────────────────────────────────
#  MÓDULO DE VENTAS
# ─────────────────────────────────────────────

def ventas_nuevos_productos():
    encabezado("Ventas › Nuevos Productos")
    catalogo = [
        ("001", "Suite Ofimática Pro",         "$299.99 / año"),
        ("002", "Sistema ERP Empresarial",      "$1,200.00 / año"),
        ("003", "Antivirus Corporativo",         "$89.99 / equipo/año"),
        ("004", "Software de Facturación",       "$450.00 / año"),
        ("005", "Plataforma CRM",               "$599.00 / año"),
        ("006", "Servidor Virtual (VPS)",        "$49.99 / mes"),
        ("007", "Laptop Empresarial 15\"",       "$1,150.00"),
        ("008", "Estación de Trabajo Tower",     "$1,800.00"),
    ]
    print("\n  📦  CATÁLOGO DE PRODUCTOS DISPONIBLES\n")
    for cod, nombre, precio in catalogo:
        print(f"  [{cod}]  {nombre:<35} {precio}")
    print("\n  Para adquirir algún producto, un asesor se pondrá en")
    print("  contacto con usted en las próximas 24 horas hábiles.")
    print("  También puede visitar: www.empresa.com/catalogo")
    pausa(2)


def ventas_promociones():
    encabezado("Ventas › Promociones y Ofertas")
    print("\n  🏷️   PROMOCIONES VIGENTES\n")
    promos = [
        ("Suite Ofimática Pro",   "30 % de descuento en planes anuales"),
        ("Antivirus Corporativo", "2 licencias gratis al comprar 10"),
        ("Laptop Empresarial",    "Financiamiento a 12 meses sin intereses"),
        ("ERP Empresarial",       "3 meses gratis en contrato de 1 año"),
        ("Paquete Cloud Starter", "Primer mes gratis + instalación incluida"),
    ]
    for prod, desc in promos:
        print(f"  ✅  {prod}")
        print(f"      {desc}\n")
    print("  ⏰  Promociones válidas hasta el 30 de abril de 2026.")
    pausa(2)


def ventas_licencias_software():
    encabezado("Ventas › Licencias de Software")
    print("\n  💿  TIPOS DE LICENCIAS DISPONIBLES\n")
    licencias = [
        ("Licencia Individual",     "1 usuario / 1 dispositivo",          "Desde $49.99"),
        ("Licencia Multiusuario",   "Hasta 10 usuarios",                   "Desde $199.99"),
        ("Licencia Corporativa",    "Usuarios ilimitados en una empresa",  "Desde $999.99"),
        ("Licencia Educativa",      "Instituciones educativas",            "50 % descuento"),
        ("Licencia Gubernamental",  "Organismos del sector público",       "Precio especial"),
        ("Suscripción SaaS",        "Acceso web, sin instalación",         "Desde $19.99/mes"),
    ]
    print(f"  {'Tipo':<28} {'Alcance':<40} {'Precio'}")
    print(f"  {'-'*26} {'-'*38} {'-'*18}")
    for tipo, alcance, precio in licencias:
        print(f"  {tipo:<28} {alcance:<40} {precio}")
    print("\n  Para cotizaciones personalizadas llame al: 800-555-0100")
    pausa(2)


def ventas_hardware():
    encabezado("Ventas › Hardware y Equipos")
    print("\n  🖥️   EQUIPOS DISPONIBLES\n")
    equipos = [
        ("Laptops empresariales",        "Intel Core i5/i7, 16 GB RAM, 512 GB SSD"),
        ("Desktops / Estaciones trabajo","Intel/AMD, 32 GB RAM, configuración a medida"),
        ("Servidores rack",              "Dell PowerEdge, HPE ProLiant"),
        ("Switches administrables",      "Cisco, HP Aruba — 24 / 48 puertos"),
        ("Routers empresariales",        "Cisco ISR, MikroTik, pfSense"),
        ("UPS / Reguladores",            "APC, Eaton — protección de equipos"),
        ("Impresoras / Multifuncionales","HP, Brother, Xerox — inyección y láser"),
        ("Monitores",                    "24\" / 27\" / 32\" — Full HD, 4K"),
        ("Accesorios de red",            "Cables, patch panels, fibra óptica"),
    ]
    for nombre, detalle in equipos:
        print(f"  🔹  {nombre}")
        print(f"      {detalle}\n")
    print("  Solicite una demo o cotización: ventas@empresa.com")
    pausa(2)


def ventas_servicios_nube():
    encabezado("Ventas › Servicios en la Nube")
    print("\n  ☁️   SOLUCIONES CLOUD\n")
    servicios = [
        ("IaaS – Infraestructura como Servicio",
         "Servidores virtuales, almacenamiento, redes escalables"),
        ("PaaS – Plataforma como Servicio",
         "Entornos de desarrollo y despliegue de aplicaciones"),
        ("SaaS – Software como Servicio",
         "ERP, CRM, ofimática y más, accesibles desde el navegador"),
        ("Almacenamiento en la Nube",
         "Desde 100 GB hasta soluciones de petabytes"),
        ("Backup en la Nube",
         "Respaldo automático cifrado y recuperación ante desastres"),
        ("CDN – Red de Distribución de Contenidos",
         "Acelera la entrega de tus sitios web globalmente"),
        ("Seguridad Cloud",
         "Firewall, WAF, DDoS protection, monitoreo 24/7"),
    ]
    for nombre, desc in servicios:
        print(f"  ☁  {nombre}")
        print(f"     {desc}\n")
    pausa(2)


def ventas_planes_empresariales():
    encabezado("Ventas › Planes Empresariales")
    print("\n  🏢  PLANES PARA EMPRESAS\n")
    planes = [
        ("BÁSICO",      "1-10 empleados",    "$199/mes",  ["Soporte 8×5", "5 licencias software", "50 GB nube"]),
        ("PROFESIONAL", "11-50 empleados",   "$499/mes",  ["Soporte 12×7", "25 licencias", "500 GB nube", "VPN"]),
        ("EMPRESARIAL", "51-200 empleados",  "$999/mes",  ["Soporte 24×7", "100 licencias", "2 TB nube", "Firewall"]),
        ("CORPORATIVO", "200+ empleados",    "A medida",  ["SLA personalizado", "Licencias ilimitadas", "Infraestructura dedicada"]),
    ]
    for nombre, tamaño, precio, incluye in planes:
        print(f"  ─── Plan {nombre} ({tamaño}) ── {precio} ───")
        for item in incluye:
            print(f"      ✔ {item}")
        print()
    print("  Contáctenos para un diagnóstico gratuito: 800-555-0200")
    pausa(2)


def menu_ventas():
    while True:
        encabezado("VENTAS")
        opciones_texto = [
            ("1", "Nuevos Productos"),
            ("2", "Promociones y Ofertas"),
            ("3", "Licencias de Software"),
            ("4", "Hardware y Equipos"),
            ("5", "Servicios en la Nube"),
            ("6", "Planes Empresariales"),
            ("0", "⬅  Regresar al Menú Principal"),
        ]
        for cod, desc in opciones_texto:
            print(f"  [{cod}]  {desc}")

        opcion = obtener_opcion([c for c, _ in opciones_texto])

        if opcion == "1":
            ventas_nuevos_productos()
        elif opcion == "2":
            ventas_promociones()
        elif opcion == "3":
            ventas_licencias_software()
        elif opcion == "4":
            ventas_hardware()
        elif opcion == "5":
            ventas_servicios_nube()
        elif opcion == "6":
            ventas_planes_empresariales()
        elif opcion == "0":
            break


# ─────────────────────────────────────────────
#  MÓDULO DE SOPORTE TÉCNICO
# ─────────────────────────────────────────────

def soporte_software():
    encabezado("Soporte Técnico › Software")
    print("\n  💻  SOPORTE PARA SOFTWARE\n")
    temas = [
        "Instalación y actualización de aplicaciones",
        "Problemas de activación / licencias",
        "Errores y bloqueos de programas",
        "Compatibilidad entre aplicaciones",
        "Migración de datos entre versiones",
        "Configuración de correo electrónico (Outlook, Thunderbird, etc.)",
        "Problemas con navegadores web",
        "Software de seguridad y antivirus",
        "Drivers y controladores de dispositivos",
        "Aplicaciones de productividad (Office, LibreOffice, etc.)",
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i:2}. {tema}")
    print("\n  Para atención inmediata llame al: 800-555-0300")
    print("  Horario: Lunes a Viernes 8:00 – 20:00 hrs")
    pausa(2)


def soporte_hardware():
    encabezado("Soporte Técnico › Hardware")
    print("\n  🔧  SOPORTE PARA HARDWARE\n")
    temas = [
        "Diagnóstico y reparación de equipos de cómputo",
        "Reemplazo de componentes (RAM, disco, batería, etc.)",
        "Problemas de arranque / encendido",
        "Sobrecalentamiento y ventilación",
        "Periféricos: teclado, ratón, monitor, impresora",
        "Problemas con puertos USB, HDMI, Thunderbolt",
        "Mantenimiento preventivo y limpieza",
        "Diagnóstico de fallas en servidores físicos",
        "Garantías y devoluciones de equipo",
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i:2}. {tema}")
    print("\n  Servicio a domicilio disponible en ciudades principales.")
    print("  Agende su visita técnica: soporte@empresa.com")
    pausa(2)


def soporte_redes():
    encabezado("Soporte Técnico › Redes y Conectividad")
    print("\n  🌐  SOPORTE DE REDES\n")
    temas = [
        "Configuración de redes LAN / WAN",
        "Wi-Fi: instalación, cobertura y velocidad",
        "Configuración de routers y switches",
        "VPN: instalación y acceso remoto",
        "Diagnóstico de caídas de red",
        "Segmentación de redes (VLANs)",
        "QoS y priorización de tráfico",
        "Configuración de DNS y DHCP",
        "Monitoreo de red (SNMP, Zabbix, PRTG)",
        "Cableado estructurado y fibra óptica",
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i:2}. {tema}")
    print("\n  NOC 24/7: noc@empresa.com  |  Teléfono: 800-555-0400")
    pausa(2)


def soporte_seguridad():
    encabezado("Soporte Técnico › Seguridad Informática")
    print("\n  🔒  SEGURIDAD INFORMÁTICA\n")
    areas = [
        ("Auditoría de seguridad",          "Evaluación completa de vulnerabilidades"),
        ("Gestión de firewalls",             "Configuración de reglas y políticas"),
        ("Detección de intrusiones (IDS/IPS)", "Monitoreo y alertas en tiempo real"),
        ("Protección contra malware",        "Limpieza y prevención de ransomware"),
        ("Análisis forense",                 "Investigación de incidentes de seguridad"),
        ("Gestión de identidades (IAM)",     "Control de accesos y permisos"),
        ("Cifrado de datos",                 "Datos en reposo y en tránsito"),
        ("Pentest / Pruebas de penetración", "Evaluaciones éticas de vulnerabilidades"),
        ("Concientización y capacitación",   "Talleres de ciberseguridad para empleados"),
        ("Cumplimiento normativo",           "ISO 27001, GDPR, HIPAA, PCI-DSS"),
    ]
    for nombre, desc in areas:
        print(f"  🛡  {nombre}")
        print(f"     {desc}\n")
    pausa(2)


def soporte_respaldo():
    encabezado("Soporte Técnico › Respaldo y Recuperación de Datos")
    print("\n  💾  BACKUP Y RECUPERACIÓN\n")
    opciones_resp = [
        "Configuración de políticas de respaldo automático",
        "Respaldo local (NAS, discos externos, cinta)",
        "Respaldo en la nube (AWS S3, Azure Blob, Google Cloud)",
        "Respaldo híbrido (local + nube)",
        "Pruebas de restauración y validación",
        "Recuperación ante desastres (DRP)",
        "Recuperación de datos desde dispositivos dañados",
        "Replicación de datos entre sitios",
        "Retención de datos y cumplimiento legal",
        "Cifrado de respaldos",
    ]
    for i, opcion in enumerate(opciones_resp, 1):
        print(f"  {i:2}. {opcion}")
    print("\n  ⚠️  Ante pérdida de datos llame INMEDIATAMENTE: 800-555-0500")
    pausa(2)


def soporte_sistemas_operativos():
    encabezado("Soporte Técnico › Sistemas Operativos")
    print("\n  🖥️   SOPORTE DE SISTEMAS OPERATIVOS\n")
    sistemas = [
        ("Windows 10 / 11",      "Activación, actualizaciones, perfiles, GPO"),
        ("Windows Server",       "Active Directory, DNS, DHCP, IIS, Hyper-V"),
        ("macOS",                "Configuración, FileVault, integraciones"),
        ("Linux (Ubuntu/CentOS/RHEL)", "Administración, scripting, servicios"),
        ("Virtualización",       "VMware, VirtualBox, Hyper-V, KVM"),
        ("Contenedores",         "Docker, Kubernetes, Docker Compose"),
        ("Actualizaciones masivas","WSUS, Ansible, scripts de automatización"),
        ("Migración de SO",      "Planeación y ejecución de migraciones"),
    ]
    for nombre, detalle in sistemas:
        print(f"  🔹  {nombre}")
        print(f"      {detalle}\n")
    pausa(2)


def soporte_remoto():
    encabezado("Soporte Técnico › Soporte Remoto")
    print("\n  📡  SOPORTE REMOTO\n")
    print("  Nuestros técnicos pueden conectarse a su equipo de forma")
    print("  segura para resolver problemas de manera inmediata.\n")
    herramientas = [
        "TeamViewer",
        "AnyDesk",
        "Microsoft Remote Desktop (RDP)",
        "Chrome Remote Desktop",
        "SSH para servidores Linux",
    ]
    print("  Herramientas autorizadas de acceso remoto:")
    for h in herramientas:
        print(f"    • {h}")
    print()
    print("  Pasos para iniciar sesión de soporte remoto:")
    pasos = [
        "Llame al 800-555-0300 para solicitar soporte remoto",
        "El agente le proporcionará un código de sesión único",
        "Descargue la herramienta indicada desde nuestra web",
        "Ingrese el código de sesión para autorizar la conexión",
        "El técnico resolverá el problema mientras usted observa",
        "Al finalizar, la sesión remota se cierra automáticamente",
    ]
    for i, paso in enumerate(pasos, 1):
        print(f"  {i}. {paso}")
    print("\n  ⏰  Disponibilidad: Lunes a Domingo 7:00 – 22:00 hrs")
    pausa(2)


def soporte_crear_ticket():
    encabezado("Soporte Técnico › Crear Ticket de Soporte")
    print("\n  🎫  REGISTRO DE NUEVO TICKET\n")
    print("  Por favor proporcione la siguiente información:\n")

    nombre = input("  Nombre completo: ").strip() or "No especificado"
    empresa = input("  Empresa / Organización: ").strip() or "No especificado"
    correo = input("  Correo electrónico: ").strip() or "No especificado"
    telefono = input("  Teléfono de contacto: ").strip() or "No especificado"

    print("\n  Categoría del problema:")
    categorias = {
        "1": "Software",
        "2": "Hardware",
        "3": "Redes / Conectividad",
        "4": "Seguridad",
        "5": "Respaldo / Recuperación de datos",
        "6": "Sistema Operativo",
        "7": "Otro",
    }
    for k, v in categorias.items():
        print(f"    [{k}] {v}")
    cat_opcion = obtener_opcion(list(categorias.keys()))
    categoria = categorias[cat_opcion]

    print("\n  Prioridad:")
    prioridades = {"1": "Baja", "2": "Media", "3": "Alta", "4": "Crítica"}
    for k, v in prioridades.items():
        print(f"    [{k}] {v}")
    prio_opcion = obtener_opcion(list(prioridades.keys()))
    prioridad = prioridades[prio_opcion]

    print()
    descripcion = input("  Describa brevemente el problema:\n  > ").strip() or "Sin descripción"

    ticket_id = generar_ticket()
    print(f"\n  {'─' * 50}")
    print(f"  ✅  TICKET CREADO EXITOSAMENTE")
    print(f"  {'─' * 50}")
    print(f"  Número de ticket : {ticket_id}")
    print(f"  Nombre           : {nombre}")
    print(f"  Empresa          : {empresa}")
    print(f"  Correo           : {correo}")
    print(f"  Teléfono         : {telefono}")
    print(f"  Categoría        : {categoria}")
    print(f"  Prioridad        : {prioridad}")
    print(f"  Descripción      : {descripcion}")
    print(f"  {'─' * 50}")
    print(f"\n  Un técnico se pondrá en contacto en:")
    tiempos = {"Baja": "72 horas", "Media": "24 horas", "Alta": "4 horas", "Crítica": "1 hora"}
    print(f"  ⏱  Tiempo estimado de respuesta: {tiempos[prioridad]}")
    print(f"\n  Guarde su número de ticket para dar seguimiento.")
    pausa(3)


def soporte_estado_ticket():
    encabezado("Soporte Técnico › Estado de Ticket")
    print("\n  🔍  CONSULTA DE ESTADO DE TICKET\n")
    ticket_id = input("  Ingrese su número de ticket (ej. TKT-20260330123456): ").strip()
    if not ticket_id:
        print("  ⚠️  Número de ticket no proporcionado.")
        pausa(1)
        return
    print(f"\n  Consultando ticket {ticket_id} ...")
    pausa(1)
    # Simulación de estados posibles
    estados = ["En revisión", "Asignado al técnico", "En proceso", "Pendiente de usuario", "Resuelto"]
    indice = int(hashlib.md5(ticket_id.encode()).hexdigest(), 16) % len(estados)
    estado = estados[indice]
    print(f"\n  Ticket   : {ticket_id}")
    print(f"  Estado   : {estado}")
    print(f"\n  Para más detalles, comuníquese al 800-555-0300")
    print(f"  o envíe correo a: soporte@empresa.com")
    pausa(2)


def menu_soporte():
    while True:
        encabezado("SOPORTE TÉCNICO")
        opciones_texto = [
            ("1", "Soporte para Software"),
            ("2", "Soporte para Hardware"),
            ("3", "Redes y Conectividad"),
            ("4", "Seguridad Informática"),
            ("5", "Respaldo y Recuperación de Datos"),
            ("6", "Sistemas Operativos"),
            ("7", "Soporte Remoto"),
            ("8", "Crear Ticket de Soporte"),
            ("9", "Consultar Estado de Ticket"),
            ("0", "⬅  Regresar al Menú Principal"),
        ]
        for cod, desc in opciones_texto:
            print(f"  [{cod}]  {desc}")

        opcion = obtener_opcion([c for c, _ in opciones_texto])

        if opcion == "1":
            soporte_software()
        elif opcion == "2":
            soporte_hardware()
        elif opcion == "3":
            soporte_redes()
        elif opcion == "4":
            soporte_seguridad()
        elif opcion == "5":
            soporte_respaldo()
        elif opcion == "6":
            soporte_sistemas_operativos()
        elif opcion == "7":
            soporte_remoto()
        elif opcion == "8":
            soporte_crear_ticket()
        elif opcion == "9":
            soporte_estado_ticket()
        elif opcion == "0":
            break


# ─────────────────────────────────────────────
#  MÓDULO DE FACTURACIÓN
# ─────────────────────────────────────────────

def menu_facturacion():
    while True:
        encabezado("FACTURACIÓN")
        opciones_texto = [
            ("1", "Consultar saldo de cuenta"),
            ("2", "Solicitar factura electrónica"),
            ("3", "Métodos de pago aceptados"),
            ("4", "Estado de pagos / historial"),
            ("5", "Cancelar o modificar suscripción"),
            ("0", "⬅  Regresar al Menú Principal"),
        ]
        for cod, desc in opciones_texto:
            print(f"  [{cod}]  {desc}")

        opcion = obtener_opcion([c for c, _ in opciones_texto])

        if opcion == "1":
            encabezado("Facturación › Saldo de Cuenta")
            print("\n  Para consultar su saldo ingrese a:")
            print("  🌐  https://portal.empresa.com/cuenta")
            print("  O llame al 800-555-0600 con su número de cliente.")
            pausa(2)

        elif opcion == "2":
            encabezado("Facturación › Factura Electrónica")
            print("\n  Solicitud de factura electrónica (CFDI / Factura XML)\n")
            print("  Envíe los siguientes datos a: facturacion@empresa.com")
            datos = ["RFC / NIT", "Razón Social", "Domicilio fiscal",
                     "Correo para envío de factura", "Folio de compra / número de pedido"]
            for d in datos:
                print(f"    • {d}")
            print("\n  ⏱  Tiempo de emisión: hasta 3 días hábiles")
            pausa(2)

        elif opcion == "3":
            encabezado("Facturación › Métodos de Pago")
            print("\n  💳  MÉTODOS DE PAGO ACEPTADOS\n")
            metodos = [
                "Tarjeta de crédito / débito (Visa, Mastercard, Amex)",
                "Transferencia bancaria (SPEI / Wire Transfer)",
                "Depósito bancario",
                "PayPal",
                "Cheque (solo empresas con cuenta establecida)",
                "Criptomonedas (Bitcoin, Ethereum) — consultar disponibilidad",
            ]
            for m in metodos:
                print(f"    ✅  {m}")
            pausa(2)

        elif opcion == "4":
            encabezado("Facturación › Historial de Pagos")
            print("\n  📋  Para consultar su historial de pagos:\n")
            print("  1. Ingrese al portal: https://portal.empresa.com/pagos")
            print("  2. Use su correo y contraseña registrados")
            print("  3. Seleccione 'Historial de Transacciones'")
            print("\n  También puede solicitarlo por correo: cobranza@empresa.com")
            pausa(2)

        elif opcion == "5":
            encabezado("Facturación › Cancelar / Modificar Suscripción")
            print("\n  ⚠️  Para cancelar o modificar su suscripción:\n")
            print("  • Llame al 800-555-0600 con su número de cliente")
            print("  • Recuerde que las cancelaciones aplican al siguiente ciclo")
            print("  • Se requiere un aviso con al menos 15 días de anticipación")
            print("  • No hay penalización en contratos mensuales")
            pausa(2)

        elif opcion == "0":
            break


# ─────────────────────────────────────────────
#  MÓDULO DE ATENCIÓN PERSONALIZADA
# ─────────────────────────────────────────────

def hablar_con_agente():
    encabezado("Hablar con un Agente")
    print("\n  👤  ATENCIÓN PERSONALIZADA\n")
    print("  Todos nuestros agentes están disponibles en el siguiente")
    print("  horario de atención:\n")
    print("  📅  Lunes a Viernes  :  08:00 – 20:00 hrs")
    print("  📅  Sábados          :  09:00 – 14:00 hrs")
    print("  📅  Domingos y festivos: Soporte de emergencia 24/7\n")
    print("  📞  Líneas de contacto:\n")
    lineas = [
        ("Ventas",                    "800-555-0100"),
        ("Soporte Técnico",           "800-555-0300"),
        ("Facturación / Cobranza",    "800-555-0600"),
        ("Emergencias / Incidentes",  "800-555-0911"),
    ]
    for area, numero in lineas:
        print(f"  {'[' + area + ']':<32}  {numero}")
    print()
    print("  📧  Correos de contacto:\n")
    correos = [
        ("Ventas",              "ventas@empresa.com"),
        ("Soporte Técnico",     "soporte@empresa.com"),
        ("Facturación",         "facturacion@empresa.com"),
        ("Información general", "contacto@empresa.com"),
    ]
    for area, correo in correos:
        print(f"  {'[' + area + ']':<32}  {correo}")
    print()
    print("  💬  Chat en vivo: https://empresa.com/chat")
    print("  📱  WhatsApp Business: +52 55 1234 5678")
    pausa(3)


def preguntas_frecuentes():
    encabezado("Preguntas Frecuentes (FAQ)")
    faq = [
        ("¿Cómo activo mi licencia de software?",
         "Recibirá un correo con su clave de activación. Abra el\n"
         "     software, vaya a 'Activar producto' e ingrese la clave.\n"
         "     En caso de problemas llame al 800-555-0300."),
        ("¿Qué hago si olvidé mi contraseña?",
         "Ingrese al portal y seleccione '¿Olvidé mi contraseña?'.\n"
         "     Recibirá un enlace de recuperación en su correo."),
        ("¿Tienen soporte en español e inglés?",
         "Sí. Contamos con agentes bilingües disponibles en el\n"
         "     mismo número de soporte."),
        ("¿Cuánto tarda una instalación on-site?",
         "Normalmente se agenda en 24-48 horas hábiles. El tiempo\n"
         "     de instalación varía según el alcance del proyecto."),
        ("¿Puedo transferir mi licencia a otro equipo?",
         "Depende del tipo de licencia. Las licencias por dispositivo\n"
         "     requieren desactivación previa. Contáctenos para ayuda."),
        ("¿Ofrecen capacitación sobre los productos?",
         "Sí. Tenemos cursos presenciales, en línea y a medida.\n"
         "     Consulte: https://empresa.com/capacitacion"),
    ]
    for i, (pregunta, respuesta) in enumerate(faq, 1):
        print(f"\n  ❓  {pregunta}")
        print(f"  ✅  {respuesta}")
    pausa(3)


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def bienvenida():
    print("\n" + "=" * 60)
    print(" " * 10 + "BIENVENIDO AL SISTEMA DE ATENCIÓN")
    print(" " * 10 + "    EMPRESA TECNOLÓGICA S.A. de C.V.")
    print("=" * 60)
    print("\n  Gracias por comunicarse con nosotros.")
    print("  Por favor, escuche las siguientes opciones.\n")
    pausa(1)


def despedida():
    print("\n" + "=" * 60)
    print("  Gracias por contactar a Empresa Tecnológica S.A. de C.V.")
    print("  ¡Que tenga un excelente día!")
    print("=" * 60 + "\n")


def menu_principal():
    bienvenida()
    while True:
        encabezado("MENÚ PRINCIPAL")
        opciones_texto = [
            ("1", "📦  Ventas"),
            ("2", "🔧  Soporte Técnico"),
            ("3", "💳  Facturación"),
            ("4", "👤  Hablar con un Agente"),
            ("5", "❓  Preguntas Frecuentes"),
            ("0", "🚪  Salir"),
        ]
        for cod, desc in opciones_texto:
            print(f"  [{cod}]  {desc}")

        opcion = obtener_opcion([c for c, _ in opciones_texto])

        if opcion == "1":
            menu_ventas()
        elif opcion == "2":
            menu_soporte()
        elif opcion == "3":
            menu_facturacion()
        elif opcion == "4":
            hablar_con_agente()
        elif opcion == "5":
            preguntas_frecuentes()
        elif opcion == "0":
            despedida()
            break


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()
