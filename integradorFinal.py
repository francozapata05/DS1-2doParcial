"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Franco\Desktop\parcial2-diseno
Fecha de generacion: 2025-11-04 16:23:11
Total de archivos integrados: 59
Total de directorios procesados: 23
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. buscar_paquete.py
#
# DIRECTORIO: casa_inteligente
#   2. main.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic
#   3. __init__.py
#   4. constantes.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion
#   5. __init__.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion\control
#   6. __init__.py
#   7. control_automatizacion_task.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion\sensores
#   8. __init__.py
#   9. movimiento_sensor_task.py
#   10. temperatura_sensor_task.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades
#   11. __init__.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
#   12. __init__.py
#   13. dispositivo.py
#   14. dispositivo_climatico.py
#   15. dispositivo_iluminacion.py
#   16. luz_inteligente.py
#   17. termostato_inteligente.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\espacios
#   18. __init__.py
#   19. casa.py
#   20. habitacion.py
#   21. registro_propiedad.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\usuarios
#   22. __init__.py
#   23. accion.py
#   24. permiso_acceso.py
#   25. usuario.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\excepciones
#   26. __init__.py
#   27. casa_inteligente_exception.py
#   28. mensajes_exception.py
#   29. operacion_invalida_exception.py
#   30. persistencia_exception.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones
#   31. __init__.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\factory
#   32. __init__.py
#   33. dispositivo_factory.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\observer
#   34. __init__.py
#   35. observable.py
#   36. observer.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\observer\eventos
#   37. __init__.py
#   38. evento_sensor.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\singleton
#   39. __init__.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\strategy
#   40. __init__.py
#   41. modo_operacion_strategy.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
#   42. __init__.py
#   43. modo_dia_strategy.py
#   44. modo_noche_strategy.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios
#   45. __init__.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
#   46. __init__.py
#   47. dispositivo_service.py
#   48. dispositivo_service_registry.py
#   49. luz_inteligente_service.py
#   50. termostato_inteligente_service.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\espacios
#   51. __init__.py
#   52. casa_service.py
#   53. habitacion_service.py
#   54. registro_propiedad_service.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\negocio
#   55. __init__.py
#   56. casas_service.py
#   57. paquete.py
#
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\usuarios
#   58. __init__.py
#   59. usuario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/59: buscar_paquete.py
# Directorio: .
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "casa_inteligente")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())


################################################################################
# DIRECTORIO: casa_inteligente
################################################################################

# ==============================================================================
# ARCHIVO 2/59: main.py
# Directorio: casa_inteligente
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\main.py
# ==============================================================================

"""
Ejemplo de uso del sistema de casa inteligente.
"""

import time
from datetime import date
from casa_inteligente_logic.servicios.espacios.casa_service import CasaService
from casa_inteligente_logic.servicios.espacios.habitacion_service import HabitacionService
from casa_inteligente_logic.servicios.espacios.registro_propiedad_service import RegistroPropiedadService
from casa_inteligente_logic.entidades.espacios.registro_propiedad import RegistroPropiedad
from casa_inteligente_logic.servicios.usuarios.usuario_service import UsuarioService
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario
from casa_inteligente_logic.entidades.usuarios.accion import Accion
from casa_inteligente_logic.servicios.negocio.casas_service import CasasService
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from casa_inteligente_logic.automatizacion.sensores.temperatura_sensor_task import TemperaturaSensorTask
from casa_inteligente_logic.automatizacion.sensores.movimiento_sensor_task import MovimientoSensorTask
from casa_inteligente_logic.automatizacion.control.control_automatizacion_task import ControlAutomatizacionTask
from casa_inteligente_logic.excepciones.casa_inteligente_exception import CasaInteligenteException
from casa_inteligente_logic.constantes import THREAD_JOIN_TIMEOUT
from casa_inteligente_logic.patrones.strategy.impl.modo_dia_strategy import ModoDiaStrategy
from casa_inteligente_logic.patrones.strategy.impl.modo_noche_strategy import ModoNocheStrategy

