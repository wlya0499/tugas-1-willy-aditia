#willy aditia
#(41823010002)
#tugas 2

part = input("Pilih bagian (A/B): ").upper()

# Memeriksa input yang valid dan menjalankan sesuai pilihan
if part == 'A':
    print("Bagian A:")
    n = int(input("Masukkan nilai n: "))
    for i in range(n):
        print(i*i)


elif part == 'B':
    print("Bagian B:")
    n = int(input("Masukkan nilai n: "))
    for i in range(n):
        if i % 2 == 1 or i == 0:
            print(i*i)
else:
    print("Pilihan tidak valid.")




#willy aditia
#(41823010002)
#tugas 2
