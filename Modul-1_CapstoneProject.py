#Capstone Project Modul 1 Fundamental Python 
#Project : Pemesanan Makanan/Resto Online.

#Justify Ester Pasaribu (JCDS 0406)

from tabulate import tabulate
from colorama import init, Fore, Style


# ----------------------------------------------------------------------------------------------------------------------
# DATA DUMMY UNTUK MENU MAKANAN
menu_makanan = [
    {"Id": 1, 
     "Nama": "Nasi Goreng", 
     "Harga": 20000, 
     "Kategori": "Main Course", 
     "Deskripsi": "Nasi dengan telur dan daging ayam", 
     "Vegetarian": False, 
     "Spicy": False, 
     "Porsi": 20},

    {"Id": 2, 
     "Nama": "Mie Goreng", 
     "Harga": 18000, 
     "Kategori": "Main Course", 
     "Deskripsi": "Mie dengan telur dan sayuran", 
     "Vegetarian": False, 
     "Spicy": True, 
     "Porsi": 15},

    {"Id": 3, 
     "Nama": "Es Teh Manis", 
     "Harga": 5000, 
     "Kategori": "Drinks", 
     "Deskripsi": "Es teh manis segar", 
     "Vegetarian": True, 
     "Spicy": False, 
     "Porsi": 30},

    {"Id": 4, 
     "Nama": "Salad Caesar", 
     "Harga": 25000, 
     "Kategori": "Appetizer", 
     "Deskripsi": "Selada segar dengan saus Caesar", 
     "Vegetarian": True, 
     "Spicy": False, 
     "Porsi": 10},

    {"Id": 5, 
     "Nama": "Kue Coklat", 
     "Harga": 10000, 
     "Kategori": "Dessert", 
     "Deskripsi": "Kue coklat lezat", 
     "Vegetarian": True, 
     "Spicy": False, 
     "Porsi": 12},
]

# ----------------------------------------------------------------------------------------------------------------------
# INISIALISASI TAMPILAN
init(autoreset=True)

# ----------------------------------------------------------------------------------------------------------------------
# DATA LOGIN USER & ADMIN
user_login = {"username": "user", "password": "user19"}
admin_login = {"username": "admin", "password": "admin19"}

# VARIABEL RIWAYAT PESANAN 
pesanan_user = [] #Menyimpan pesanan pengguna 
riwayat_pesanan_admin = [] #Menyimpan riwayat pesanan admin
pesanan_diproses = False #Menyimpan status apakah pesanan user sudah diproses oleh admin atau belum

def is_valid_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False
    
    # return input_str.isdigit()

def is_valid_input(input_str):
    return input_str.strip() != ""

def get_latest_menu_id():
    latest_id = max(menu_makanan, key=lambda x: x["Id"])["Id"]
    return latest_id + 1

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FUNGSI UNTUK MENAMPILKAN MENU MAKANAN (USER DAN ADMIN AKSES)
def tampilkan_menu_makanan():
    table = []
    print("\nDAFTAR MENU MAKANAN:")
    for menu in menu_makanan:
        table.append([menu["Id"], menu["Nama"], menu["Harga"], menu["Kategori"], menu["Deskripsi"], "Vegetarian" if menu["Vegetarian"] else "Non-Vegetarian", "Pedas" if menu["Spicy"] else "Tidak Pedas", menu["Porsi"]])
    print(tabulate(table, headers=["ID", "Nama", "Harga", "Kategori", "Deskripsi", "Status Vegetarian", "Status Spicy", "Porsi Stock"], tablefmt="pretty"))
    print()

