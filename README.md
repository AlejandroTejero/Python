# Python - Tactical Battle + Practicas

> No se requiere entorno virtual ni instalación de dependencias externas. Ejecutar con **Python 3**.

---

## Estructura del proyecto

Dentro del ZIP/proyecto encontrarás:
- `Apredizaje/` → ejercicios y pruebas (no es la práctica final).
- `TacticalBattle/` → Practica final, simulacion del juego tocado y hundido.

---

## Tactical Battle — Juego local (sin red)

### ¿Qué es?
Versión local del juego. Dos jugadores juegan por turnos en la misma máquina/terminal.

### Cómo ejecutar y ejemplo de ejecucción

```bash
python3 servidor.py <PUERTO> <PARTIDAS_SIMULTANEAS> <FICHERO_RANKING>
python3 servidor.py 5000 1 ranking_simple.txt


python3 cliente.py <IP_SERVIDOR> <PUERTO>
python3 cliente.py 127.0.0.1 5000

python3 cliente.py <IP_SERVIDOR> <PUERTO>
python3 cliente.py 127.0.0.1 5001
```
