import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/gabri/Ev_M4_DevOps/src')))

from usuario import Usuario

def test_actualizar_peso_correcto():
    usuario = Usuario("Ana", 65.5)
    usuario.actualizar_peso(63.0)
    assert usuario.peso == 63.0

def test_actualizar_peso_no_debe_restar_1kg():
    usuario = Usuario("Juan", 70.0)
    usuario.actualizar_peso(69.5)
    assert usuario.peso != 69.0