import sys
import telnetlib
import time

TXT_WHITE="\033[1;37m"
TXT_GRAY="\033[0;37m"
TXT_CYAN="\033[0;36m"
TXT_PURPLE="\033[0;35m"
TXT_BLUE="\033[0;34m"
TXT_YELLOW="\033[0;33m"
TXT_BOLD_GREEN="\033[1;32m"
TXT_BOLD_RED="\033[0;31m"
TXT_DEFAULT="\033[0m"
TXT_BOLD_DEFAULT="\033[1;39m"
#stupid banner so you can show off to your friends
print("****************************************************")
print("* *                                              * *")
print("*                                                  *")
print("*          Selamat datang di SolusiSMS             *")
print("*                  by "+TXT_YELLOW+"lantip"+TXT_DEFAULT+"                       *")
print("*             "+TXT_BLUE+"http://lantip.net/"+TXT_DEFAULT+"                   *")
print("*                                                  *")
print("**                                                **")
print("****************************************************")
time.sleep(5)
HOST = "modem_ip_address"
PORT = "8223" #modem port
user = "username"
password = "password"
tn = telnetlib.Telnet(HOST,PORT)
tn.read_until("username: ")
tn.write(user+"\r")
tn.read_until("password: ")
tn.write(password+"\n")
tn.write("\r")
tn.read_until("]")
tn.write("module2"+"\r")
tn.read_until("got!! press 'ctrl-x' to release module 2.")
SELECTION = raw_input("What to do? \n(1) Send SMS, \n(2) Read ALL SMS, \n(3) Check Pulsa \n");
if SELECTION == "1":
	tn.write("ate1"+"\r")
	tn.read_until("0")
	tn.write("at+cmgf=1"+"\r")
	tn.read_until("0")
	NUMBER = raw_input("Enter phone number: ")
	#for i in range(5):
	tn.write("at+cmgw="+ NUMBER)
	tn.write("\r")
	#PESAN = """ini adalah pesan panjang tanpa raw input. apakah pesan ini sampai ke yang dikirim atau enggak, hanya tuhan yang tahu"""
	PESAN = raw_input("Isikan Pesan: ")
	tn.read_until("$",15)
	for letter in PESAN:
			tn.write(letter),
			time.sleep(.1)
	time.sleep(2)
	tn.write("\x1A")
	tn.write("\r")
	time.sleep(5)
	QUE = tn.read_until("$",15)
	#print QUE
	VAL = QUE.splitlines()
	SMS = VAL[1].replace('+CMGW: ','')
	tn.write("at+cmss="+SMS)
	tn.write("\r")
	tn.read_until("$",15)
	#print(VAL[1])
	#print('at+cmss='+SMS)
	tn.write("\x18")
	tn.write("\r")
	time.sleep(2)
	tn.read_until("release module 2 ...")
	tn.write("logout")
	tn.write("\r")
	print("Pesan yang dikirim: "+str(PESAN))
	print("Pesan dikirim ke nomer:" + TXT_BOLD_GREEN + NUMBER + TXT_DEFAULT + "")
	print(TXT_BOLD_DEFAULT + "message is on the way dude!"+TXT_DEFAULT)
elif SELECTION == "2":
	tn.write("ate1"+"\r")
	tn.read_until("0")
	tn.write("at+cmgf=1"+"\r")
	tn.read_until("0")
	tn.write("at+cmgl=ALL"+"\r")
	response=tn.read_until('$',20)
	tn.write("\x18")
	tn.write("\r")
	time.sleep(2)
	tn.read_until("release module 2 ...")
	tn.write("logout")
	tn.write("\r")
	print(response)
elif SELECTION == "3":
	tn.write("at+cusd=1,'*888#'"+"\r")
	response=tn.read_until("$",20)
	VAL = response.splitlines()
	print(response[0])
	tn.write("\x18")
	tn.write("\r")
	time.sleep(2)
	tn.read_until("release module 2 ...")
	tn.write("logout")
	tn.write("\r")
else:
	tn.write("\x18")
	tn.write("\r")
	time.sleep(2)
	tn.read_until("release module 2 ...")
	tn.write("logout")
	tn.write("\r")
	print("Perintah tidak dikenali")
tn.close
