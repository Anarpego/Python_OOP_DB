from orden import Orden
from computadora import Computadora
from monitor import Monitor
from dispositivo_entrada import DispositivoEntrada
from raton import Raton
from teclado import Teclado

teclado = Teclado('hp', 'usb')
raton   = Raton('hp', 'usb')
monitor = Monitor('hp', '15 pulgadas')

computadoraHp = Computadora('HP', monitor, teclado, raton)

tecladoDell = Teclado('Dell', 'usb')
ratonDell   = Raton('Dell', 'usb')
monitorDell = Monitor('Dell', '15 pulgadas')

computadoraDell = Computadora('Dell', monitorDell, tecladoDell, ratonDell)

tecladoMsi = Teclado('msi', 'usb')
ratonMsi  = Raton('msi', 'usb')
monitorMsi = Monitor('msi', '15 pulgadas')

computadoraMsi = Computadora('Msi', monitorMsi, tecladoMsi, ratonMsi)


computadoraArmada  = Computadora('Armada', monitorMsi, teclado, ratonDell)

computadoras1 = [computadoraHp, computadoraDell]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadoraArmada)
print(orden1)

computadoras2 = [computadoraArmada, computadoraMsi, computadoraDell]
orden2 = Orden(computadoras2)
print(orden2)