def main():
    """Punto de entrada principal del sistema."""
    print("=" * 70)
    print("         SISTEMA DE CASA INTELIGENTE - PATRONES DE DISENO")
    print("=" * 70)

    # Singleton
    print("\n" + "-" * 70)
    print("  PATRON SINGLETON: Inicializando servicios")
    print("-" * 70)
    habitacion_service = HabitacionService()
    registro_service = RegistroPropiedadService()
    usuario_service = UsuarioService()
    casas_service = CasasService()
    print("[OK] Todos los servicios comparten la misma instancia del Registry")

    # Creacion de casa y habitacion
    print("\n1. Creando casa con habitacion...")
    casa_service = CasaService()
    casa = casa_service.crear_casa_con_habitacion(
        id_catastral=1,
        domicilio="Av. Siempre Viva 742",
        nombre_habitacion="Living"
    )
    habitacion = casa_service.get_habitacion(casa)
    print(f"[OK] Habitacion '{habitacion.get_nombre()}' creada en la casa.")

    # Registro de Propiedad
    print("\n2. Creando registro de propiedad...")
    registro = RegistroPropiedad(
        id_catastral=1,
        casa=casa,
        habitacion=habitacion,
        propietario="Homero Simpson",
        avaluo=150000.0
    )
    print("[OK] Registro de propiedad creado.")

    # Factory
    print("\n" + "-" * 70)
    print("  PATRON FACTORY: Instalando dispositivos")
    print("-" * 70)
    try:
        habitacion_service.instalar_dispositivo(habitacion, "LuzInteligente", "Luz del living")
        habitacion_service.instalar_dispositivo(habitacion, "TermostatoInteligente", "Termostato del living")
        print("[OK] Dispositivos instalados exitosamente.")
    except CasaInteligenteException as e:
        print(f"[ERROR] {e.get_user_message()}")

    # Strategy
    print("\n" + "-" * 70)
    print("  PATRON STRATEGY: Activando modos")
    print("-" * 70)
    habitacion_service.activar_modo(habitacion, ModoNocheStrategy())
    habitacion_service.activar_modo(habitacion, ModoDiaStrategy())

    # Observer
    print("\n" + "-" * 70)
    print("  PATRON OBSERVER: Sistema de automatizacion")
    print("-" * 70)
    tarea_temp = TemperaturaSensorTask()
    tarea_mov = MovimientoSensorTask()
    tarea_control = ControlAutomatizacionTask(tarea_temp, tarea_mov, habitacion, habitacion_service)

    print("[INFO] Iniciando sensores y control de automatizacion...")
    tarea_temp.start()
    tarea_mov.start()
    tarea_control.start()

    time.sleep(10)

    print("[INFO] Deteniendo sistema de automatizacion...")
    tarea_temp.detener()
    tarea_mov.detener()
    tarea_control.detener()
    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_mov.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)
    print("[OK] Sistema de automatizacion detenido.")

    # Gestion de Usuarios
    print("\n3. Gestion de Usuarios...")
    acciones = [
        Accion(1, "Encender luces"),
        Accion(2, "Apagar luces"),
        Accion(3, "Regular termostato")
    ]
    usuario = Usuario(25123456, "Homero Simpson", acciones)
    habitacion.set_usuarios([usuario])
    print(f"[OK] Usuario '{usuario.get_nombre()}' asignado a la habitacion.")

    usuario_service.asignar_permiso_acceso(
        usuario,
        True,
        date.today(),
        "Acceso total"
    )
    print("[OK] Permiso de acceso asignado.")

    usuario_service.ejecutar_acciones(usuario, date.today())

    # Operaciones de Negocio
    print("\n4. Operaciones de Negocio...")
    casas_service.add_casa(registro)
    print("[OK] Casa agregada al servicio de casas.")

    caja_luces = casas_service.desactivar_dispositivos(1, LuzInteligente)
    caja_luces.mostrar_contenido_caja()

    # Persistencia
    print("\n5. Persistencia de Datos...")
    try:
        registro_service.persistir(registro)
        registro_leido = RegistroPropiedadService.leer_registro("Homero Simpson")
        registro_service.mostrar_datos(registro_leido)
    except CasaInteligenteException as e:
        print(f"[ERROR] {e.get_user_message()}")

    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - DispositivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de dispositivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Modos de operacion de la casa")
    print("=" * 70)

if __name__ == "__main__":
    main()



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic
################################################################################

# ==============================================================================
# ARCHIVO 3/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/59: constantes.py
# Directorio: casa_inteligente\casa_inteligente_logic
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\constantes.py
# ==============================================================================

"""
Modulo de constantes del sistema.
"""

# Automatizacion
TEMP_MIN_TERMOSTATO = 20  # °C
INTERVALO_CONTROL_AUTOMATIZACION = 2.5  # segundos
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
INTERVALO_SENSOR_MOVIMIENTO = 1.0  # segundos
SENSOR_TEMP_MIN = 15  # °C
SENSOR_TEMP_MAX = 30  # °C

# Persistencia
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# Threads
THREAD_JOIN_TIMEOUT = 2.0  # segundos



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion
################################################################################

# ==============================================================================
# ARCHIVO 5/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion\control
################################################################################

# ==============================================================================
# ARCHIVO 6/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion\control
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 7/59: control_automatizacion_task.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion\control
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\control\control_automatizacion_task.py
# ==============================================================================

"""
Controlador de automatizacion.
"""

import threading
import time
from casa_inteligente_logic.patrones.observer.observer import Observer
from casa_inteligente_logic.automatizacion.sensores.temperatura_sensor_task import TemperaturaSensorTask
from casa_inteligente_logic.automatizacion.sensores.movimiento_sensor_task import MovimientoSensorTask
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion
from casa_inteligente_logic.servicios.espacios.habitacion_service import HabitacionService
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

INTERVALO_CONTROL_AUTOMATIZACION = 2.5  # segundos
TEMP_MIN_TERMOSTATO = 20  # °C