# -----------------------------------------------------------------------------------------------------------------------
# FUNGSI UNTUK PESAN MAKANAN (USER AKSES)
def pesan_makanan():
    tampilkan_menu_makanan()

    pesanan_user = []  # Menyimpan pesanan pengguna
    lanjut_pesan = "ya"

    while lanjut_pesan.lower() == "ya":
        id_menu_str = input("Masukkan ID Menu yang ingin dipesan: ")

        # Menambahkan penanganan input kosong atau hanya Enter
        while not is_valid_input(id_menu_str):
            print(Fore.RED + Style.BRIGHT + "ID Menu tidak boleh kosong. Silakan input kembali.")
            id_menu_str = input("Masukkan ID Menu yang ingin dipesan: ")

        if not is_valid_integer(id_menu_str):
            print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
            continue

        id_menu = int(id_menu_str)

        menu_ditemukan = False  # Variabel untuk melacak apakah ID menu ditemukan

        for menu in menu_makanan:
            if menu["Id"] == id_menu:
                menu_ditemukan = True  # ID Menu Ditemukan
                jumlah_pesanan_str = input("Masukkan jumlah pesanan: ")

                if not is_valid_integer(jumlah_pesanan_str):
                    print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
                    break

                jumlah_pesanan = int(jumlah_pesanan_str)

                if menu["Porsi"] >= jumlah_pesanan:
                    menu["Porsi"] -= jumlah_pesanan
                    pesanan_user.append({"menu": menu, "jumlah_pesanan": jumlah_pesanan})
                    print(Fore.GREEN + Style.BRIGHT + "Pesanan Anda Berhasil, Silahkan Cek di Menu Riwayat Pesanan Anda!")
                else:
                    print(Fore.RED + Style.BRIGHT + "Pesanan anda gagal, menu tidak ditemukan atau jumlah pesanan melebihi stok hari ini!")
                break  # Keluar dari loop setelah menemukan menu

        # Setelah loop selesai, jika ID menu tidak ditemukan, tampilkan pesan kesalahan
        if not menu_ditemukan:
            print(Fore.RED + Style.BRIGHT + "ID Menu Tidak Ada, Silahkan input kembali!")

        while True:
            lanjut_pesan = input("Apakah Anda ingin menginput kembali ID menu? (ya/tidak): ").lower()
            if lanjut_pesan in ["ya", "tidak"]:
                break
            else:
                print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")

    if lanjut_pesan.lower() == "tidak":
        print(Fore.GREEN + Style.BRIGHT + "Oke, Anda tidak ingin pesan makanan!")

    return pesanan_user

# ----------------------------------------------------------------------------------------------------------------------
# FUNGSI UNTUK RIWAYAT PESANAN (USER AKSES)
def riwayat_pesanan(pesanan_user):
    global pesanan_diproses

    if pesanan_diproses:
        print(Fore.GREEN + Style.BRIGHT + "Tidak ada riwayat pesanan karena pesanan user sudah diproses oleh admin.")
        return 0  # Return 0 jika pesanan sudah diproses
    
    if not pesanan_user:
        print(Fore.GREEN + Style.BRIGHT + "Tidak ada riwayat pesanan.")
        return 0  # Return 0 jika tidak ada pesanan

    table = []
    total_harga = 0

    #variabel untuk menyimpan data pesanan dan pembayaran user
    pesanan_user_admin = []
    total_pembayaran_admin = 0 

    for pesanan in pesanan_user:
        menu = pesanan.get("menu", {}) 
        jumlah_pesanan = pesanan.get("jumlah_pesanan", 0) 
        harga_total = jumlah_pesanan * menu.get("Harga", 0) 
        table.append([menu["Id"], menu["Nama"], jumlah_pesanan, harga_total])
        total_harga += harga_total

        #menyimpan data pesanan dan pembayaran untuk admin
        pesanan_user_admin.append({"menu": menu, "jumlah_pesanan": jumlah_pesanan})
        total_pembayaran_admin += harga_total

    print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan dan Pembayaran:")
    print(tabulate(table, headers=["ID Menu Makanan", "Nama Menu Makanan", "Jumlah Pesanan", "Harga Total"], tablefmt="pretty"))

    while True:
        lanjutkan = input("User Yakin Ingin Melanjutkan Pesanan? (ya/tidak): ")
        if not is_valid_input(lanjutkan):
            print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan input kembali.")
            continue
        else:
            break

    if lanjutkan.lower() == "ya":
        if total_harga is not None and isinstance(total_harga, int) and total_harga > 0:
            # Menampilkan total_harga yang diperlukan untuk dibayar
            print(Fore.GREEN + Style.BRIGHT + f"Total Harga yang Harus Dibayarkan: {total_harga}")

            # Pemberitahuan saat pembayaran kurang dari total harga
            while True:
                pembayaran_str = input("Masukkan jumlah uang yang akan dibayarkan : ")
                
                if not is_valid_integer(pembayaran_str):
                    print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
                    continue
                
                pembayaran = int(pembayaran_str)
            
                if pembayaran == total_harga:
                    print(Fore.GREEN + Style.BRIGHT + "Yuhuuuu berhasil berhasil horee, admin proses ya!")

                    # Pesanan dan total pembayaran user tetap dapat diakses oleh admin
                    return pesanan_user_admin, total_pembayaran_admin
                
                    # # Setelah proses pembayaran selesai, kosongkan riwayat pesanan
                    # pesanan_user.clear()
                    # print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan Telah Dikosongkan Setelah Pembayaran.")
                    # break
                elif pembayaran > total_harga:
                    kembalian = pembayaran - total_harga
                    print(Fore.BLUE + Style.BRIGHT + f"Yuhuuuu berhasil berhasil horee, admin proses ya! Tapi uang anda ada kembaliannya sebanyak: {kembalian}")

                     # Pesanan dan total pembayaran user tetap dapat diakses oleh admin
                    return pesanan_user_admin, total_pembayaran_admin
                
                    # # Setelah proses pembayaran selesai, kosongkan riwayat pesanan
                    # pesanan_user.clear()
                    # print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan Telah Dikosongkan Setelah Pembayaran.")
                    # break
                else:
                    print(Fore.RED + Style.BRIGHT + "Sedih deh, uang anda kurang! Silahkan Input Kembali Pembayaran")
        else:
            print(Fore.RED + Style.BRIGHT + "Tidak ada pesanan untuk dibayar.")
            return 0 #Return 0 jika tidak ada pesanan
            
            # Setelah proses pembayaran selesai, kosongkan riwayat pesanan
            #pesanan_user.clear()
            #print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan Telah Dikosongkan Setelah Pembayaran.")
    elif lanjutkan.lower() == "tidak":
        print(Fore.RED + Style.BRIGHT + "Oke, pesanan Anda tidak akan dilanjutkan oleh admin")
        pesanan_user.clear()
        print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan Telah Dikosongkan Setelah Pembatalan Pesanan.")
        return 0  # Return 0 jika user tidak ingin melanjutkan pesanan.
    else:
        print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
        return 0  # Return 0 jika input tidak valid.
    
