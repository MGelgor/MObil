import time
import os

def top_menu() :
	print ("###############################################################")
	print ("#      MObil                   ",time.asctime(),"     #")
	print ("###############################################################")

os_name = os.name
if os_name == 'posix' :
	os_clean = "clear"

def copadam_dansi() :
	time.sleep (2.5)
	print("\n\n\n\n\n   O ")
	print("  /|\ ")
	print(" / | \ ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print(" _/|\_ ")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n___O___")
	print("   |")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print(" _/|\_ ")
	print("   | ")
	print("  / \ ")
	print("  | |")
	print("  | |")
	time.sleep (0.2)
	os.system( os_clean )
	print("\n\n\n\n\n   O")
	print("  /|\ ")
	print(" / | \ ")
	print("  / \ ")
	print("  | |")
	print("  | |")
menu1=1
menu2=2
sifre=123
sifre=int(input("\n\n\n\n\nŞifreyi gir\n>"))

top_menu()
if sifre==123:
	while True :
		print("     __________________     ")
		time.sleep (0.04)
		print("    /                  \    ")
		time.sleep (0.04)
		print("    | Sisteme Girdiniz |    ")
		time.sleep (0.04)
		print("    \__________________/    ")
		time.sleep (1)
		menu1=int(input("Masaüstü: 1:Bilgisayarım, 2:Oyunlar, 3:Sistemi Kapat\n"))
		if menu1==1:
			print("--Bilgisayarım--")
			print("")
			time.sleep (1.5)
			print("1:Yerel Disk C")
			print("2:Yerel Disk D")
		elif menu1==2:
			print("--Oyunlar--")
			time.sleep (1.5)
			print("")
			print("1:Counter Strayk")
			print("2:Cop Adam.Avi")
			menu2=int(input(""))
			while menu2==2:
				copadam_dansi()
				break
			
		
		elif menu1==3:
			print("     __________________     ")
			time.sleep (0.04)
			print("    /                  \    ")
			time.sleep (0.04)
			print("    |    Görüşürüz     |    ")
			time.sleep (0.04)
			print("    \__________________/    ")
			time.sleep (1)
			
		
		