class ControlAutomatizacionTask(threading.Thread, Observer):
    """Controla la automatizacion basado en sensores."""
    def __init__(
        self,
        sensor_temperatura: TemperaturaSensorTask,
        sensor_movimiento: MovimientoSensorTask,
        habitacion: Habitacion,
        habitacion_service: HabitacionService
    ):
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_movimiento = sensor_movimiento
        self._habitacion = habitacion
        self._habitacion_service = habitacion_service
        self._ultima_temperatura: float = 25.0
        self._ultimo_movimiento: bool = False
        self._detenido = threading.Event()

        # Suscribirse a los sensores
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_movimiento.agregar_observador(self)

    def actualizar(self, evento, sender) -> None:
        if isinstance(sender, TemperaturaSensorTask):
            self._ultima_temperatura = evento
        elif isinstance(sender, MovimientoSensorTask):
            self._ultimo_movimiento = evento

    def run(self):
        while not self._detenido.is_set():
            self._evaluar_y_actuar()
            time.sleep(INTERVALO_CONTROL_AUTOMATIZACION)

    def _evaluar_y_actuar(self):
        temp = self._ultima_temperatura
        movimiento = self._ultimo_movimiento

        print(f"[CONTROL] Temp: {temp}°C, Movimiento: {movimiento}")

        if temp < TEMP_MIN_TERMOSTATO:
            print("[CONTROL] Temperatura baja. Encendiendo termostato...")
            for dispositivo in self._habitacion.get_dispositivos():
                if isinstance(dispositivo, TermostatoInteligente):
                    dispositivo.encender()
                    print(f"[CONTROL] Termostato {dispositivo.get_nombre()} encendido.")
        
        if movimiento:
            print("[CONTROL] Movimiento detectado.")

    def detener(self) -> None:
        self._detenido.set()



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\automatizacion\sensores
################################################################################

# ==============================================================================
# ARCHIVO 8/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion\sensores
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 9/59: movimiento_sensor_task.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion\sensores
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\movimiento_sensor_task.py
# ==============================================================================

"""
Sensor de movimiento en tiempo real.
"""

import threading
import time
import random
from casa_inteligente_logic.patrones.observer.observable import Observable

INTERVALO_SENSOR_MOVIMIENTO = 1.0  # segundos

class MovimientoSensorTask(threading.Thread, Observable[bool]):
    """Detecta movimiento y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _detectar_movimiento(self) -> bool:
        return random.choice([True, False])

    def run(self):
        while not self._detenido.is_set():
            movimiento = self._detectar_movimiento()
            if movimiento:
                self.notificar_observadores(movimiento)
            time.sleep(INTERVALO_SENSOR_MOVIMIENTO)

    def detener(self) -> None:
        self._detenido.set()


# ==============================================================================
# ARCHIVO 10/59: temperatura_sensor_task.py
# Directorio: casa_inteligente\casa_inteligente_logic\automatizacion\sensores
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\automatizacion\sensores\temperatura_sensor_task.py
# ==============================================================================

"""
Sensor de temperatura en tiempo real.
"""

import threading
import time
import random
from casa_inteligente_logic.patrones.observer.observable import Observable

INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = 15  # °C
SENSOR_TEMP_MAX = 30  # °C

class TemperaturaSensorTask(threading.Thread, Observable[float]):
    """Lee la temperatura ambiental y notifica a los observadores."""
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def _leer_temperatura(self) -> float:
        return round(random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX), 2)

    def run(self):
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def detener(self) -> None:
        self._detenido.set()



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades
################################################################################

# ==============================================================================
# ARCHIVO 11/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
################################################################################

# ==============================================================================
# ARCHIVO 12/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/59: dispositivo.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo.py
# ==============================================================================

"""
Interfaz base para todos los dispositivos.
"""

from abc import ABC

class Dispositivo(ABC):
    """Clase abstracta que representa un dispositivo."""
    _id_counter = 0

    def __init__(self, nombre: str):
        Dispositivo._id_counter += 1
        self._id = Dispositivo._id_counter
        self._nombre = nombre
        self._encendido = False

    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def is_encendido(self) -> bool:
        return self._encendido

    def encender(self) -> None:
        self._encendido = True

    def apagar(self) -> None:
        self._encendido = False


# ==============================================================================
# ARCHIVO 14/59: dispositivo_climatico.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo_climatico.py
# ==============================================================================

"""
Clase base para dispositivos de climatizacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoClimatico(Dispositivo):
    """Clase abstracta para dispositivos de climatizacion."""
    def __init__(self, nombre: str, temperatura: float):
        super().__init__(nombre)
        self._temperatura = temperatura

    def get_temperatura(self) -> float:
        return self._temperatura

    def set_temperatura(self, temperatura: float) -> None:
        self._temperatura = temperatura


# ==============================================================================
# ARCHIVO 15/59: dispositivo_iluminacion.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\dispositivo_iluminacion.py
# ==============================================================================