# FUNGSI UNTUK LIHAT RIWAYAT PESANAN USER (ADMIN AKSES)
def lihat_riwayat_pesanan_user(pesanan_user):
    global pesanan_diproses

    if not pesanan_user:
        print(Fore.GREEN + Style.BRIGHT + "Tidak ada riwayat pesanan dari user.")
        return
    
    table = []
    for pesanan in pesanan_user:
        menu = pesanan.get("menu", {}) 
        jumlah_pesanan = pesanan.get("jumlah_pesanan", 0) 
        table.append([menu.get("Id", ""), menu.get("Nama", ""), jumlah_pesanan])

    print(Fore.GREEN + Style.BRIGHT + "Riwayat Pesanan User:")
    print(tabulate(table, headers=["ID Menu Makanan", "Nama Menu Makanan", "Jumlah Pesanan"], tablefmt="pretty"))

    # Tanyakan apakah admin akan memproses atau menghapus pesanan user
    pilihan = input("Apakah admin akan memproses pesanan user? (proses/hapus): ")

    while not is_valid_input(pilihan):
        print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'proses' atau 'hapus'.")
        pilihan = input("Apakah admin akan memproses pesanan user? (proses/hapus): ")

    if pilihan.lower() == "proses":
        print(Fore.GREEN + Style.BRIGHT + "Pesanan User Sudah Berhasil Diproses Admin!")

        # Lakukan tindakan sesuai dengan kebutuhan setelah memproses pesanan
        #riwayat_pesanan_admin.extend(pesanan_user) #Menambahkan pesanan user ke riwayat pesanan admin
        pesanan_user.clear()
        pesanan_diproses = True #Setel nilai pesanan_diproses menjadi True setelah memproses pesanan user
        print(Fore.GREEN + Style.BRIGHT + "Tidak ada riwayat pesanan dari user karena sudah berhasil diproses oleh admin.")

    elif pilihan.lower() == "hapus":
        print(Fore.GREEN + Style.BRIGHT + "Pesanan User Telah Dihapus oleh Admin.")
        pesanan_user.clear()

    else:
        print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'proses' atau 'hapus'.")
    
