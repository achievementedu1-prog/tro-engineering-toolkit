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