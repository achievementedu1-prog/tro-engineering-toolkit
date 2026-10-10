
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from calculators import (
    kalkulator_hukum_ohm,
    kalkulator_daya,
    kalkulator_pembagi_tegangan,
    kalkulator_kode_resistor,
    kalkulator_resistor_seri_paralel
)


class TestCalculators(unittest.TestCase):

    def jalankan_dengan_input(self, fungsi, daftar_input):
        hasil_output = StringIO()

        with patch("builtins.input", side_effect=daftar_input):
            with redirect_stdout(hasil_output):
                fungsi()

        return hasil_output.getvalue()

    def test_hukum_ohm(self):
        output = self.jalankan_dengan_input(
            kalkulator_hukum_ohm,
            ["1", "2", "6", "0"]
        )
        self.assertIn("12.00", output)

    def test_kalkulator_daya(self):
        output = self.jalankan_dengan_input(
            kalkulator_daya,
            ["1", "12", "2", "0"]
        )
        self.assertIn("24.00", output)

    def test_pembagi_tegangan(self):
        output = self.jalankan_dengan_input(
            kalkulator_pembagi_tegangan,
            ["12", "1000", "2000"]
        )
        self.assertIn("8.00", output)

    def test_kode_warna_resistor(self):
        output = self.jalankan_dengan_input(
            kalkulator_kode_resistor,
            ["cokelat", "hitam", "merah", "emas"]
        )
        self.assertIn("1000", output)

    
    def test_resistor_seri(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["1", "3", "100", "220", "330"]
        )
        self.assertIn("650.00", output)

    def test_resistor_paralel(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["2", "2", "100", "100"]
        )
        self.assertIn("50.00", output)

    def test_resistor_paralel_nol(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["2", "2", "100", "0"]
        )
        self.assertIn("lebih besar dari 0", output)

    def test_pilihan_rangkaian_tidak_valid(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["9"]
        )
        self.assertIn("tidak valid", output)


    def test_jumlah_resistor_input_huruf(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["1", "abc", "2", "100", "200"]
        )
        self.assertIn("bilangan bulat", output)
        self.assertIn("300.00", output)

    def test_jumlah_resistor_nol(self):
        output = self.jalankan_dengan_input(
            kalkulator_resistor_seri_paralel,
            ["1", "0", "2", "100", "200"]
        )
        self.assertIn("minimal 1", output)
        self.assertIn("300.00", output)
        
if __name__ == "__main__":
    unittest.main()