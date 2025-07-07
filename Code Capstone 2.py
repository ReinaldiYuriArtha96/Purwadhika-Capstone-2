# Sistem Manajemen Nilai Siswa SMA Capstone 2 Final - Final
from tabulate import tabulate 
# Untuk menampilkan tabel data

# Data Admin (1)
data_admin = {
    '00001': 'Admin1',
    '00002': 'Admin2',
    '00003': 'Admin3',
    '00004': 'Admin4',
    '00005': 'Admin5'
}

# Data Siswa Awal (2)
data_siswa = [
    {'nis': '10000', 'nama': 'Kemal', 'kelas': 'X IPA 2', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 99, 'tugas_2': 98, 'tugas_3': 88, 'uts': 60, 'uas': 89},
    {'nis': '10001', 'nama': 'Maudy', 'kelas': 'X IPS 2', 'jenis_kelamin': 'Perempuan', 'tugas_1': 86, 'tugas_2': 58, 'tugas_3': 79, 'uts': 74, 'uas': 79},
    {'nis': '10002', 'nama': 'Robert', 'kelas': 'X IPS 2', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 80, 'tugas_2': 81, 'tugas_3': 91, 'uts': 94, 'uas': 94},
    {'nis': '10003', 'nama': 'Eka', 'kelas': 'X IPA 1', 'jenis_kelamin': 'Perempuan', 'tugas_1': 89, 'tugas_2': 87, 'tugas_3': 76, 'uts': 80, 'uas': 85},
    {'nis': '10004', 'nama': 'Yoga', 'kelas': 'X IPS 1', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 45, 'tugas_2': 65, 'tugas_3': 72, 'uts': 68, 'uas': 58},
    {'nis': '10005', 'nama': 'Fiona', 'kelas': 'X IPA 1', 'jenis_kelamin': 'Perempuan', 'tugas_1': 77, 'tugas_2': 85, 'tugas_3': 78, 'uts': 80, 'uas': 90},
    {'nis': '10006', 'nama': 'Yuri', 'kelas': 'X IPA 3', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 84, 'tugas_2': 90, 'tugas_3': 92, 'uts': 93, 'uas': 95},
    {'nis': '10007', 'nama': 'Mia', 'kelas': 'X IPS 3', 'jenis_kelamin': 'Perempuan', 'tugas_1': 64, 'tugas_2': 61, 'tugas_3': 69, 'uts': 70, 'uas': 75},
    {'nis': '10008', 'nama': 'Anton', 'kelas': 'X IPA 2', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 55, 'tugas_2': 60, 'tugas_3': 62, 'uts': 63, 'uas': 66},
    {'nis': '10009', 'nama': 'Jeni', 'kelas': 'X IPS 2', 'jenis_kelamin': 'Perempuan', 'tugas_1': 70, 'tugas_2': 65, 'tugas_3': 68, 'uts': 72, 'uas': 73},
    {'nis': '10010', 'nama': 'Otniel', 'kelas': 'X IPA 3', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 48, 'tugas_2': 51, 'tugas_3': 53, 'uts': 50, 'uas': 45},
    {'nis': '10011', 'nama': 'Nadia', 'kelas': 'X IPS 3', 'jenis_kelamin': 'Perempuan', 'tugas_1': 93, 'tugas_2': 91, 'tugas_3': 95, 'uts': 89, 'uas': 90},
    {'nis': '10012', 'nama': 'Jafar', 'kelas': 'X IPA 1', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 75, 'tugas_2': 77, 'tugas_3': 79, 'uts': 76, 'uas': 78},
    {'nis': '10013', 'nama': 'Adhya', 'kelas': 'X IPA 2', 'jenis_kelamin': 'Perempuan', 'tugas_1': 82, 'tugas_2': 80, 'tugas_3': 85, 'uts': 87, 'uas': 84},
    {'nis': '10014', 'nama': 'Dewo', 'kelas': 'X IPS 1', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 91, 'tugas_2': 88, 'tugas_3': 85, 'uts': 90, 'uas': 92},
    {'nis': '10015', 'nama': 'Lintang', 'kelas': 'X IPS 2', 'jenis_kelamin': 'Perempuan', 'tugas_1': 67, 'tugas_2': 70, 'tugas_3': 72, 'uts': 68, 'uas': 65},
    {'nis': '10016', 'nama': 'Fikar', 'kelas': 'X IPA 3', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 40, 'tugas_2': 45, 'tugas_3': 50, 'uts': 48, 'uas': 42},
    {'nis': '10017', 'nama': 'Metha', 'kelas': 'X IPS 3', 'jenis_kelamin': 'Perempuan', 'tugas_1': 74, 'tugas_2': 72, 'tugas_3': 76, 'uts': 75, 'uas': 78},
    {'nis': '10018', 'nama': 'Josua', 'kelas': 'X IPA 1', 'jenis_kelamin': 'Laki-laki', 'tugas_1': 95, 'tugas_2': 97, 'tugas_3': 94, 'uts': 96, 'uas': 98},
    {'nis': '10019', 'nama': 'Mare', 'kelas': 'X IPA 2', 'jenis_kelamin': 'Perempuan', 'tugas_1': 58, 'tugas_2': 61, 'tugas_3': 64, 'uts': 60, 'uas': 62},
]

