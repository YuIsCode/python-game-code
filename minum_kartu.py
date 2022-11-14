from contextlib import nullcontext
# Setiap pemain memiliki n kartu awal sebagai awalan (diinput oleh user)
# o Sisa pembagian kartu menjadi deck yang dihadapkan ke bawah
# o Di awal permainan, dibuka 1 kartu awalan dari deck sebagai acuan awal pemain
# o Setiap pemain membuang kartu yang jenisnya sama dengan kartu awalan tersebut
# o Pemain yang membuang kartu dengan nilai terbesar selanjutnya akan membuang kartu 
# sembarang (menjadi kartu acuan) yang pemain lainnya harus membuang dengan jenis 
# yang sama
# o Nilai dari tiap kartu diurutkan dari yang paling rendah ke yang paling tinggi sebagai 
# berikut: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, As
# o Jika pemain tidak memiliki kartu dengan jenis yang sama, maka akan mengambil kartu 
# dari deck hingga pemain memiliki kartu dengan jenis yang sama
# o Jika deck sudah habis dan pemain masih belum memiliki kartu dengan jenis yang sama, 
# maka pemain mengambil kartu yang dibuang oleh pemain lainnya
# o Pemenang dari permainan ini merupakan pemain yang menghabiskan kartu di tangannya 
# lebih awal.

import random
# mulai tampilan
print("\n \n")
print("PERMAINAN KARTU MINUMAN")
jumlah_kartu_tangan = input("Masukkan Jumlah Kartu Yang Di Bagi :")
# name1 = input("Masukkan Nama Mu  : ")
# name2 = input("Masukkan Nama Bot : ")

# nama tempat list kartu
list_kartu = []
kartu_bot = []
kartu_player = []
skor_player = 0
skor_bot = 0
kesempatan = "bandar"

# membuat list kartu
def kartu_yang_ada():
  for kartu in ("Sekop","Hati","Wajik","Keriting"):
    for peringkat in range(2,15):
      list_kartu.append((peringkat,kartu))

def nama_kartu(kartu):
  if kartu[0] <= 10 : rank = str(kartu[0])
  if kartu[0] == 11 : rank = "Jack"
  if kartu[0] == 12 : rank = "Queen"
  if kartu[0] == 13 : rank = "King"
  if kartu[0] == 14 : rank = "As"
  fullname = rank + " " + kartu[1]
  return fullname

def tambah_kartu_player():
    if len(list_kartu) > 0 :
        kartu_player.append(list_kartu[0])
        list_kartu.remove(list_kartu[0])
    else:
        print("Kartu Habis")
        return "Habis"

def daftar_kartu_player():
    print("\n Kartu Anda : " )
    i = 0
    for data in kartu_player:
        print(" " + str(i) + " --> " + nama_kartu(data));
        i+=1
    print()
    print("Pilihan :")
    print("1. Keluarkan Kartu ")
    print("2. Minum")
    print()

def daftar_kartu_bot():
  i = 0
  for data in kartu_bot:
    print(" " + str(i) + " --> " + nama_kartu(data));
    i+=1
  print()

def ambil_kartu_player(index):
  kartu = kartu_player[int(index)]
  kartu_player.remove(kartu_player[int(index)])
  return kartu

def ambil_kartu_bot(kartu_musuh):
  while True:
    for data in kartu_bot:
      cek = cek_kartu_bot(data,kartu_musuh)
      if cek == "1":
        kartu_bot.remove(data)
        return data
    ambil_kartu_bot_dari_deck()
        

def cek_kartu_bot(kartu_sendiri,kartu_musuh):
  if str(kartu_sendiri[1]) == str(kartu_musuh[1]): return "1"
  else : return "0"

def ambil_kartu_bot_dari_deck():
  if len(list_kartu) > 0 :
    kartu_bot.append(list_kartu[0])
    list_kartu.remove(list_kartu[0])
  else:
    print("Kartu Habis")
    return "Habis"


kartu_yang_ada()

# acak kartu yang ada
random.shuffle(list_kartu);

# pembagian kartu ke bot berdasarkan brapa kartu yang di bagi
for i in range(0,int(jumlah_kartu_tangan)):
  kartu_bot.append(list_kartu[i])
  list_kartu.remove(list_kartu[i])

# pembagian kartu ke player berdasarkan brapa kartu yang di bagi
for i in range(0,int(jumlah_kartu_tangan)):
  kartu_player.append(list_kartu[i])
  list_kartu.remove(list_kartu[i])