# --------------------------------------------------------------------------------------------------------------------
# FUNGSI UNTUK TAMPILAN MENU ADMIN
def tampilkan_menu_admin():
    print('\n')
    print(Fore.BLUE + Style.BRIGHT + "Selamat Datang, Admin!")
    print('''Menu Admin:
          1. Lihat Menu Makanan
          2. Tambah Menu Makanan
          3. Ubah Menu Makanan
          4. Hapus Menu Makanan
          5. Lihat Riwayat Pesanan User
          6. Kembali ke Menu Awal
          7. Exit/Logout Admin
          ''')

# FUNGSI UNTUK TAMBAH MENU MAKANAN
def tambah_menu_makanan():
    print(Fore.BLUE + Style.BRIGHT + "Admin ingin tambah menu makanan?")
    pilihan = input("(ya/tidak): ").lower()
    
    while pilihan not in ['ya', 'tidak'] or pilihan == "":
        if pilihan == "":
            print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan input 'ya' atau 'tidak'.")
        else:
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
        pilihan = input("(ya/tidak): ").lower()

    if pilihan == "ya":
        new_menu = {}
        new_menu["Id"] = get_latest_menu_id()  # Menggunakan fungsi get_latest_menu_id
        new_menu["Nama"] = input("Nama Menu Makanan Baru: ")
        harga_str = input("Harga Menu Makanan Baru: ")
        while not is_valid_integer(harga_str):
            print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
            harga_str = input("Harga Menu Makanan Baru: ")
        new_menu["Harga"] = int(harga_str)
        new_menu["Kategori"] = input("Kategori Menu Makanan Baru: ")
        new_menu["Deskripsi"] = input("Deskripsi Menu Makanan Baru: ")
        
        # Input untuk Status Vegetarian
        status_vegetarian = input("Status Vegetarian (ya/tidak): ").lower()
        while status_vegetarian not in ['ya', 'tidak']:
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
            status_vegetarian = input("Status Vegetarian (ya/tidak): ").lower()
        new_menu["Vegetarian"] = status_vegetarian == "ya"
        
        # Input untuk Status Pedas
        status_pedas = input("Status Pedas (ya/tidak): ").lower()
        while status_pedas not in ['ya', 'tidak']:
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
            status_pedas = input("Status Pedas (ya/tidak): ").lower()
        new_menu["Spicy"] = status_pedas == "ya"
        
        porsi_str = input("Jumlah Porsi Stok Makanan Hari Ini: ")
        while not is_valid_integer(porsi_str):
            print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
            porsi_str = input("Jumlah Porsi Stok Makanan Hari Ini: ")
        new_menu["Porsi"] = int(porsi_str)
        
        menu_makanan.append(new_menu)
        print(Fore.GREEN + Style.BRIGHT + "Menu Makanan Berhasil Ditambah")
    else:
        print(Fore.BLUE + Style.BRIGHT + "Oke, Menu Makanan Tidak Ditambahkan")

# FUNGSI UNTUK UBAH MENU MAKANAN
def ubah_menu_makanan():

    tampilkan_menu_makanan() 

    while True:
        id_menu_input = input("Masukkan ID Menu yang ingin diubah (atau tekan Enter untuk kembali): ")
        
        if is_valid_input(id_menu_input):
            id_menu = int(id_menu_input)
            
            for menu in menu_makanan:
                if menu["Id"] == id_menu:
                    ubah_kolom_menu(menu)
                    print(Fore.GREEN + Style.BRIGHT + "Menu Makanan Berhasil Diubah")
                    return
            print(Fore.RED + Style.BRIGHT + "ID Menu Makanan Tidak Ditemukan")
        else:
            print(Fore.YELLOW + Style.BRIGHT + "Input tidak valid. Masukkan ID Menu atau tekan Enter untuk kembali.")
            return

