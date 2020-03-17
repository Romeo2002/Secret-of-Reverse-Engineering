import binascii

key = " %@$erwr#@$$!@#21$@^&*&(%rthdhdfw423%#DSgfY$%^#$%bre#B@@%#G3re"
Username = raw_input("Please enter your username:")
print Username
Username_len = len(Username)
print "Username Lenght is: %d" %Username_len
buffer = "".join(reversed(Username[0:4]))
buffer = int(binascii.hexlify(buffer),base=16)
print "Buffer %x"%buffer
if len(Username) <=1:
	i =1
	print int(binascii.hexlify(key[i]), base=16)
	EBX = (buffer - int(binascii.hexlify(key[i]), base=16))*int(binascii.hexlify(key[i]), base=16) 
	EBX = EBX & 0xffffffff
	print "%x"%EBX
	ESI = EBX
	EBX = EBX - (i)
	EBX = EBX + 0x4353543
	EBX = EBX & 0xffffffff
	ESI = ESI + EBX
	ESI = ESI & 0xffffffff
	password = ESI^int(binascii.hexlify(key[i]),base=16)
	print "%x"%password
	print "%d"%password
else:
	i = 4
	print int(binascii.hexlify(key[i]), base=16)
	EBX = (buffer - int(binascii.hexlify(key[i]), base=16))*int(binascii.hexlify(key[i]), base=16) 
	EBX = EBX & 0xffffffff
	print "EBX %x"%EBX
	ESI = EBX
	EBX = EBX - (i)
	EBX = EBX + 0x4353543
	EBX = EBX & 0xffffffff
	ESI = ESI + EBX
	ESI = ESI & 0xffffffff
	password = ESI^int(binascii.hexlify(key[i]),base=16)
	print "%x"%password
	print "%d"%password