"""
Clase base para dispositivos de iluminacion.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoIluminacion(Dispositivo):
    """Clase abstracta para dispositivos de iluminacion."""
    def __init__(self, nombre: str, brillo: int):
        super().__init__(nombre)
        self._brillo = brillo

    def get_brillo(self) -> int:
        return self._brillo

    def set_brillo(self, brillo: int) -> None:
        if not 0 <= brillo <= 100:
            raise ValueError("El brillo debe estar entre 0 y 100.")
        self._brillo = brillo


# ==============================================================================
# ARCHIVO 16/59: luz_inteligente.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\luz_inteligente.py
# ==============================================================================

"""
Entidad LuzInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_iluminacion import DispositivoIluminacion

class LuzInteligente(DispositivoIluminacion):
    """Entidad LuzInteligente - solo datos."""

    def __init__(self, nombre: str, marca: str):
        super().__init__(
            nombre=nombre,
            brillo=50
        )
        self._marca = marca

    def get_marca(self) -> str:
        return self._marca

    def set_marca(self, marca: str) -> None:
        self._marca = marca


# ==============================================================================
# ARCHIVO 17/59: termostato_inteligente.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\dispositivos\termostato_inteligente.py
# ==============================================================================

"""
Entidad TermostatoInteligente.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo_climatico import DispositivoClimatico

class TermostatoInteligente(DispositivoClimatico):
    """Entidad TermostatoInteligente - solo datos."""

    def __init__(self, nombre: str):
        super().__init__(
            nombre=nombre,
            temperatura=22.0
        )



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\espacios
################################################################################

# ==============================================================================
# ARCHIVO 18/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/59: casa.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\casa.py
# ==============================================================================

"""
Entidad Casa.
"""

class Casa:
    """Representa una casa."""
    def __init__(self, id_catastral: int, domicilio: str):
        if id_catastral <= 0:
            raise ValueError("El ID catastral debe ser mayor a cero.")
        self._id_catastral = id_catastral
        self._domicilio = domicilio

    def get_id_catastral(self) -> int:
        return self._id_catastral

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio


# ==============================================================================
# ARCHIVO 20/59: habitacion.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\habitacion.py
# ==============================================================================

"""
Entidad Habitacion.
"""

from typing import List
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario

class Habitacion:
    """Representa una habitacion en la casa."""
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._dispositivos: List[Dispositivo] = []
        self._usuarios: List[Usuario] = []

    def get_nombre(self) -> str:
        return self._nombre

    def get_dispositivos(self) -> List[Dispositivo]:
        return self._dispositivos.copy()

    def add_dispositivo(self, dispositivo: Dispositivo) -> None:
        self._dispositivos.append(dispositivo)

    def get_usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()

    def set_usuarios(self, usuarios: List[Usuario]) -> None:
        self._usuarios = usuarios


# ==============================================================================
# ARCHIVO 21/59: registro_propiedad.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\espacios\registro_propiedad.py
# ==============================================================================

"""
Entidad RegistroPropiedad.
"""

from casa_inteligente_logic.entidades.espacios.casa import Casa
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class RegistroPropiedad:
    """Vincula casa, habitacion, propietario y avaluo."""
    def __init__(self, id_catastral: int, casa: Casa, habitacion: Habitacion, propietario: str, avaluo: float):
        self._id_catastral = id_catastral
        self._casa = casa
        self._habitacion = habitacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_catastral(self) -> int:
        return self._id_catastral

    def get_casa(self) -> Casa:
        return self._casa

    def get_habitacion(self) -> Habitacion:
        return self._habitacion

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\entidades\usuarios
################################################################################

# ==============================================================================
# ARCHIVO 22/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/59: accion.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\accion.py
# ==============================================================================

"""
Entidad Accion.
"""

from datetime import date

class Accion:
    """Accion permitida a un usuario."""
    def __init__(self, id_accion: int, descripcion: str):
        self._id_accion = id_accion
        self._descripcion = descripcion

    def get_id_accion(self) -> int:
        return self._id_accion

    def get_descripcion(self) -> str:
        return self._descripcion


# ==============================================================================
# ARCHIVO 24/59: permiso_acceso.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\permiso_acceso.py
# ==============================================================================

"""
Entidad PermisoAcceso.
"""

from datetime import date

class PermisoAcceso:
    """Certificacion de acceso de un usuario."""
    def __init__(self, permitido: bool, fecha_emision: date, observaciones: str):
        self._permitido = permitido
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def is_permitido(self) -> bool:
        return self._permitido

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones


# ==============================================================================
# ARCHIVO 25/59: usuario.py
# Directorio: casa_inteligente\casa_inteligente_logic\entidades\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\entidades\usuarios\usuario.py
# ==============================================================================

"""
Entidad Usuario.
"""

from typing import List, Optional
from casa_inteligente_logic.entidades.usuarios.accion import Accion
from casa_inteligente_logic.entidades.usuarios.permiso_acceso import PermisoAcceso

class Usuario:
    """Representa un usuario de la casa."""
    def __init__(self, dni: int, nombre: str, acciones: List[Accion]):
        self._dni = dni
        self._nombre = nombre
        self._acciones = acciones
        self._permiso_acceso: Optional[PermisoAcceso] = None

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_acciones(self) -> List[Accion]:
        return self._acciones.copy()  # Defensive copy

    def get_permiso_acceso(self) -> Optional[PermisoAcceso]:
        return self._permiso_acceso

    def set_permiso_acceso(self, permiso: PermisoAcceso) -> None:
        self._permiso_acceso = permiso



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\excepciones
################################################################################

# ==============================================================================
# ARCHIVO 26/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\excepciones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 27/59: casa_inteligente_exception.py
# Directorio: casa_inteligente\casa_inteligente_logic\excepciones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\casa_inteligente_exception.py
# ==============================================================================

"""
Excepcion base para el sistema de casa inteligente.
"""

class CasaInteligenteException(Exception):
    """Clase base para excepciones del sistema."""
    def __init__(self, user_message: str, technical_message: str):
        super().__init__(f"{user_message} ({technical_message})")
        self._user_message = user_message
        self._technical_message = technical_message

    def get_user_message(self) -> str:
        return self._user_message

    def get_technical_message(self) -> str:
        return self._technical_message

    def get_full_message(self) -> str:
        return str(self)


# ==============================================================================
# ARCHIVO 28/59: mensajes_exception.py
# Directorio: casa_inteligente\casa_inteligente_logic\excepciones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\mensajes_exception.py
# ==============================================================================

"""
Centralizacion de mensajes de error para excepciones.
"""

# Operacion
USER_OPERACION_INVALIDA = "La operacion no es valida."
TECH_OPERACION_INVALIDA = "La operacion no se pudo completar."

# Persistencia
USER_PERSISTENCIA_ESCRITURA = "Error al guardar el registro."
TECH_PERSISTENCIA_ESCRITURA = "Fallo la operacion de escritura en disco."
USER_PERSISTENCIA_LECTURA = "Error al leer el registro."
TECH_PERSISTENCIA_LECTURA = "Fallo la operacion de lectura de disco."
USER_PERSISTENCIA_NO_ENCONTRADO = "El registro solicitado no existe."
TECH_PERSISTENCIA_NO_ENCONTRADO = "El archivo no fue encontrado en el directorio de datos."


# ==============================================================================
# ARCHIVO 29/59: operacion_invalida_exception.py
# Directorio: casa_inteligente\casa_inteligente_logic\excepciones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\operacion_invalida_exception.py
# ==============================================================================

"""
Excepcion para cuando una operacion no es valida.
"""

from casa_inteligente_logic.excepciones.casa_inteligente_exception import CasaInteligenteException
from casa_inteligente_logic.excepciones.mensajes_exception import (
    USER_OPERACION_INVALIDA,
    TECH_OPERACION_INVALIDA
)

class OperacionInvalidaException(CasaInteligenteException):
    """Lanzada cuando una operacion no es valida."""
    def __init__(self, message: str):
        super().__init__(
            USER_OPERACION_INVALIDA,
            f"{TECH_OPERACION_INVALIDA}: {message}"
        )


# ==============================================================================
# ARCHIVO 30/59: persistencia_exception.py
# Directorio: casa_inteligente\casa_inteligente_logic\excepciones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\excepciones\persistencia_exception.py
# ==============================================================================

"""
Excepcion para errores de persistencia.
"""

from enum import Enum
from casa_inteligente_logic.excepciones.casa_inteligente_exception import CasaInteligenteException

class TipoOperacion(Enum):
    LECTURA = "lectura"
    ESCRITURA = "escritura"

class PersistenciaException(CasaInteligenteException):
    """Lanzada cuando ocurren errores de I/O en persistencia."""
    def __init__(self, user_message: str, technical_message: str, nombre_archivo: str, tipo_operacion: TipoOperacion):
        super().__init__(user_message, f"{technical_message} en archivo: {nombre_archivo}")
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacion:
        return self._tipo_operacion



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones
################################################################################

# ==============================================================================
# ARCHIVO 31/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 32/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\factory
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/59: dispositivo_factory.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\factory
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\factory\dispositivo_factory.py
# ==============================================================================

"""
Factory para la creacion de dispositivos.
"""

from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

class DispositivoFactory:
    """Fabrica de dispositivos que encapsula la logica de creacion."""
    @staticmethod
    def crear_dispositivo(tipo: str, nombre: str) -> Dispositivo:
        factories = {
            "LuzInteligente": lambda: LuzInteligente(nombre, "Philips Hue"),
            "TermostatoInteligente": lambda: TermostatoInteligente(nombre)
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de dispositivo desconocido: {tipo}")

        return factories[tipo]()



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 34/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/59: observable.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\observable.py
# ==============================================================================

"""
Clase Observable generica para el patron Observer.
"""

from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento, self)


# ==============================================================================
# ARCHIVO 36/59: observer.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\observer
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\observer.py
# ==============================================================================

"""
Interfaz Observer generica para el patron Observer.
"""

from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.patrones.observer.observable import Observable
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para que un objeto sea notificable de cambios."""
    @abstractmethod
    def actualizar(self, evento: T, sender: 'Observable') -> None:
        """
        Recibe una actualizacion de un objeto observable.

        Args:
            evento: El evento que se ha producido.
        """
        pass



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 37/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\observer\eventos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 38/59: evento_sensor.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\observer\eventos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\observer\eventos\evento_sensor.py
# ==============================================================================

