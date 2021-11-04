"""
Nama    : Dino D. Ramadhan
NIM     : A11.2019.11709
Kel.    : A11.4318
Makul   : Struktur Data
Project : Klasemen Reguler Season NBA
"""


import os 
# Membuat class untuk node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.tim = data['tim']
        self.win = data['win']
        self.lose = data['lose']
        self.next_node = next_node

# Membuat class untuk linked list
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail= tail
            
    def tambahbelakang(self, data):
        # Inisialisasi node baru
        new_node = Node(data)
        # jika head masih kosong
        if (self.head is None):
            self.head=new_node
            self.tail=new_node
        else :
            self.tail.next_node=new_node
            self.tail=new_node

    # Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data :")
        print ("Node -> Next Node")
        current_node = self.head
        if (self.head is None):
            print("Data masih Kosong.")
        else:    
            while current_node is not None:
                print ("Tim : {} | Win : {} Lose : {}".format(current_node.tim, current_node.win, current_node.lose))
                if (current_node.next_node is not None) :
                  print (" -> ")
                current_node = current_node.next_node

    # Delete Dimana saja
    def deletedimanasaja(self):
        tim = input("Masukkan nama Tim yang ingin dihapus : ")
        if(self.head == None):  
            print("Data masih Kosong.")
            return
        current_node = self.head
        # Delete depan
        if (self.head.tim == tim) :
            self.head = self.head.next_node
            print ("Data {} berhasil dihapus.".format(tim))
            return
        # Delete belakang
        if (self.tail.tim == tim) :
            while current_node.next_node.next_node is not None :
                current_node = current_node.next_node
            current_node.next_node = self.tail.next_node
            self.tail = current_node
            print ("Data {} berhasil dihapus.".format(tim))
            return
        # Jika data tidak ditemukan
        while current_node.next_node is not None and current_node.next_node.tim != tim :
            current_node = current_node.next_node
            print ("Data {} tidak dtemukan.".format(tim))
        #Delete Tengah
        if (current_node.next_node is not None) :
            current_node.next_node = current_node.next_node.next_node
            print ("Data {} berhasil dihapus.".format(tim))
            
    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            # os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Tambah Belakang")
            print("2. Tampil Data")
            print("3. Hapus Data Dimana Saja")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda : ")))
            if(pilihan=="1"):
                # os.system("clear")
                tim = str(input("Masukan nama Tim : "))
                win = str(input("Masukan record win : "))
                lose = str(input("Masukan record lose : "))
                self.tambahbelakang({
                  "tim": tim,
                  "win": win,
                  "lose": lose
                })
            elif(pilihan=="2"):
                # os.system("clear")
                self.showData()
                x = input("")
            elif(pilihan=="3"):
                # os.system("clear")
                self.deletedimanasaja()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    # execute only if run as a script
    l = LinkedList()
    l.mainmenu()