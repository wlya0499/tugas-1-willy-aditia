#willy aditia(41823010002)

print("Salamat datang di Aplikasi perhitungan nilai Mahasiswa")
def rumus_nilai_akhir(tugas, uts, uas):
    return 0.25 * tugas + 0.35 * uts + 0.4 * uas

def ubah_jadi_huruf(nilai_akhir):
    if nilai_akhir > 85:
        return "A"
    elif nilai_akhir > 80:
        return "A-"
    elif nilai_akhir > 75:
        return "B+"
    elif nilai_akhir > 70:
        return "B"
    elif nilai_akhir > 65:
        return "B-"
    elif nilai_akhir > 60:
        return "C+"
    elif nilai_akhir > 55:
        return "C"
    elif nilai_akhir > 50:
        return "C-"
    elif nilai_akhir > 30:
        return "D"
    else:
        return "E"

tugas = float(input("Silahkan masukkan nilai tugas anda: \n"))
uts = float(input("Silahkan masukkan nilai UTS anda: \n"))
uas = float(input("Silahkna masukkan nilai UAS anda: \n"))

nilai_akhir = rumus_nilai_akhir(tugas, uts, uas)
print("Nilai akhir:", nilai_akhir)

dalam_huruf = ubah_jadi_huruf(nilai_akhir)
print("Dalam huruf:", dalam_huruf)
