from input_utils import input_angka

def kalkulator_hukum_ohm():
    while True:
        print("\n--- KALKULATOR HUKUM OHM ---")
        print("1. Hitung Tegangan (V)")
        print("2. Hitung Arus (I)")
        print("3. Hitung Hambatan (R)")
        print("0. Kembali")

        pilihan = input("Pilih perhitungan: ")

        if pilihan == "1":
            arus = input_angka("Arus (A): ")
            hambatan = input_angka("Hambatan (Ohm): ")
            print(f"Tegangan = {arus * hambatan:.2f} V")

        elif pilihan == "2":
            tegangan = input_angka("Tegangan (V): ")
            hambatan = input_angka("Hambatan (Ohm): ")

            if hambatan == 0:
                print("Hambatan tidak boleh nol.")
                continue

            print(f"Arus = {tegangan / hambatan:.2f} A")

        elif pilihan == "3":
            tegangan = input_angka("Tegangan (V): ")
            arus = input_angka("Arus (A): ")

            if arus == 0:
                print("Arus tidak boleh nol.")
                continue

            print(f"Hambatan = {tegangan / arus:.2f} Ohm")

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")

def kalkulator_daya():
    while True:
        print("\n--- KALKULATOR DAYA LISTRIK ---")
        print("1. Daya dari Tegangan dan Arus")
        print("2. Daya dari Arus dan Hambatan")
        print("3. Daya dari Tegangan dan Hambatan")
        print("0. Kembali")

        pilihan = input("Pilih perhitungan: ")

        if pilihan == "1":
            tegangan = input_angka("Tegangan (V): ")
            arus = input_angka("Arus (A): ")
            daya = tegangan * arus
            print(f"Daya = {daya:.2f} W")

        elif pilihan == "2":
            arus = input_angka("Arus (A): ")
            hambatan = input_angka("Hambatan (Ohm): ")
            daya = arus ** 2 * hambatan
            print(f"Daya = {daya:.2f} W")

        elif pilihan == "3":
            tegangan = input_angka("Tegangan (V): ")
            hambatan = input_angka("Hambatan (Ohm): ")

            if hambatan == 0:
                print("Hambatan tidak boleh nol.")
                continue

            daya = tegangan ** 2 / hambatan
            print(f"Daya = {daya:.2f} W")

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid.")

def kalkulator_pembagi_tegangan():
    print("\n--- KALKULATOR PEMBAGI TEGANGAN ---")

    tegangan_masuk = input_angka("Tegangan masukan (V): ")
    r1 = input_angka("Hambatan R1 (Ohm): ")
    r2 = input_angka("Hambatan R2 (Ohm): ")

    if r1 + r2 == 0:
        print("Total hambatan tidak boleh nol.")
        return

    tegangan_keluar = tegangan_masuk * r2 / (r1 + r2)

    print(f"Tegangan keluaran = {tegangan_keluar:.2f} V")

def kalkulator_kode_resistor():
    warna_angka = {
        "hitam": 0,
        "cokelat": 1,
        "merah": 2,
        "jingga": 3,
        "kuning": 4,
        "hijau": 5,
        "biru": 6,
        "ungu": 7,
        "abu-abu": 8,
        "putih": 9
    }

    warna_pengali = {
        "hitam": 1,
        "cokelat": 10,
        "merah": 100,
        "jingga": 1000,
        "kuning": 10000,
        "hijau": 100000,
        "biru": 1000000,
        "emas": 0.1,
        "perak": 0.01
    }

    warna_toleransi = {
        "cokelat": 1,
        "merah": 2,
        "hijau": 0.5,
        "biru": 0.25,
        "ungu": 0.1,
        "emas": 5,
        "perak": 10
    }

    print("\n--- KALKULATOR KODE WARNA RESISTOR ---")
    print("Warna yang tersedia:")
    print(", ".join(warna_angka.keys()))

    warna1 = input("Warna gelang pertama: ").strip().lower()
    warna2 = input("Warna gelang kedua: ").strip().lower()
    pengali = input("Warna gelang ketiga (pengali): ").strip().lower()
    toleransi = input("Warna gelang keempat (toleransi): ").strip().lower()

    if warna1 not in warna_angka or warna2 not in warna_angka:
        print("Warna gelang pertama atau kedua tidak valid.")
        return

    if pengali not in warna_pengali:
        print("Warna pengali tidak valid.")
        return

    if toleransi not in warna_toleransi:
        print("Warna toleransi tidak valid.")
        return

    angka = warna_angka[warna1] * 10 + warna_angka[warna2]
    hambatan = angka * warna_pengali[pengali]
    persen = warna_toleransi[toleransi]

    print(f"Nilai hambatan = {hambatan:g} Ohm")
    print(f"Toleransi = ±{persen:g}%")                            