"""
Evento de sensor para el patron Observer.
"""

from datetime import datetime

class EventoSensor:
    """Representa un evento de un sensor."""
    def __init__(self, valor: float, unidad: str):
        self._valor = valor
        self._unidad = unidad
        self._timestamp = datetime.now()

    def get_valor(self) -> float:
        return self._valor

    def get_unidad(self) -> str:
        return self._unidad

    def get_timestamp(self) -> datetime:
        return self._timestamp



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 39/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\singleton
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 40/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\strategy
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/59: modo_operacion_strategy.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\strategy
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\modo_operacion_strategy.py
# ==============================================================================

"""
Interfaz para la estrategia de modo de operacion.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoOperacionStrategy(ABC):
    """Interfaz para definir algoritmos de modos de operacion."""
    @abstractmethod
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        pass



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 42/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/59: modo_dia_strategy.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\modo_dia_strategy.py
# ==============================================================================

"""
Estrategia para el modo dia.
"""

from casa_inteligente_logic.patrones.strategy.modo_operacion_strategy import ModoOperacionStrategy
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoDiaStrategy(ModoOperacionStrategy):
    """Enciende todas las luces."""
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        print("Activando modo dia...")
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.encender()
                print(f"Encendiendo {dispositivo.get_nombre()}")


# ==============================================================================
# ARCHIVO 44/59: modo_noche_strategy.py
# Directorio: casa_inteligente\casa_inteligente_logic\patrones\strategy\impl
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\patrones\strategy\impl\modo_noche_strategy.py
# ==============================================================================

"""
Estrategia para el modo noche.
"""

from casa_inteligente_logic.patrones.strategy.modo_operacion_strategy import ModoOperacionStrategy
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class ModoNocheStrategy(ModoOperacionStrategy):
    """Apaga todas las luces."""
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        print("Activando modo noche...")
        for dispositivo in habitacion.get_dispositivos():
            if isinstance(dispositivo, LuzInteligente):
                dispositivo.apagar()
                print(f"Apagando {dispositivo.get_nombre()}")



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios
################################################################################

# ==============================================================================
# ARCHIVO 45/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
################################################################################

# ==============================================================================
# ARCHIVO 46/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/59: dispositivo_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\dispositivo_service.py
# ==============================================================================

"""
Servicio base para todos los dispositivos.
"""

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo

class DispositivoService(ABC):
    """Servicio abstracto para operaciones de dispositivo."""
    def mostrar_datos(self, dispositivo: 'Dispositivo') -> None:
        print(f"Dispositivo: {type(dispositivo).__name__}")
        print(f"Nombre: {dispositivo.get_nombre()}")
        print(f"Encendido: {dispositivo.is_encendido()}")


# ==============================================================================
# ARCHIVO 48/59: dispositivo_service_registry.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\dispositivo_service_registry.py
# ==============================================================================

"""
Registro de servicios de dispositivo (Singleton y Registry).
"""

from threading import Lock
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente
from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente
from casa_inteligente_logic.servicios.dispositivos.luz_inteligente_service import LuzInteligenteService
from casa_inteligente_logic.servicios.dispositivos.termostato_inteligente_service import TermostatoInteligenteService

class DispositivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls() # Llama al constructor
        return cls._instance

    def _inicializar_servicios(self):
        self._luz_service = LuzInteligenteService()
        self._termostato_service = TermostatoInteligenteService()

        self._mostrar_datos_handlers = {
            LuzInteligente: self._mostrar_datos_luz,
            TermostatoInteligente: self._mostrar_datos_termostato
        }

    def mostrar_datos(self, dispositivo: Dispositivo) -> None:
        tipo = type(dispositivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](dispositivo)

    def _mostrar_datos_luz(self, dispositivo):
        return self._luz_service.mostrar_datos(dispositivo)

    def _mostrar_datos_termostato(self, dispositivo):
        return self._termostato_service.mostrar_datos(dispositivo)

# ==============================================================================
# ARCHIVO 49/59: luz_inteligente_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\luz_inteligente_service.py
# ==============================================================================

"""
Servicio para LuzInteligente.
"""

from casa_inteligente_logic.servicios.dispositivos.dispositivo_service import DispositivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.luz_inteligente import LuzInteligente

class LuzInteligenteService(DispositivoService):
    """Servicio para LuzInteligente."""

    def mostrar_datos(self, dispositivo: 'LuzInteligente') -> None:
        super().mostrar_datos(dispositivo)
        print(f"Marca: {dispositivo.get_marca()}")
        print(f"Brillo: {dispositivo.get_brillo()}% ")


# ==============================================================================
# ARCHIVO 50/59: termostato_inteligente_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\dispositivos
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\dispositivos\termostato_inteligente_service.py
# ==============================================================================

"""
Servicio para TermostatoInteligente.
"""

from casa_inteligente_logic.servicios.dispositivos.dispositivo_service import DispositivoService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from casa_inteligente_logic.entidades.dispositivos.termostato_inteligente import TermostatoInteligente

class TermostatoInteligenteService(DispositivoService):
    """Servicio para TermostatoInteligente."""

    def mostrar_datos(self, dispositivo: 'TermostatoInteligente') -> None:
        super().mostrar_datos(dispositivo)
        print(f"Temperatura: {dispositivo.get_temperatura()} C")



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\espacios
################################################################################

# ==============================================================================
# ARCHIVO 51/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/59: casa_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\casa_service.py
# ==============================================================================

"""
Servicio para Casa.
"""

from casa_inteligente_logic.entidades.espacios.casa import Casa
from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion

class CasaService:
    """Servicio para operaciones relacionadas con Casa."""
    def crear_casa_con_habitacion(
        self,
        id_catastral: int,
        domicilio: str,
        nombre_habitacion: str
    ) -> Casa:
        casa = Casa(id_catastral, domicilio)
        habitacion = Habitacion(nombre_habitacion)
        # Acoplamiento aqui, pero aceptable para este caso
        setattr(casa, '_habitacion', habitacion)
        return casa

    def get_habitacion(self, casa: Casa) -> Habitacion:
        return getattr(casa, '_habitacion')


# ==============================================================================
# ARCHIVO 53/59: habitacion_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\habitacion_service.py
# ==============================================================================

"""
Servicio para Habitacion.
"""

from casa_inteligente_logic.entidades.espacios.habitacion import Habitacion
from casa_inteligente_logic.patrones.factory.dispositivo_factory import DispositivoFactory
from casa_inteligente_logic.excepciones.operacion_invalida_exception import OperacionInvalidaException
from casa_inteligente_logic.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry

class HabitacionService:
    """Servicio para operaciones de Habitacion."""
    def __init__(self):
        self._dispositivo_service_registry = DispositivoServiceRegistry.get_instance()

    def instalar_dispositivo(self, habitacion: Habitacion, tipo: str, nombre: str) -> None:
        nuevo_dispositivo = DispositivoFactory.crear_dispositivo(tipo, nombre)
        habitacion.add_dispositivo(nuevo_dispositivo)

    def activar_modo(self, habitacion: Habitacion, modo) -> None:
        modo.ejecutar(habitacion)


# ==============================================================================
# ARCHIVO 54/59: registro_propiedad_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\espacios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\espacios\registro_propiedad_service.py
# ==============================================================================

"""
Servicio para RegistroPropiedad.
"""

import os
import pickle
from casa_inteligente_logic.entidades.espacios.registro_propiedad import RegistroPropiedad
from casa_inteligente_logic.servicios.dispositivos.dispositivo_service_registry import DispositivoServiceRegistry
from casa_inteligente_logic.excepciones.persistencia_exception import PersistenciaException, TipoOperacion
from casa_inteligente_logic.excepciones.mensajes_exception import (
    USER_PERSISTENCIA_ESCRITURA,
    TECH_PERSISTENCIA_ESCRITURA,
    USER_PERSISTENCIA_LECTURA,
    TECH_PERSISTENCIA_LECTURA,
    USER_PERSISTENCIA_NO_ENCONTRADO,
    TECH_PERSISTENCIA_NO_ENCONTRADO
)

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

class RegistroPropiedadService:
    """Servicio para persistencia y visualizacion de RegistroPropiedad."""
    def __init__(self):
        self._dispositivo_service_registry = DispositivoServiceRegistry.get_instance()

    def mostrar_datos(self, registro: RegistroPropiedad) -> None:
        print("REGISTRO DE PROPIEDAD")
        print("=================")
        print(f"Catastro:    {registro.get_id_catastral()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_casa().get_domicilio()}")
        print(f"Cantidad de dispositivos: {len(registro.get_habitacion().get_dispositivos())}")
        print("Listado de Dispositivos instalados")
        print("____________________________")
        for dispositivo in registro.get_habitacion().get_dispositivos():
            self._dispositivo_service_registry.mostrar_datos(dispositivo)
            print()

    def persistir(self, registro: RegistroPropiedad) -> None:
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{registro.get_propietario()}{EXTENSION_DATA}")

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente en {nombre_archivo}")
        except IOError as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_ESCRITURA,
                f"{TECH_PERSISTENCIA_ESCRITURA}: {e}",
                nombre_archivo,
                TipoOperacion.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> RegistroPropiedad:
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")

        if not os.path.exists(nombre_archivo):
            raise PersistenciaException(
                USER_PERSISTENCIA_NO_ENCONTRADO,
                TECH_PERSISTENCIA_NO_ENCONTRADO,
                nombre_archivo,
                TipoOperacion.LECTURA
            )

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
                print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
                return registro
        except (IOError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                USER_PERSISTENCIA_LECTURA,
                f"{TECH_PERSISTENCIA_LECTURA}: {e}",
                nombre_archivo,
                TipoOperacion.LECTURA
            )



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 55/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 56/59: casas_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\casas_service.py
# ==============================================================================

"""
Servicio para gestionar multiples casas.
"""

from typing import Dict, Type
from casa_inteligente_logic.entidades.espacios.registro_propiedad import RegistroPropiedad
from casa_inteligente_logic.entidades.dispositivos.dispositivo import Dispositivo
from casa_inteligente_logic.servicios.negocio.paquete import Paquete

class CasasService:
    """Servicio para operaciones de alto nivel en multiples casas."""
    def __init__(self):
        self._casas: Dict[int, RegistroPropiedad] = {}

    def add_casa(self, registro: RegistroPropiedad) -> None:
        self._casas[registro.get_id_catastral()] = registro

    def buscar_casa(self, id_catastral: int) -> RegistroPropiedad:
        if id_catastral not in self._casas:
            raise ValueError(f"Casa con catastro {id_catastral} no encontrada.")
        return self._casas[id_catastral]

    def desactivar_dispositivos(self, id_catastral: int, tipo_dispositivo: Type[Dispositivo]) -> Paquete:
        paquete = Paquete(tipo_dispositivo)
        dispositivos_desactivados = []

        for casa in self._casas.values():
            habitacion = casa.get_habitacion()
            dispositivos_en_habitacion = habitacion.get_dispositivos()
            
            for dispositivo in dispositivos_en_habitacion:
                if isinstance(dispositivo, tipo_dispositivo):
                    dispositivos_desactivados.append(dispositivo)
            
            # Remover dispositivos desactivados de la habitacion
            dispositivos_restantes = [d for d in dispositivos_en_habitacion if d not in dispositivos_desactivados]
            setattr(habitacion, '_dispositivos', dispositivos_restantes)

        for dispositivo in dispositivos_desactivados:
            paquete.agregar_dispositivo(dispositivo)

        print(f"DESACTIVANDO {len(dispositivos_desactivados)} unidades de {tipo_dispositivo}")
        return paquete


# ==============================================================================
# ARCHIVO 57/59: paquete.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\negocio
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\negocio\paquete.py
# ==============================================================================

"""
Clase generica para empaquetar dispositivos.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')

