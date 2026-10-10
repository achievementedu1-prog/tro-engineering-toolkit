
def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))

            if nilai < 0:
                print("Nilai tidak boleh negatif.")
                continue

            return nilai

        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def tampilkan_menu():
    print("\n" + "=" * 40)
    print("       TRO ENGINEERING TOOLKIT")
    print("=" * 40)
    print("1. Kalkulator Hukum Ohm")
    print("2. Informasi Aplikasi")
    print("3. Kalkulator Daya Listrik")
    print("4. Kalkulator Pembagi Tegangan")
    print("0. Keluar")
    print("=" * 40)


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

def informasi_aplikasi():
    print("\nTRO Engineering Toolkit")
    print("Versi: 1.1.0")
    print("Toolkit teknik untuk mahasiswa Teknologi Rekayasa Otomasi.")
    print("Fitur: Hukum Ohm, Kalkulator Daya, dan Kalkulator Pembagi Tegangan.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kalkulator_hukum_ohm()
        elif pilihan == "2":
            informasi_aplikasi()
        elif pilihan == "3":
            kalkulator_daya()
        elif pilihan == "4":
            kalkulator_pembagi_tegangan()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()