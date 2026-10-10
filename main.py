def tampilkan_menu():
    print("\n" + "=" * 40)
    print("       TRO ENGINEERING TOOLKIT")
    print("=" * 40)
    print("1. Kalkulator Hukum Ohm")
    print("2. Informasi Aplikasi")
    print("0. Keluar")
    print("=" * 40)


def informasi_aplikasi():
    print("\nTRO Engineering Toolkit")
    print("Versi: 1.0.0")
    print("Dibuat untuk mahasiswa Teknologi Rekayasa Otomasi.")
    print("Fitur dikembangkan secara bertahap.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\nFitur Hukum Ohm akan kita buat berikutnya.")
        elif pilihan == "2":
            informasi_aplikasi()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan aplikasi!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()