class Paquete(Generic[T]):
    """Caja generica para empaquetar un tipo de dispositivo."""
    _id_counter = 0

    def __init__(self, tipo_dispositivo: type):
        Paquete._id_counter += 1
        self._id_paquete = Paquete._id_counter
        self._tipo_dispositivo = tipo_dispositivo
        self._contenido: List[T] = []

    def agregar_dispositivo(self, dispositivo: T) -> None:
        if not isinstance(dispositivo, self._tipo_dispositivo):
            raise TypeError(f"Solo se pueden agregar dispositivos de tipo {self._tipo_dispositivo.__name__}")
        self._contenido.append(dispositivo)

    def get_contenido(self) -> List[T]:
        return self._contenido.copy()

    def mostrar_contenido_caja(self) -> None:
        print("Contenido de la caja:")
        print(f"  Tipo: {self._tipo_dispositivo.__name__}")
        print(f"  Cantidad: {len(self._contenido)}")
        print(f"  ID Paquete: {self._id_paquete}")



################################################################################
# DIRECTORIO: casa_inteligente\casa_inteligente_logic\servicios\usuarios
################################################################################

# ==============================================================================
# ARCHIVO 58/59: __init__.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\usuarios\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/59: usuario_service.py
# Directorio: casa_inteligente\casa_inteligente_logic\servicios\usuarios
# Ruta completa: C:\Users\Franco\Desktop\parcial2-diseno\casa_inteligente\casa_inteligente_logic\servicios\usuarios\usuario_service.py
# ==============================================================================

"""
Servicio para Usuario.
"""

from datetime import date
from casa_inteligente_logic.entidades.usuarios.usuario import Usuario
from casa_inteligente_logic.entidades.usuarios.permiso_acceso import PermisoAcceso

class UsuarioService:
    """Servicio para operaciones de Usuario."""
    def asignar_permiso_acceso(
        self,
        usuario: Usuario,
        permitido: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        permiso = PermisoAcceso(permitido, fecha_emision, observaciones)
        usuario.set_permiso_acceso(permiso)

    def ejecutar_acciones(self, usuario: Usuario, fecha: date) -> bool:
        permiso = usuario.get_permiso_acceso()
        if not permiso or not permiso.is_permitido():
            print(f"El usuario {usuario.get_nombre()} no tiene permiso para ejecutar acciones.")
            return False

        acciones_del_dia = usuario.get_acciones()
        
        for accion in acciones_del_dia:
            print(f"El usuario {usuario.get_nombre()} ejecuto la accion {accion.get_id_accion()} {accion.get_descripcion()}")
        
        return True



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 59
# Generado: 2025-11-04 16:23:11
################################################################################
