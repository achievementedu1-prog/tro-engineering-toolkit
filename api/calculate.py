
import json
import math
from http.server import BaseHTTPRequestHandler

from calculators import (
    hitung_ohm,
    hitung_daya,
    hitung_pembagi_tegangan,
    hitung_kode_resistor,
    hitung_resistor_seri_paralel,
)


def angka(data, nama):
    """Mengambil angka dari JSON dan memvalidasinya."""
    nilai = data.get(nama)

    if nilai is None or isinstance(nilai, bool):
        raise ValueError(f"Input '{nama}' wajib diisi dengan angka.")

    try:
        nilai = float(nilai)
    except (ValueError, TypeError):
        raise ValueError(f"Input '{nama}' harus berupa angka.")

    if not math.isfinite(nilai):
        raise ValueError(f"Input '{nama}' harus berupa angka yang valid.")

    return nilai


def proses_kalkulasi(data):
    kalkulator = data.get("kalkulator")

    if kalkulator == "ohm":
        hasil = hitung_ohm(
            metode=data.get("metode"),
            tegangan=angka(data, "tegangan")
            if data.get("tegangan") is not None else None,
            arus=angka(data, "arus")
            if data.get("arus") is not None else None,
            hambatan=angka(data, "hambatan")
            if data.get("hambatan") is not None else None,
        )

    elif kalkulator == "daya":
        hasil = hitung_daya(
            metode=data.get("metode"),
            tegangan=angka(data, "tegangan")
            if data.get("tegangan") is not None else None,
            arus=angka(data, "arus")
            if data.get("arus") is not None else None,
            hambatan=angka(data, "hambatan")
            if data.get("hambatan") is not None else None,
        )

    elif kalkulator == "pembagi_tegangan":
        hasil = hitung_pembagi_tegangan(
            angka(data, "tegangan_masuk"),
            angka(data, "r1"),
            angka(data, "r2"),
        )

    elif kalkulator == "kode_resistor":
        hasil = hitung_kode_resistor(
            data.get("warna1", ""),
            data.get("warna2", ""),
            data.get("pengali", ""),
            data.get("toleransi", ""),
        )

    elif kalkulator == "resistor_seri_paralel":
        hambatan = data.get("hambatan")

        if not isinstance(hambatan, list) or not hambatan:
            raise ValueError(
                "Input 'hambatan' harus berupa daftar angka yang tidak kosong."
            )

        nilai_hambatan = []
        for nilai in hambatan:
            if isinstance(nilai, bool):
                raise ValueError("Setiap hambatan harus berupa angka.")
            try:
                nilai = float(nilai)
            except (ValueError, TypeError):
                raise ValueError("Setiap hambatan harus berupa angka.")

            if not math.isfinite(nilai):
                raise ValueError("Setiap hambatan harus berupa angka yang valid.")

            nilai_hambatan.append(nilai)

        hasil = hitung_resistor_seri_paralel(
            data.get("jenis"),
            nilai_hambatan,
        )

    else:
        raise ValueError("Jenis kalkulator tidak dikenal.")

    return hasil


class handler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        body = json.dumps(data, allow_nan=False).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self.send_json(200, {
            "status": "ok",
            "message": "TRO Engineering Toolkit Python API is running.",
            "methods": ["GET", "POST"],
        })

    def do_POST(self):
        try:
            panjang = int(self.headers.get("Content-Length", "0"))

            if panjang <= 0 or panjang > 100_000:
                self.send_json(400, {
                    "status": "error",
                    "message": "Ukuran permintaan tidak valid.",
                })
                return

            body = self.rfile.read(panjang)
            data = json.loads(body.decode("utf-8"))

            if not isinstance(data, dict):
                raise ValueError("Data JSON harus berupa objek.")

            hasil = proses_kalkulasi(data)

            self.send_json(200, {
                "status": "ok",
                "hasil": hasil,
            })

        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {
                "status": "error",
                "message": "Format JSON tidak valid.",
            })

        except ValueError as error:
            self.send_json(400, {
                "status": "error",
                "message": str(error),
            })

        except Exception:
            self.send_json(500, {
                "status": "error",
                "message": "Terjadi kesalahan internal pada server.",
            })