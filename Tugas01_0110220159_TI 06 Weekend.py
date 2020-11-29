print("berikut adalah fitur input data nilai mahasiswa")
print("=====================")
print('input data dibawah ini')
# untuk menginput nim
s = input('Silahkan Masukakan NIM : ')

# untuk menginput jumlah matakuliah yang diambil dengan tipe data int
y = int(input('jumlah mata kuliah yang kamu diambil : '))

# variabel jumlah menampung nilai dari variabel d sebagai beban sks
jumlah = 0

# jika mata kuliah yang di ambil kurang dari sama dengan 8
if (y <= 8):

    i = 0
    while i < y:
        # disini akan terjadi perulangan sebanyak matakuliah yang diambil oleh mahasiswa

        # untuk mengingut nama mata kuliah yang diambil
        print('Nilai Mahasiswa ', i + 1)
        f = input('nama mata kuliah : ')

        # untuk menginput banyaknya sks yang di ambil mahasiswa/i
        a = eval(input('Beban SKS mata kuliah : '))
        jumlah = jumlah + a
        # variabel jumlah di gunakan untuk melakukan kalkulasi dari banyaknya sks dan akan di tampilkan di rangkuman

        # program ini untuk menginput kuis
        kuis = eval(input('Nilai Kuis: '))

        # untuk menginput tugas1, tugas 2, uts, uas yang akan ditampilkan
        ts = eval(input('Nilai Tugas 1: '))
        td = eval(input('Nilai Tugas 2: '))
        uts = eval(input('Nilai UTS: '))
        uas = eval(input('Nilai UAS: '))

        # variabel total di gunakan untuk mengitung total penilaian dari semua nilai diatas
        # dengan bobot nilai 15% untuk kuis, 15% untuk tugas1 , 20% untuk tugas 2, 25% untuk uts, dan 25% untuk UAS
        total = 0.15*kuis+0.15*ts+0.20*td+0.25*uts+0.25*uas

        # operator logika untuk mementukan grade dari setiap nilai
        if (total == 100) or (total >= 85):    # Grade A = 85 - 100
            print('Nilai untuk mata kuliah', a, ': ', total, ' (grade A)')
        elif (total < 85) or (total >= 70):  # Grade B = 70-84
            print('Nilai untuk mata kuliah', a, ': ', total, ' (grade B)')
        elif (total < 70) or (total >= 55):  # Grade C = 55 - 69
            print('Nilai untuk mata kuliah', a, ': ', total, ' (grade c)')
        elif (total < 55) or (total >= 40):  # grade D = 40 -54
            print('Nilai untuk mata kuliah', a, ': ', total, ' (grade D)')
        else:
            # untuk nilai di bawah 40 = grade E
            print('Nilai untuk mata kuliah', a, ': ', total, ' (garde E)')
        i = i + 1
else:
    print('Jumlah mata kuliah harus antara 1-8')
    # jumalah/banyak mata kuliah yang diambail antara 1-8

# ip variabel untuk menentukan indeks prestarsi yang diambil dalam satu semseter
ip = jumlah/i

print()
print('Rangkuman')
print('NIM: ', a)
print('Total SKS : ', jumlah)
print('index prestasi : ', ip)
print(end="")
