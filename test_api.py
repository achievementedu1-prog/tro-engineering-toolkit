
import unittest

from api.calculate import proses_kalkulasi


class TestAPI(unittest.TestCase):

    def test_hukum_ohm_tegangan(self):
        hasil = proses_kalkulasi({
            "kalkulator": "ohm",
            "metode": "tegangan",
            "arus": 2,
            "hambatan": 10
        })

        self.assertEqual(hasil["hasil"], 20)
        self.assertEqual(hasil["satuan"], "V")


if __name__ == "__main__":
    unittest.main()