def ubah_kolom_menu(menu):
    print('''\nPilih kolom/field yang ingin diubah:
          1. Nama Menu
          2. Harga Menu
          3. Kategori Menu
          4. Deskripsi Menu
          5. Status Vegetarian
          6. Status Pedas
          7. Jumlah Porsi Stok Makanan Hari ini
          ''')
    
    pilihan_kolom = input("Masukkan nomor kolom yang ingin diubah: ")

    if pilihan_kolom == "1":
        menu["Nama"] = input(f"Nama Menu ({menu['Nama']}): ")

    elif pilihan_kolom == "2":
        harga_input = input(f"Harga Menu ({menu['Harga']}): ")
        while not is_valid_input(harga_input) or not is_valid_integer(harga_input):
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Harap masukkan angka.")
            harga_input = input(f"Harga Menu ({menu['Harga']}): ")
        menu["Harga"] = int(harga_input)

    elif pilihan_kolom == "3":
        menu["Kategori"] = input(f"Kategori Menu ({menu['Kategori']}): ")

    elif pilihan_kolom == "4":
        menu["Deskripsi"] = input(f"Deskripsi Menu ({menu['Deskripsi']}): ")

    elif pilihan_kolom == "5":
        status_vegetarian = input("Status Vegetarian (ya/tidak): ").lower()
        while status_vegetarian not in ['ya', 'tidak']:
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
            status_vegetarian = input("Status Vegetarian (ya/tidak): ").lower()
        menu["Vegetarian"] = status_vegetarian == "ya"

    elif pilihan_kolom == "6":
        status_pedas = input("Status Pedas (ya/tidak): ").lower()
        while status_pedas not in ['ya', 'tidak']:
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
            status_pedas = input("Status Pedas (ya/tidak): ").lower()
        menu["Spicy"] = status_pedas == "ya"

    elif pilihan_kolom == "7":
        porsi_input = input(f"Jumlah Porsi Stok Makanan Hari Ini ({menu['Porsi']}): ")
        while not is_valid_input(porsi_input) or not is_valid_integer(porsi_input):
            print(Fore.RED + Style.BRIGHT + "Input tidak valid. Harap masukkan angka.")
            porsi_input = input(f"Jumlah Porsi Stok Makanan Hari Ini ({menu['Porsi']}): ")
        menu["Porsi"] = int(porsi_input)

    else:
        print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan pilih nomor kolom yang valid.")
        ubah_kolom_menu(menu)
        
# FUNGSI UNTUK HAPUS MENU MAKANAN
def hapus_menu_makanan():

    # CEK APAKAH TERDAFTAR MENU MAKANAN YANG INGIN DIHAP
    tampilkan_menu_makanan()

    id_menu_input = input("Masukkan ID Menu yang ingin dihapus (atau ketik 'skip' untuk batal): ")

    while not is_valid_input(id_menu_input) or (id_menu_input.lower() == 'skip'):
        if not is_valid_input(id_menu_input):
            print(Fore.RED + Style.BRIGHT + "ID Menu tidak boleh kosong.")
        else:
            print(Fore.BLUE + Style.BRIGHT + "Penghapusan Menu Makanan dibatalkan.")
            return

        id_menu_input = input("Masukkan ID Menu yang ingin dihapus (atau ketik 'skip' untuk batal): ")

    while not is_valid_integer(id_menu_input):
        print(Fore.RED + Style.BRIGHT + "Hanya Boleh Type Data Integer atau Input Dalam Bentuk Angka Integer.")
        id_menu_input = input("Masukkan ID Menu yang ingin dihapus: ")
    id_menu = int(id_menu_input)

    # Cek apakah ID menu yang dimasukkan oleh admin ada dalam database
    menu_ditemukan = False
    for menu in menu_makanan:
        if menu["Id"] == id_menu:
            menu_ditemukan = True
            konfirmasi = input(f"Yakin Ingin Menghapus Menu '{menu['Nama']}'? (ya/tidak): ").lower()
            while konfirmasi not in ['ya', 'tidak']:
                print(Fore.RED + Style.BRIGHT + "Input tidak valid. Silakan input 'ya' atau 'tidak'.")
                konfirmasi = input(f"Yakin Ingin Menghapus Menu '{menu['Nama']}'? (ya/tidak): ").lower()

            if konfirmasi == "ya":
                menu_makanan.remove(menu)
                print(Fore.GREEN + Style.BRIGHT + "Menu Makanan Berhasil Dihapus dari Database")
            else:
                print(Fore.BLUE + Style.BRIGHT + "Oke, Data Menu Makanan Tidak Jadi Dihapus")

    # Jika ID menu tidak ditemukan, berikan peringatan
    if not menu_ditemukan:
        print(Fore.RED + Style.BRIGHT + "ID Menu Makanan Tidak Ditemukan. Silahkan Coba Lagi.")

