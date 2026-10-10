from input_utils import input_angka


def input_jumlah_resistor():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah resistor: "))

            if jumlah < 1:
                print("Jumlah resistor minimal 1.")
                continue

            return jumlah

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

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


def kalkulator_resistor_seri_paralel():
    print("\n=== KALKULATOR RESISTOR SERI-PARALEL ===")
    print("1. Rangkaian Seri")
    print("2. Rangkaian Paralel")

    pilihan = input("Pilih jenis rangkaian: ")

    if pilihan == "1":
        jumlah = input_jumlah_resistor()

        hambatan_total = 0

        for i in range(jumlah):
            hambatan = input_angka(
                f"Masukkan hambatan R{i + 1} (ohm): "
            )
            hambatan_total += hambatan

        print(f"Hambatan total seri = {hambatan_total:.2f} ohm")

    elif pilihan == "2":
        jumlah = input_jumlah_resistor()

        jumlah_kebalikan = 0

        for i in range(jumlah):
            hambatan = input_angka(
                f"Masukkan hambatan R{i + 1} (ohm): "
            )

            if hambatan == 0:
                print("Hambatan resistor harus lebih besar dari 0.")
                return

            jumlah_kebalikan += 1 / hambatan

        hambatan_total = 1 / jumlah_kebalikan

        print(f"Hambatan total paralel = {hambatan_total:.2f} ohm")

    else:
        print("Pilihan rangkaian tidak valid.")

# ==========================================
# FUNGSI PERHITUNGAN UNTUK PYTHON API
# ==========================================

def hitung_ohm(metode, tegangan=None, arus=None, hambatan=None):
    if metode == "tegangan":
        if arus is None or hambatan is None:
            raise ValueError("Arus dan hambatan wajib diisi.")
        return {"hasil": arus * hambatan, "satuan": "V"}

    elif metode == "arus":
        if tegangan is None or hambatan is None:
            raise ValueError("Tegangan dan hambatan wajib diisi.")
        if hambatan == 0:
            raise ValueError("Hambatan tidak boleh nol.")
        return {"hasil": tegangan / hambatan, "satuan": "A"}

    elif metode == "hambatan":
        if tegangan is None or arus is None:
            raise ValueError("Tegangan dan arus wajib diisi.")
        if arus == 0:
            raise ValueError("Arus tidak boleh nol.")
        return {"hasil": tegangan / arus, "satuan": "Ohm"}

    raise ValueError("Metode Hukum Ohm tidak valid.")


def hitung_daya(metode, tegangan=None, arus=None, hambatan=None):
    if metode == "tegangan_arus":
        if tegangan is None or arus is None:
            raise ValueError("Tegangan dan arus wajib diisi.")
        daya = tegangan * arus

    elif metode == "arus_hambatan":
        if arus is None or hambatan is None:
            raise ValueError("Arus dan hambatan wajib diisi.")
        daya = arus ** 2 * hambatan

    elif metode == "tegangan_hambatan":
        if tegangan is None or hambatan is None:
            raise ValueError("Tegangan dan hambatan wajib diisi.")
        if hambatan == 0:
            raise ValueError("Hambatan tidak boleh nol.")
        daya = tegangan ** 2 / hambatan

    else:
        raise ValueError("Metode perhitungan daya tidak valid.")

    return {"hasil": daya, "satuan": "W"}


def hitung_pembagi_tegangan(tegangan_masuk, r1, r2):
    if r1 + r2 == 0:
        raise ValueError("Total hambatan tidak boleh nol.")

    hasil = tegangan_masuk * r2 / (r1 + r2)
    return {"hasil": hasil, "satuan": "V"}


def hitung_kode_resistor(warna1, warna2, pengali, toleransi):
    warna_angka = {
        "hitam": 0, "cokelat": 1, "merah": 2,
        "jingga": 3, "kuning": 4, "hijau": 5,
        "biru": 6, "ungu": 7, "abu-abu": 8, "putih": 9
    }

    warna_pengali = {
        "hitam": 1, "cokelat": 10, "merah": 100,
        "jingga": 1000, "kuning": 10000,
        "hijau": 100000, "biru": 1000000,
        "emas": 0.1, "perak": 0.01
    }

    warna_toleransi = {
        "cokelat": 1, "merah": 2, "hijau": 0.5,
        "biru": 0.25, "ungu": 0.1,
        "emas": 5, "perak": 10
    }

    warna1 = warna1.strip().lower()
    warna2 = warna2.strip().lower()
    pengali = pengali.strip().lower()
    toleransi = toleransi.strip().lower()

    if warna1 not in warna_angka or warna2 not in warna_angka:
        raise ValueError("Warna gelang pertama atau kedua tidak valid.")
    if pengali not in warna_pengali:
        raise ValueError("Warna pengali tidak valid.")
    if toleransi not in warna_toleransi:
        raise ValueError("Warna toleransi tidak valid.")

    angka = warna_angka[warna1] * 10 + warna_angka[warna2]
    hambatan = angka * warna_pengali[pengali]
    persen = warna_toleransi[toleransi]

    return {
        "hambatan": hambatan,
        "satuan": "Ohm",
        "toleransi_persen": persen
    }


def hitung_resistor_seri_paralel(jenis, hambatan):
    if not hambatan:
        raise ValueError("Masukkan minimal satu nilai hambatan.")

    if any(r <= 0 for r in hambatan):
        raise ValueError("Semua hambatan harus lebih besar dari nol.")

    if jenis == "seri":
        total = sum(hambatan)

    elif jenis == "paralel":
        total = 1 / sum(1 / r for r in hambatan)

    else:
        raise ValueError("Jenis rangkaian harus seri atau paralel.")

    return {"hasil": total, "satuan": "Ohm"}