# Historias de Usuario - Sistema de Casa Inteligente

**Proyecto**: CasaInteligente
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestion de Espacios y Dispositivos](#epic-1-gestion-de-espacios-y-dispositivos)
2. [Epic 2: Gestion de Dispositivos Inteligentes](#epic-2-gestion-de-dispositivos-inteligentes)
3. [Epic 3: Sistema de Automatizacion](#epic-3-sistema-de-automatizacion)
4. [Epic 4: Gestion de Usuarios](#epic-4-gestion-de-usuarios)
5. [Epic 5: Operaciones de la Casa](#epic-5-operaciones-de-la-casa)
6. [Epic 6: Persistencia y Auditoria](#epic-6-persistencia-y-auditoria)
7. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Espacios y Dispositivos

### US-001: Registrar Casa

**Como** propietario
**Quiero** registrar una casa con su direccion y numero de catastro
**Para** tener un control oficial de mis propiedades

#### Criterios de Aceptacion

- [x] El sistema debe permitir crear una casa con:
  - ID de catastro unico (numero entero positivo)
  - Domicilio de ubicacion (cadena de texto)
- [x] La casa debe poder modificarse posteriormente
- [x] El sistema debe validar que los datos sean consistentes

#### Detalles Tecnicos

**Clase**: `Casa` (`casa_inteligente_logic/entidades/espacios/casa.py`)
**Servicio**: `CasaService` (`casa_inteligente_logic/servicios/espacios/casa_service.py`)

---

### US-002: Crear Habitacion en Casa

**Como** administrador de la casa
**Quiero** crear una habitacion asociada a una casa
**Para** organizar los dispositivos en areas identificables

#### Criterios de Aceptacion

- [x] Una habitacion debe tener:
  - Nombre identificatorio unico
  - Lista de dispositivos (vacia al inicio)
  - Lista de usuarios (vacia al inicio)
- [x] La habitacion debe estar asociada a una casa valida

#### Detalles Tecnicos

**Clase**: `Habitacion` (`casa_inteligente_logic/entidades/espacios/habitacion.py`)
**Servicio**: `HabitacionService` (`casa_inteligente_logic/servicios/espacios/habitacion_service.py`)

---

## Epic 2: Gestion de Dispositivos Inteligentes

### US-003: Instalar Luces Inteligentes

**Como** usuario
**Quiero** instalar luces inteligentes de una marca especifica
**Para** controlar la iluminacion de una habitacion

#### Criterios de Aceptacion

- [x] Debe poder instalar multiples luces simultaneamente
- [x] Cada luz debe tener:
  - Marca (Philips Hue, Xiaomi, etc.)
  - Nivel de brillo inicial (50%)
- [x] Las luces deben crearse via Factory Method

#### Detalles Tecnicos

**Clase**: `LuzInteligente` (`casa_inteligente_logic/entidades/dispositivos/luz_inteligente.py`)
**Servicio**: `LuzInteligenteService` (`casa_inteligente_logic/servicios/dispositivos/luz_inteligente_service.py`)
**Factory**: `DispositivoFactory` (`casa_inteligente_logic/patrones/factory/dispositivo_factory.py`)

---

### US-004: Instalar Termostatos Inteligentes

**Como** usuario
**Quiero** instalar termostatos inteligentes
**Para** controlar la temperatura de una habitacion

#### Criterios de Aceptacion

- [x] Debe poder instalar multiples termostatos simultaneamente
- [x] Cada termostato debe tener:
  - Temperatura inicial (22 C)
- [x] Los termostatos deben crearse via Factory Method

#### Detalles Tecnicos

**Clase**: `TermostatoInteligente` (`casa_inteligente_logic/entidades/dispositivos/termostato_inteligente.py`)
**Servicio**: `TermostatoInteligenteService` (`casa_inteligente_logic/servicios/dispositivos/termostato_inteligente_service.py`)

---

## Epic 3: Sistema de Automatizacion

### US-005: Monitorear Temperatura en Tiempo Real

**Como** sistema de automatizacion
**Quiero** leer la temperatura de la habitacion cada 2 segundos
**Para** tomar decisiones de climatizacion

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer temperatura cada 2 segundos
  - Notificar a observadores cada vez que lee
- [x] Implementar patron Observer (Observable)

#### Detalles Tecnicos

**Clase**: `TemperaturaSensorTask` (`casa_inteligente_logic/automatizacion/sensores/temperatura_sensor_task.py`)
**Patron**: Observer (Observable[float])

---

### US-006: Monitorear Movimiento en Tiempo Real

**Como** sistema de automatizacion
**Quiero** detectar movimiento en la habitacion cada 1 segundo
**Para** tomar decisiones de seguridad o iluminacion

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Detectar movimiento (True/False) cada 1 segundo
  - Notificar a observadores cada vez que detecta un cambio
- [x] Implementar patron Observer (Observable)

#### Detalles Tecnicos

**Clase**: `MovimientoSensorTask` (`casa_inteligente_logic/automatizacion/sensores/movimiento_sensor_task.py`)
**Patron**: Observer (Observable[bool])

---

### US-007: Control Automatico de Climatizacion

**Como** sistema de automatizacion
**Quiero** encender el termostato automaticamente cuando la temperatura baja
**Para** mantener una temperatura confortable

#### Criterios de Aceptacion

- [x] El controlador debe:
  - Observar el sensor de temperatura
  - Encender el termostato si la temperatura es menor a 20 C
- [x] Implementar patron Observer (Observer[float])

#### Detalles Tecnicos

**Clase**: `ControlClimatizacionTask` (`casa_inteligente_logic/automatizacion/control/control_climatizacion_task.py`)
**Patron**: Observer (observa sensores)

---

## Epic 4: Gestion de Usuarios

### US-008: Registrar Usuario con Acciones Permitidas

**Como** administrador de la casa
**Quiero** registrar usuarios con acciones permitidas
**Para** controlar quien puede hacer que cosa

#### Criterios de Aceptacion

- [x] Un usuario debe tener:
  - DNI unico
  - Nombre completo
  - Lista de acciones permitidas
- [x] Las acciones deben tener:
  - ID unico
  - Descripcion de la accion

#### Detalles Tecnicos

**Clases**:
- `Usuario` (`casa_inteligente_logic/entidades/usuarios/usuario.py`)
- `Accion` (`casa_inteligente_logic/entidades/usuarios/accion.py`)

---

## Epic 5: Operaciones de la Casa

### US-009: Activar Modo de Operacion

**Como** usuario
**Quiero** activar un modo de operacion (ej. "Modo Noche")
**Para** cambiar el estado de varios dispositivos a la vez

#### Criterios de Aceptacion

- [x] Debe permitir especificar el modo a activar
- [x] El sistema debe aplicar las acciones del modo a todos los dispositivos
- [x] Usar el patron Strategy para los modos

#### Detalles Tecnicos

**Servicio**: `CasaService.activar_modo()`
**Estrategias**:
- `ModoNocheStrategy`
- `ModoDiaStrategy`

---

## Epic 6: Persistencia y Auditoria

### US-010: Persistir Registro de Propiedad en Disco

**Como** sistema
**Quiero** guardar el registro de la propiedad en disco
**Para** mantener datos permanentes

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Serializar `RegistroPropiedad` con Pickle
  - Guardar en `data/`
  - Nombre de archivo: `{propietario}.dat`
- [x] Si ocurre error, lanzar `PersistenciaException`

#### Detalles Tecnicos

**Servicio**: `RegistroPropiedadService.persistir()`

---

### US-011: Recuperar Registro de Propiedad desde Disco

**Como** sistema
**Quiero** recuperar un registro de propiedad guardado
**Para** restaurar el estado del sistema

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Deserializar archivo `.dat` con Pickle
  - Retornar `RegistroPropiedad`
- [x] Si archivo no existe o esta corrupto, lanzar `PersistenciaException`

#### Detalles Tecnicos

**Servicio**: `RegistroPropiedadService.leer_registro()`

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para DispositivoServiceRegistry

**Como** arquitecto
**Quiero** una unica instancia del registro de servicios de dispositivos
**Para** un estado consistente

#### Detalles Tecnicos
**Clase**: `DispositivoServiceRegistry`
**Patron**: Singleton

---

### US-TECH-002: Implementar Factory Method para Creacion de Dispositivos

**Como** arquitecto
**Quiero** centralizar la creacion de dispositivos
**Para** desacoplar el cliente de las clases concretas

#### Detalles Tecnicos
**Clase**: `DispositivoFactory`
**Patron**: Factory Method

---

### US-TECH-003: Implementar Observer Pattern para Sensores

**Como** arquitecto
**Quiero** notificar cambios de sensores de forma tipo-segura
**Para** un sistema de eventos desacoplado

#### Detalles Tecnicos
**Clases**: `Observable[T]`, `Observer[T]`
**Patron**: Observer

---

### US-TECH-004: Implementar Strategy Pattern para Modos de Operacion

**Como** arquitecto
**Quiero** algoritmos intercambiables para los modos de la casa
**Para** permitir diferentes comportamientos dinamicos

#### Detalles Tecnicos
**Interfaz**: `ModoOperacionStrategy`
**Patron**: Strategy

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimorfico

**Como** arquitecto
**Quiero** eliminar `isinstance()`
**Para** mejorar la mantenibilidad

#### Detalles Tecnicos
**Clase**: `DispositivoServiceRegistry`
**Patron**: Registry
