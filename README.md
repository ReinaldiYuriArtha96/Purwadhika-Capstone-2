
# Sistem Manajemen Nilai Siswa SMA

## Deskripsi Program

Program ini adalah aplikasi berbasis **Command Line Interface (CLI)** untuk mengelola data nilai siswa tingkat SMA. Program ini menyediakan fitur lengkap seperti **CRUD**, perhitungan **nilai akhir**, **grade**, **status kelulusan**, hingga statistik akademik.

---

## Urgensi Program

### Efisiensi Administrasi
- Menghindari kesalahan pencatatan manual
- Mempercepat proses input dan pelaporan nilai
- Mempermudah pencarian data siswa

### Monitoring Akademik
- Mengelompokkan siswa berdasarkan performa
- Deteksi siswa remedial atau berprestasi
- Statistik distribusi grade untuk analisis kelas

### Pengambilan Keputusan
- Data nilai real time untuk rapor dan evaluasi
- Dasar pemberian penghargaan dan pembinaan
- Mendukung analisis tingkat kelulusan

---

## Stakeholder

| Peran                 | Kebutuhan Utama                                          |
|-----------------------|----------------------------------------------------------|
| Guru/Wali Kelas/Admin | Laporan nilai siswa dan kelulusan dan CRUD               | 
| Siswa                 | Melihat nilai pribadi dan status kelulusan               |

---

## Fitur Utama

- Lihat Data: Semua siswa atau berdasarkan NIS
- Tambah Siswa: Validasi NIS, input nilai lengkap
- Ubah Data: Edit identitas atau nilai siswa
- Hapus Siswa: Konfirmasi sebelum penghapusan
- Statistik Akademik: Rata-rata, tertinggi, terendah, distribusi grade
- Sorting Data: Berdasarkan nama, NIS, atau nilai akhir
- Login Role-Based: Admin dan Siswa

---

## Struktur Data

Setiap data siswa memiliki atribut berikut:

- `nis`: Nomor Induk Siswa  
- `nama`: Nama lengkap  
- `kelas`: Kelas siswa  
- `jenis_kelamin`: Laki-laki atau Perempuan  
- `tugas_1` – `tugas_3`: Nilai tugas  
- `uts`: Nilai Ujian Tengah Semester  
- `uas`: Nilai Ujian Akhir Semester  
- `nilai_akhir`: Perhitungan berdasarkan bobot  
- `grade`: A / B / C / D / E  
- `status`: Lulus atau Remedial  

---

## Bobot Nilai

- Tugas 1 (10%)  
- Tugas 2 (10%)  
- Tugas 3 (10%)  
- UTS (20%)  
- UAS (50%)  

---

## Konversi Grade

| Nilai Akhir | Grade  |
|-------------|--------|
| ≥ 85        | A      |
| 75 – 84     | B      |
| 65 – 74     | C      |
| 55 – 64     | D      |
| < 55        | E      |

---

## Cara Penggunaan

Jalankan program dengan perintah:

```bash
python Code Capstone 2.py
```

## Login Sebagai

- **Admin**: Gunakan NIA `00001` hingga `00005`  
- **Siswa**: Gunakan NIS yang telah terdaftar dalam sistem  

> Keluar dari program dengan memilih **Logout**, atau ketik **tidak** saat ditanya apakah ingin login ulang.

---

## Panduan Menu Berdasarkan Role

### Admin
- Tambah Data Siswa  
- Lihat dan Cari Data  
- Edit Data  
- Hapus Data  
- Statistik Akademik  
- Sorting Data  

### Siswa
- Lihat nilai pribadi dan status kelulusan

---

## Contoh Data

Program ini sudah dilengkapi dengan 20 data siswa dari berbagai kelas, seperti:

- Kemal – X IPA 2  
- Maudy – X IPS 2  
- Robert – X IPS 2  
- Eka – X IPA 1  
- ... dan lainnya

---

## Kebutuhan Sistem

- **Python** versi 3.x

### Library yang Digunakan

| Library                    | Keterangan                                                 |
|----------------------------|------------------------------------------------------------|
| `tabulate`                 | Untuk menampilkan data dalam bentuk tabel CLI              |
| `collections.OrderedDict`  | Untuk menampilkan distribusi grade secara terurut          |

> Instalasi library eksternal:
```bash
pip install tabulate
```