kartu_acuan = list_kartu[0]
list_kartu.remove(list_kartu[0])
kartu_pilihan_bot = ambil_kartu_bot(kartu_acuan)

def bagian_atas():
    print("\n\n==================================================================")
    print("Kartu Pertama : " + str(nama_kartu(kartu_acuan)))
    print("kartu Bot     : " + str(nama_kartu(kartu_pilihan_bot)))
    print("Total Kartu Saat Ini : " + str(len(list_kartu)))
    print("==================================================================")

def menang(kartu_player,kartu_bot):
    # cek menang + skor
    if kartu_player[0] > kartu_bot[0] : 
        print("Player menang")
        return "player"
    elif kartu_bot[0] > kartu_player[0]:
        print("Bot Menang")
        return "bot"
    else:
        print("Imbang")

while True:
    if kesempatan == "bandar":
        while True:
            bagian_atas()
            daftar_kartu_player()
            pilihan = input("Apa Yang Anda Lakukan :")
            
            if pilihan == "2" :
                tambah_kartu_player() 
                True
            elif pilihan == "1":
                while True :
                    keluar = input("\nMau Pake Kartu Yang Mana? :")
                    if int(keluar) < len(kartu_player) :
                        kartu_pilihan_player = ambil_kartu_player(keluar)
                        print("Kartu Pilihan Player : " + str(nama_kartu(kartu_pilihan_player)))
                        kesempatan = menang(kartu_pilihan_player,kartu_pilihan_bot)
                        break
                    else : True
                break
    elif kesempatan == "player" : 
        if len(kartu_player) > 0 :
            print("\n\n============================================================")
            print("Giliran anda untuk mengeluarkan kartu")
            print("Total Kartu Saat Ini : " + str(len(list_kartu)))
            while True:
                daftar_kartu_player()
                pilihan = input("Apa Yang Anda Lakukan :")
                
                if pilihan == "2" :
                    tambah_kartu_player() 
                    True
                elif pilihan == "1":
                    while True :
                        keluar = input("\nMau Pake Kartu Yang Mana? :")
                        if int(keluar) < len(kartu_player) :
                            kartu_pilihan_player = ambil_kartu_player(keluar)
                            break
                        else : True
                    break
            # bot memilih kartu
            kartu_acuan = kartu_pilihan_player
            kartu_pilihan_bot = ambil_kartu_bot(kartu_acuan)
            
            print("\n\n==================================================================")
            print("Kartu Pilihan Player : " + str(nama_kartu(kartu_pilihan_player)))
            print("Kartu Acuan : " + str(nama_kartu(kartu_acuan)))
            print("kartu Bot     : " + str(nama_kartu(kartu_pilihan_bot)))
            print("Total Kartu Saat Ini : " + str(len(list_kartu)))
            kesempatan = menang(kartu_pilihan_player,kartu_pilihan_bot)
            print("==================================================================")
        else:
            print("\n\n\n==========================================================")
            print("Permainan selesai Anda Menang")
            print("==========================================================")
            break
        
        
    else :
        if len(kartu_bot) > 0 :
            # bot memilih kartu
            kartu_acuan = kartu_bot.pop(0)
            kartu_pilihan_bot = kartu_acuan
            print("\n\n============================================================")
            print("Giliran bot untuk mengeluarkan kartu")
            print("\n\n==================================================================")
            print("Kartu Acuan : " + str(nama_kartu(kartu_acuan)))
            print("kartu Bot     : " + str(nama_kartu(kartu_pilihan_bot)))
            print("Total Kartu Saat Ini : " + str(len(list_kartu)))
            print("==================================================================")
            
            while True:
                print("Total Kartu Saat Ini : " + str(len(list_kartu)))
                daftar_kartu_player()
                pilihan = input("Apa Yang Anda Lakukan :")
                
                if pilihan == "2" :
                    tambah_kartu_player() 
                    True
                elif pilihan == "1":
                    while True :
                        keluar = input("\nMau Pake Kartu Yang Mana? :")
                        if int(keluar) < len(kartu_player) :
                            kartu_pilihan_player = ambil_kartu_player(keluar)
                            print("Kartu Pilihan Player : " + str(nama_kartu(kartu_pilihan_player)))
                            kesempatan = menang(kartu_pilihan_player,kartu_pilihan_bot)
                            break
                        else : True
                    break
        else:
            print("\n\n\n==========================================================")
            print("Permainan Selesai Bot Menang")
            print("==========================================================")
            break
        
    
    
    print("Total Kartu Player "+ str(len(kartu_player)) + "|" + str(len(kartu_bot)) +" Bot")
