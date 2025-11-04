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
