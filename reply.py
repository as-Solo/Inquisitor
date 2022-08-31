import socket

palabra = '67:a6:c7:7b:32:fa'
palabra = palabra.split(':')

hex_mac = ''
for element in palabra:
    hex_mac = hex_mac + str(hex(int(element, 16)))
#return hex_mac
print (hex_mac.replace('0x', '\\x'))
#print (type(bytes.fromhex(palabra)))
#print (type(palabra))
#
#numero = int( palabra, 16)
#print (type(hex(numero)))
#print (hex(numero))
#
#print (numero)
#
#hexadec = hex(numero)
#print (hexadec)
#print (type(hexadec))
print (int('0x08', 16))

print (socket.inet_aton ('192.45.23.2' ))

'''
htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'
code ='\x08\x06'
ethernet1 = victimmac + attckmac + code
ethernet2 = gatewaymac +  attckmac + code
victim_ARP = ethernet1 + htype + protype + hsize + psize + opcode + attckmac + gatewayip + victimmac + victimip
gateway_ARP = ethernet2 + htype + protype + hsize + psize +opcode + attckmac + victimip + gatewaymac + gatewayip
nombre de la interfa de red segun MAC

gatewayip = socket.inet_aton ( gateway_ip )
victimip = socket.inet_aton ( victim_ip )
'''

def construct_reply(spoofer_mac, victim_mac, victim_ip, gateway_ip):
    
    htype = '\x00\x01'
    protype = '\x08\x00'
    hsize = '\x06'
    psize = '\x04'
    opcode = '\x00\x02'
    code ='\x08\x06'
    ethernet = client_mac + spoofer_mac + code
    
    arp_trace = ethernet + htype + protype + hsize + psize + opcode + spoofer_mac + gateway_ip + victim_mac + victim_ip
    
    return arp_trace
    

print(socket.inet_aton('172.18.0.2').hex())
print(socket.inet_aton('172.18.0.2').decode())
print(type(socket.inet_aton('172.18.0.2').hex()))