# --------------------------------------------------------------------------------------------------------------------
# FUNGSI UTAMA PROGRAM 
def main():
    global pesanan_user, riwayat_pesanan_admin

    print(Fore.CYAN + Style.BRIGHT + "\nSelamat Datang di Program Restoran Online")
    while True:
        print(Fore.CYAN + Style.BRIGHT + 
              '''Pilihan: 
              1. Login
              2. Logout
              ''')
        pilihan = input("Pilih (1/2): ").strip()

        if not is_valid_input(pilihan):
            print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan coba lagi.")
            continue

        if pilihan == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if not is_valid_input(username) or not is_valid_input(password):
                print(Fore.RED + Style.BRIGHT + "Username dan password tidak boleh kosong. Silakan coba lagi.")
                continue

            if username == user_login["username"] and password == user_login["password"]:
                print(Fore.BLUE + Style.BRIGHT + f"\nSelamat Datang, {username}!")
                
                while True:
                    print(Fore.BLUE + Style.BRIGHT + 
                          '''Menu User:
                          1. Lihat Menu Makanan
                          2. Pesan Makanan
                          3. Riwayat Pesanan dan Pembayaran
                          4. Kembali ke Menu Awal
                          5. Logout/Exit
                          ''')
                    pilihan_user = input("Pilih Menu User (1/2/3/4/5): ").strip()

                    if not is_valid_input(pilihan_user):
                        print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan coba lagi.")
                        continue

                    if pilihan_user == "1":
                        tampilkan_menu_makanan()

                    elif pilihan_user == "2":
                        pesanan = pesan_makanan()
                        if pesanan:
                            pesanan_user.extend(pesanan) #Menambahkan pesanan ke daftar pesanan pengguna 

                    elif pilihan_user == "3":
                        if not pesanan_user:
                            print(Fore.RED + Style.BRIGHT + "Tidak ada riwayat pesanan. Silakan pesan makanan terlebih dahulu.")
                            continue  
                        total_harga = riwayat_pesanan(pesanan_user)
                        if total_harga is not None and isinstance(total_harga, int) and total_harga > 0:
                            total_harga = 0

                    elif pilihan_user == "4":
                        break

                    elif pilihan_user == "5":
                        print(Fore.GREEN + Style.BRIGHT + "Terimakasih sudah mencoba program ini!")
                        return
                    
            elif username == admin_login["username"] and password == admin_login["password"]:
                while True:
                    tampilkan_menu_admin()
                    pilihan_admin = input("Pilih Menu Admin (1/2/3/4/5/6/7): ").strip()

                    if not is_valid_input(pilihan_admin):
                        print(Fore.RED + Style.BRIGHT + "Input tidak boleh kosong. Silakan coba lagi.")
                        continue

                    if pilihan_admin == "1":
                        tampilkan_menu_makanan()

                    elif pilihan_admin == "2":
                        tambah_menu_makanan()

                    elif pilihan_admin == "3":
                        ubah_menu_makanan()

                    elif pilihan_admin == "4":
                        hapus_menu_makanan()

                    elif pilihan_admin == "5":
                        lihat_riwayat_pesanan_user(pesanan_user)

                        # tampilkan_menu_admin()
                    elif pilihan_admin == "6":
                        break

                    elif pilihan_admin == "7":
                        print(Fore.GREEN + Style.BRIGHT + "Terimakasih sudah mencoba program ini!")
                        return
            else:
                print(Fore.RED + Style.BRIGHT + "Login Gagal, Cek Kembali Username dan Password Anda!")
                
        elif pilihan == "2":
            print(Fore.GREEN + Style.BRIGHT + "Terimakasih sudah mencoba program ini!")
            return

# PANGGIL MAIN FUNCTION SAAT MENJALANI PROGRAM
if __name__ == "__main__":
    main()
