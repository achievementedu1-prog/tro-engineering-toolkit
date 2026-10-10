
import math


def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan).replace(",", "."))

            if not math.isfinite(nilai):
                print("Masukkan angka yang valid dan terbatas.")
                continue

            if nilai < 0:
                print("Nilai tidak boleh negatif.")
                continue

            return nilai

        except ValueError:
            print("Input tidak valid. Masukkan angka.")