# FUNGSI HITUNG NILAI AKHIR (3)
def hitung_nilai_akhir(t1, t2, t3, uts, uas):
    return round((t1 * 0.1 + t2 * 0.1 + t3 * 0.1 + uts * 0.2 + uas * 0.5), 1)

# Fungsi KONVERSI NILAI AKHIR ke GRADE (4)
def konversi_grade(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 55:
        return 'D'
    else:
        return 'E'

# Fungsi STATUS KELULUSAN (5)
def status_lulus(grade):
    return 'Lulus' if grade in ['A', 'B', 'C'] else 'Remedial'


# Fungsi Proses otomatis nilai akhir dan grade (6)
for s in data_siswa:
    s['nilai_akhir'] = hitung_nilai_akhir(s['tugas_1'], s['tugas_2'], s['tugas_3'], s['uts'], s['uas'])
    s['grade'] = konversi_grade(s['nilai_akhir'])
    s['status'] = status_lulus(s['grade'])

 
# Fungsi Tambah Data Siswa (7)

def tambah_siswa(data):
    print("\n=== Tambah Data Siswa ===")
    #Input & Validasi NIS
    nis = input("Masukkan NIS (max 5 digit angka): ")
    if not nis.isdigit() or len(nis) > 5:
        print("NIS tidak valid.")
        return
    if any(s['nis'] == nis for s in data):
        print("NIS sudah terdaftar.")
        return
    #Input Data Pribadi
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    jenis_kelamin = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan): ")

    try:
        # Input Nilai – Validasi Range
        def input_nilai(nama_nilai):
            while True:
                nilai = input(f"Nilai {nama_nilai} (0-100): ")
                if not nilai.isdigit():
                    print("Wajib berupa angka.")
                    continue
                nilai = int(nilai)
                if 0 <= nilai <= 100:
                    return nilai
                else:
                    print("Nilai wajib antara 0 dan 100.")

        t1 = input_nilai("Tugas 1")
        t2 = input_nilai("Tugas 2")
        t3 = input_nilai("Tugas 3")
        uts = input_nilai("UTS")
        uas = input_nilai("UAS")

    except Exception as e:
        print("Terjadi kesalahan saat input nilai:", e)
        return

    # Perhitungan Otomatis (Jika Lengkap)
    if all(n != 0 for n in [t1, t2, t3, uts, uas]):
        nilai_akhir = hitung_nilai_akhir(t1, t2, t3, uts, uas)
        grade = konversi_grade(nilai_akhir)
        status = status_lulus(grade)
    else:
        nilai_akhir = None
        grade = "-"
        status = "-"
    # Menyimpan ke Database (List)
    data.append({
        'nis': nis,
        'nama': nama,
        'kelas': kelas,
        'jenis_kelamin': jenis_kelamin,
        'tugas_1': t1,
        'tugas_2': t2,
        'tugas_3': t3,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir,
        'grade': grade,
        'status': status
    })

    print("Data siswa berhasil ditambahkan. Terimakasih!")
    print("Nilai siswa belum dilengkapi. Grade dan status  muncul jika semua nilai sudah diisi.")
    row = [[
    nama, kelas, jenis_kelamin, t1, t2, t3, uts, uas,
    nilai_akhir if nilai_akhir is not None else "-", grade, status
    ]]
    headers = ["Nama", "Kelas", "JK", "Tugas 1", "Tugas 2", "Tugas 3", "UTS", "UAS", "Nilai Akhir", "Grade", "Status"]
    print("\nData Siswa Baru:")
    #Output Konfirmasi (Dengan Tabel)
    print(tabulate(row, headers=headers, tablefmt="grid"))

