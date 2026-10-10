from calculators import (
    kalkulator_hukum_ohm, 
    kalkulator_daya, 
    kalkulator_pembagi_tegangan,
    kalkulator_kode_resistor,)

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("       TRO ENGINEERING TOOLKIT")
    print("=" * 40)
    print("1. Kalkulator Hukum Ohm")
    print("2. Informasi Aplikasi")
    print("3. Kalkulator Daya Listrik")
    print("4. Kalkulator Pembagi Tegangan")
    print("5. Kalkulator Kode Warna Resistor")
    print("0. Keluar")
    print("=" * 40)


def informasi_aplikasi():
    print("\nTRO Engineering Toolkit")
    print("Versi: 1.1.0")
    print("Toolkit teknik untuk mahasiswa Teknologi Rekayasa Otomasi.")
    print("Fitur: Hukum Ohm, Kalkulator Daya, Kalkulator Pembagi Tegangan, dan Kalkulator Kode Warna Resistor.")


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
        elif pilihan == "5":
            kalkulator_kode_resistor()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()