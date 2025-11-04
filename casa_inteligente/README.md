# Sistema de Gestion de Casa Inteligente

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema de gestion para casas inteligentes que demuestra la implementacion de multiples patrones de diseno de software con un enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseno Implementados](#patrones-de-diseno-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalacion](#instalacion)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modulos del Sistema](#modulos-del-sistema)
- [Documentacion Tecnica](#documentacion-tecnica)
- [Testing y Validacion](#testing-y-validacion)
- [Contribucion](#contribucion)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **CasaInteligente** aborda los desafios de la domotica moderna, un dominio que requiere:

1. **Gestion de Multiples Tipos de Dispositivos**
   - Dispositivos de iluminacion (Luces Inteligentes)
   - Dispositivos climaticos (Termostatos Inteligentes)
   - Cada tipo con caracteristicas y estados particulares

2. **Monitoreo Ambiental en Tiempo Real**
   - Sensores de temperatura y movimiento que operan continuamente
   - Sistema de automatizacion basado en condiciones ambientales
   - Respuesta dinamica a cambios en el entorno

3. **Gestion de Usuarios y Permisos**
   - Control de usuarios con acciones permitidas
   - Asignacion y seguimiento de permisos de acceso

4. **Organizacion Espacial**
   - Estructuracion de la casa en habitaciones
   - Asociacion de dispositivos y usuarios a espacios concretos

5. **Persistencia y Trazabilidad**
   - Almacenamiento permanente de registros de la propiedad
   - Recuperacion de historicos para auditoria

### Actores del Sistema

- **Propietario**: Gestiona el registro de la propiedad, supervisa operaciones
- **Usuario**: Interactua con los dispositivos segun sus permisos
- **Sistema de Automatizacion**: Opera de forma autonoma basado en sensores

### Flujo de Operaciones Tipico

```
1. REGISTRO --> Se crea un registro de propiedad con una casa y habitacion
2. INSTALACION --> Se instalan dispositivos en la habitacion
3. MONITOREO --> Sensores detectan temperatura y movimiento continuamente
4. AUTOMATIZACION --> Sistema actua cuando se cumplen condiciones
5. MODOS --> Usuario activa modos (ej. Noche) que cambian el estado de los dispositivos
6. PERSISTENCIA --> Datos se guardan para auditoria futura
```

---

## Caracteristicas Principales

### Funcionalidades del Sistema

#### 1. Gestion de Dispositivos

- **Creacion dinamica** de 2 tipos de dispositivos mediante Factory Pattern
  - **LuzInteligente**: Con marca y nivel de brillo
  - **TermostatoInteligente**: Con control de temperatura

#### 2. Sistema de Automatizacion Inteligente

- **Sensores en tiempo real** (patron Observer)
  - Sensor de temperatura: lecturas cada 2 segundos
  - Sensor de movimiento: detecciones cada 1 segundo

- **Control automatizado condicional**
  - Se activa cuando:
    - Temperatura baja de un umbral
  - Control cada 2.5 segundos

- **Notificaciones de eventos**
  - Eventos de sensores a observadores suscritos
  - Sistema tipo-seguro con Generics (Observable[T])

#### 3. Gestion de Usuarios

- **Usuarios con acciones permitidas**
  - Permiso de acceso obligatorio para operar
  - Validacion automatica antes de ejecutar acciones

#### 4. Modos de Operacion

- **Activacion de modos** (patron Strategy)
  - **ModoNocheStrategy**: Apaga todas las luces
  - **ModoDiaStrategy**: Enciende todas las luces

#### 5. Persistencia de Datos

- **Serializacion con Pickle**
  - Guardado completo de RegistroPropiedad
  - Directorio configurable (default: `data/`)
  - Nombre de archivo: `{propietario}.dat`

- **Recuperacion de datos**
  - Lectura de registros persistidos
  - Manejo de excepciones especificas

---

## Arquitectura del Sistema

### Principios Arquitectonicos

El sistema esta disenado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una unica razon para cambiar
- **Open/Closed**: Abierto a extension, cerrado a modificacion
- **Liskov Substitution**: Subtipos intercambiables
- **Interface Segregation**: Interfaces especificas
- **Dependency Inversion**: Dependencias de abstracciones

### Separacion de Capas

```
+----------------------------------+
|        PRESENTACION              |
|  (main.py - Demostracion CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (CasasService, Paquete)         |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (HabitacionService, etc.)       |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Dispositivo, Habitacion, Usuario)|
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

---

## Patrones de Diseno Implementados

### 1. SINGLETON Pattern

**Ubicacion**: `casa_inteligente_logic/servicios/dispositivos/dispositivo_service_registry.py`

**Problema que resuelve**:
- Garantizar una unica instancia del registro de servicios de dispositivos
- Compartir estado entre todos los servicios del sistema

**Implementacion**:
```python
class DispositivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

---

### 2. FACTORY METHOD Pattern

**Ubicacion**: `casa_inteligente_logic/patrones/factory/dispositivo_factory.py`

**Problema que resuelve**:
- Creacion de dispositivos sin conocer clases concretas
- Encapsulacion de logica de construccion

**Implementacion**:
```python
class DispositivoFactory:
    @staticmethod
    def crear_dispositivo(tipo: str, nombre: str) -> Dispositivo:
        factories = {
            "LuzInteligente": lambda: LuzInteligente(nombre, "Philips Hue"),
            "TermostatoInteligente": lambda: TermostatoInteligente(nombre)
        }
        # ...
```

---

### 3. OBSERVER Pattern

**Ubicacion**: `casa_inteligente_logic/patrones/observer/`

**Problema que resuelve**:
- Notificacion automatica a multiples observadores
- Desacoplamiento entre sensores y controladores

**Implementacion**:
```python
class Observable(Generic[T], ABC):
    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento, self)
```

---

### 4. STRATEGY Pattern

**Ubicacion**: `casa_inteligente_logic/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de modos de operacion intercambiables
- Eliminar condicionales if/else

**Implementacion**:
```python
class ModoOperacionStrategy(ABC):
    @abstractmethod
    def ejecutar(self, habitacion: 'Habitacion') -> None:
        pass
```

---

## Requisitos del Sistema

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Modulos Estandar**: Solo biblioteca estandar de Python

---

## Instalacion

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd casa_inteligente
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Ejecutar Sistema

```bash
python main.py
```

---

## Uso del Sistema

### Ejemplo Basico

```python
from casa_inteligente_logic.servicios.espacios.casa_service import CasaService
from casa_inteligente_logic.servicios.espacios.habitacion_service import HabitacionService

# 1. Crear casa con habitacion
casa_service = CasaService()
casa = casa_service.crear_casa_con_habitacion(
    id_catastral=1,
    domicilio="Av. Siempre Viva 742",
    nombre_habitacion="Living"
)
habitacion = casa_service.get_habitacion(casa)

# 2. Instalar dispositivos (usa Factory Method)
habitacion_service = HabitacionService()
habitacion_service.instalar_dispositivo(habitacion, "LuzInteligente", "Luz del living")
habitacion_service.instalar_dispositivo(habitacion, "TermostatoInteligente", "Termostato del living")

# 3. Activar modo (usa Strategy)
from casa_inteligente_logic.patrones.strategy.impl.modo_noche_strategy import ModoNocheStrategy
habitacion_service.activar_modo(habitacion, ModoNocheStrategy())
```

---

## Estructura del Proyecto

```
casa_inteligente/
|
+-- main.py                          # Punto de entrada del sistema
+-- README.md                        # Este archivo
+-- USER_STORIES.md                  # Historias de usuario
|
+-- casa_inteligente_logic/          # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- dispositivos/
    |   +-- espacios/
    |   +-- usuarios/
    |
    +-- servicios/                   # Logica de negocio
    |   +-- dispositivos/
    |   +-- espacios/
    |   +-- negocio/
    |   +-- usuarios/
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- factory/
    |   +-- observer/
    |   +-- singleton/
    |   +-- strategy/
    |
    +-- automatizacion/              # Sistema de automatizacion con threads
    |   +-- sensores/
    |   +-- control/
    |
    +-- excepciones/                 # Excepciones personalizadas
```

---

## Modulos del Sistema

### Modulo: `entidades`
**Responsabilidad**: Objetos de dominio puros (DTOs).
**Clases principales**: `Dispositivo`, `Habitacion`, `Usuario`.

### Modulo: `servicios`
**Responsabilidad**: Logica de negocio del sistema.
**Servicios principales**: `HabitacionService`, `RegistroPropiedadService`, `UsuarioService`.

### Modulo: `patrones`
**Responsabilidad**: Implementaciones de patrones de diseno (Singleton, Factory, Observer, Strategy).

### Modulo: `automatizacion`
**Responsabilidad**: Sistema de automatizacion con threads.
**Componentes**: Sensores (`TemperaturaSensorTask`, `MovimientoSensorTask`) y Control (`ControlAutomatizacionTask`).

### Modulo: `excepciones`
**Responsabilidad**: Excepciones de dominio especificas.

---

## Documentacion Tecnica

### Convenciones de Codigo
- **PEP 8 Compliance**
- **Docstrings (Google Style)**
- **Type Hints**

### Configuracion de Constantes
Todas las constantes se encuentran en `constantes.py`.

---

## Testing y Validacion

El archivo `main.py` contiene un test de integracion completo que valida los patrones de diseno y las funcionalidades principales del sistema.

---

## Contribucion

### Como Agregar un Nuevo Tipo de Dispositivo

#### Paso 1: Crear Entidad
En `entidades/dispositivos/nuevo_dispositivo.py`.

#### Paso 2: Crear Servicio
En `servicios/dispositivos/nuevo_dispositivo_service.py`.

#### Paso 3: Registrar en Registry
En `dispositivo_service_registry.py`.

#### Paso 4: Registrar en Factory
En `dispositivo_factory.py`.

#### Paso 5: Usar el Nuevo Dispositivo
En `main.py` o donde sea necesario.

---

## Licencia

Este proyecto es de codigo abierto y esta disponible bajo la licencia MIT.