# Fungsi READ – Menampilkan Semua Data Siswa (8)
def tampilkan_semua(data):
    #Cek Apakah Data Kosong
    if not data:
        print("\nTidak ada data siswa.")
        return
    #Persiapan Header Tabel
    print("\n=== Data Siswa ===")
    header = ["NIS", "Nama", "Kelas", "JK", "Tugas 1", "Tugas 2", "Tugas 3", "UTS", "UAS", "Nilai Akhir", "Grade", "Status"]
    table = []
    for s in data:
        #Isi Tabel Baris per Baris
        table.append([
            s['nis'], s['nama'], s['kelas'], s['jenis_kelamin'],
            s['tugas_1'], s['tugas_2'], s['tugas_3'], s['uts'], s['uas'],
            s['nilai_akhir'] if s['nilai_akhir'] is not None else "-",
            s['grade'], s['status']
        ])
    #Tampilkan Tabel dengan Tabulate
    print(tabulate(table, headers=header, tablefmt="grid"))

# Fungsi READ – Cari atau Tampilkan Data Siswa (9)
def cari_siswa(data):
    #Tampilan Menu Baca Data
    print("\n=== READ MENU ===")
    print("1. Tampilkan Semua Siswa")
    print("2. Cari Siswa Berdasarkan NIS")
    #Input Pilihan Menu
    pilihan = input("Pilih menu: ")
    #Opsi 1 – Tampilkan Semua Siswa
    if pilihan == "1":
        tampilkan_semua(data)
    #Opsi 2 – Cari Siswa Berdasarkan NIS
    elif pilihan == "2":
        nis = input("Masukkan NIS yang ingin dicari: ")
        for s in data:
            if s['nis'] == nis:
                header = ["NIS", "Nama", "Kelas", "JK", "Tugas 1", "Tugas 2", "Tugas 3", "UTS", "UAS", "Nilai Akhir", "Grade", "Status"]
                row = [[
                    s['nis'], s['nama'], s['kelas'], s['jenis_kelamin'],
                    s['tugas_1'], s['tugas_2'], s['tugas_3'], s['uts'], s['uas'],
                    s['nilai_akhir'] if s['nilai_akhir'] is not None else "-", s['grade'], s['status']
                ]]
                print(tabulate(row, headers=header, tablefmt="grid"))
                return
        print("Data siswa tidak ditemukan.")
    #Validasi Input Menu
    else:
        print("Pilihan tidak valid.")

# Fungsi UPDATE – Mengubah Data Siswa (10)
def ubah_siswa(data):
    #Input NIS yang ingin diubah
    nis = input("Masukkan NIS yang ingin diubah: ")
    #Loop Pencarian Siswa
    for s in data:
        if s['nis'] == nis:
            print(f"\nData lama: Nama = {s['nama']}, Kelas = {s['kelas']}")
            #Input Data Baru (Identitas)
            s['nama'] = input("Masukkan Nama baru: ") or s['nama']
            s['kelas'] = input("Masukkan Kelas baru: ") or s['kelas']
            s['jenis_kelamin'] = input("Masukkan Jenis Kelamin baru: ") or s['jenis_kelamin']
            #Fungsi input_nilai() untuk Validasi Nilai
            def input_nilai(nama_nilai, nilai_lama):
                while True:
                    nilai_baru = input(f"{nama_nilai} (0-100) [Nilai lama: {nilai_lama}]: ")
                    if nilai_baru == "":
                        return nilai_lama
                    if not nilai_baru.isdigit():
                        print("Harus berupa angka.")
                        continue
                    nilai_baru = int(nilai_baru)
                    if 0 <= nilai_baru <= 100:
                        return nilai_baru
                    else:
                        print("Nilai harus antara 0 dan 100.")
            #Input Komponen Nilai Baru
            s['tugas_1'] = input_nilai("Tugas 1", s['tugas_1'])
            s['tugas_2'] = input_nilai("Tugas 2", s['tugas_2'])
            s['tugas_3'] = input_nilai("Tugas 3", s['tugas_3'])
            s['uts']     = input_nilai("UTS", s['uts'])
            s['uas']     = input_nilai("UAS", s['uas'])

            #Hitung Ulang Nilai Akhir, Grade, dan Status
            if all(n != 0 for n in [s['tugas_1'], s['tugas_2'], s['tugas_3'], s['uts'], s['uas']]):
                s['nilai_akhir'] = hitung_nilai_akhir(s['tugas_1'], s['tugas_2'], s['tugas_3'], s['uts'], s['uas'])
                s['grade'] = konversi_grade(s['nilai_akhir'])
                s['status'] = status_lulus(s['grade'])
            else:
                s['nilai_akhir'] = None
                s['grade'] = "-"
                s['status'] = "-"
                print("\nSalah satu nilai bernilai 0. Oleh sebab itu nilai akhir dan grade tidak dapat dihitung.")
            #Output Berhasil Diperbarui
            print("\nData berhasil diperbarui. Terimakasih!")
            return
    #Jika Siswa Tidak Ditemukan
    print("Data siswa tidak ditemukan.")

# Fungsi DELETE – Menghapus Data Siswa (11)
def hapus_siswa(data):
    #Input NIS
    nis = input("Masukkan NIS yang ingin dihapus: ")
    #Loop Pencarian Siswa
    for i in range(len(data)):
        if data[i]['nis'] == nis:
            #Konfirmasi Penghapusan
            konfirmasi = input(f"Yakin ingin menghapus data {data[i]['nama']}? (ya/tidak): ")
            #Jika Konfirmasi "ya"
            if konfirmasi.lower() == 'ya':
                data.pop(i)
                print("Data berhasil dihapus.")
            #Jika Konfirmasi tidak
            else:
                print("Dibatalkan.")
            return
    #Jika NIS Tidak Ditemukan
    print("Data tidak ditemukan.")

# Fungsi login (12)
def login():
    #Menampilkan tampilan login
    print("\n=== LOGIN SISTEM ===")
    #Input identitas pengguna (NIA/NIS)
    kode = input("Masukkan NIA (Admin) atau NIS (Siswa): ")
    #Cek apakah pengguna adalah Admin
    if kode in data_admin:
        print(f"Login berhasil sebagai ADMIN ({data_admin[kode]})")
        return 'admin'
    #Jika bukan Admin, cek apakah pengguna adalah Siswa
    for s in data_siswa:
        if s['nis'] == kode:
            print(f"Login berhasil sebagai SISWA ({s['nama']})")
            return s['nis']
    #Jika tidak ditemukan di Admin maupun Siswa
    print("Login gagal. NIA/NIS tidak ditemukan.")
    return None

# Fungsi Statistik Akademik Siswa (13)
from collections import OrderedDict

def statistik_akademik(data):
    #Menampilkan judul
    print("\n=== STATISTIK AKADEMIK ===")
    #Filter data siswa dengan nilai lengkap
    data_valid = [s for s in data if s['nilai_akhir'] is not None]
    #Hitung jumlah siswa valid
    total = len(data_valid)
    #Cek apakah ada data yang valid
    if total == 0:
        print("Belum ada data nilai lengkap untuk dihitung.")
        return
    #Rata-rata nilai akhir
    rata2 = sum([s['nilai_akhir'] for s in data_valid]) / total
    #Nilai tertinggi dan siswa yang meraih
    tertinggi = max(data_valid, key=lambda x: x['nilai_akhir'])
    #Nilai terendah dan siswa yang meraih
    terendah = min(data_valid, key=lambda x: x['nilai_akhir'])
    #Struktur distribusi menggunakan OrderedDict
    distribusi_grade = OrderedDict({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0})
    #Menghitung jumlah siswa per grade
    for s in data_valid:
        distribusi_grade[s['grade']] += 1
    #Menampilkan statistik utama
    print(f"Total Siswa dengan Nilai Lengkap: {total}")
    print(f"Rata-rata Nilai Akhir: {rata2:.2f}")
    print(f"Nilai Tertinggi: {tertinggi['nilai_akhir']} diraih oleh {tertinggi['nama']} (Grade: {tertinggi['grade']})")
    print(f"Nilai Terendah: {terendah['nilai_akhir']} diraih oleh {terendah['nama']} (Grade: {terendah['grade']})")
    #Menampilkan distribusi grade dalam bentuk tabel
    header = ["Grade", "Jumlah Siswa"]
    table = [[g, j] for g, j in distribusi_grade.items()]
    print("\nDistribusi Grade:")
    print(tabulate(table, headers=header, tablefmt="grid"))

# Fungsi Sorting (14)
def sorting_siswa(data):
    #Menampilkan menu Sorting
    print("\n=== SORTING SISWA ===")
    print("1. Berdasarkan Nilai Akhir (Tertinggi ke Terendah)")
    print("2. Berdasarkan Nama (A-Z)")
    print("3. Berdasarkan NIS (Asc)")
    #Input Pilihan Sorting
    pilihan = input("Pilih metode sorting: ")
    #Logika Sorting 
    if pilihan == "1":
        sorted_data = sorted(data, key=lambda x: x['nilai_akhir'] if x['nilai_akhir'] is not None else -1, reverse=True)
    elif pilihan == "2":
        sorted_data = sorted(data, key=lambda x: x['nama'])
    elif pilihan == "3":
        sorted_data = sorted(data, key=lambda x: x['nis'])
    else:
        print("Pilihan tidak valid.")
        return
    #Tampilan Output Data
    header = ["NIS", "Nama", "Nilai Akhir", "Grade", "Status"]
    table = [
        [s['nis'], s['nama'], s['nilai_akhir'] if s['nilai_akhir'] is not None else "-", s['grade'], s['status']]
        for s in sorted_data
    ]
    print(tabulate(table, headers=header, tablefmt="grid"))

# Fungsi Menu Utama Admin (15)
def menu_admin(data):
    #Perulangan Menu
    while True:
        #Daftar Menu Admin
        print("\n=== MENU UTAMA (ADMIN) ===")
        print("1. Tambah Data Siswa")
        print("2. Cari Siswa")
        print("3. Ubah Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Statistik Akademik")
        print("6. Sorting Data Siswa")
        print("7. Logout")
        #Logika Pemrosesan Menu
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_siswa(data)
        elif pilihan == "2":
            cari_siswa(data)
        elif pilihan == "3":
            ubah_siswa(data)
        elif pilihan == "4":
            hapus_siswa(data)
        elif pilihan == "5":
            statistik_akademik(data)
        elif pilihan == "6":
            sorting_siswa(data)
        elif pilihan == "7":
            print("Logout berhasil.")
            break
        #Jika input Salah
        else:
            print("Pilihan tidak valid.")
# Fungsi Menu Siswa (16)
def menu_siswa(data, nis_login):
    while True:
        #Daftar Menu Siswa
        print(f"\n=== MENU SISWA (NIS: {nis_login}) ===")
        print("1. Lihat Nilai dan Status")
        print("2. Logout")

        pilihan = input("Pilih menu: ")
        #Pilihan 1 – Lihat Nilai dan Status
        if pilihan == "1":
            siswa = next((s for s in data if s['nis'] == nis_login), None)
            if siswa:
                header = ["Nama", "Kelas", "Nilai Akhir", "Grade", "Status"]
                row = [[siswa['nama'], siswa['kelas'], siswa['nilai_akhir'], siswa['grade'], siswa['status']]]
                print(tabulate(row, headers=header, tablefmt="grid"))
            else:
                print("Data tidak ditemukan.")
        #Pilihan 2 – Logout
        elif pilihan == "2":
            print("Logout berhasil.")
            break
        #Validasi Input
        else:
            print("Pilihan tidak valid.")

# Fungsi Start Program
def start_program(data):
    while True:
        #Sambutan Awal
        print("\n=== SELAMAT DATANG DI SISTEM MANAJEMEN NILAI SISWA ===")
        print("Silakan login menggunakan NIA (Admin) atau NIS (Siswa)")
        #Autentikasi Pengguna
        login_status = login()
        #Akses Berdasarkan Role
        if login_status == 'admin':
            menu_admin(data)
        elif login_status:
            menu_siswa(data, login_status)
        else:
            #Login Gagal – Opsi Ulangi
            retry = input("Coba login lagi? (ya/tidak): ").lower()
            if retry != 'ya':
                print(" Terima kasih telah menggunakan sistem ini.")
                break
# Main Entry Point
if __name__ == "__main__":
    start_program(data_siswa)