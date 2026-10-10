
const API_URL = "/api/calculate";

const form = document.getElementById("calculator-form");
const fields = document.getElementById("calculator-fields");
const title = document.getElementById("calculator-title");
const calculateButton = document.getElementById("calculate-button");
const result = document.getElementById("result");

let activeTool = null;

const toolNames = {
    ohm: "Hukum Ohm",
    power: "Daya Listrik",
    divider: "Pembagi Tegangan",
    resistor: "Kode Resistor",
    series: "Resistor Seri & Paralel"
};

function buatInput(nama, label, tipe = "number", tambahan = "") {
    return `
        <label class="field">
            <span>${label}</span>
            <input
                name="${nama}"
                type="${tipe}"
                ${tipe === "number" ? 'step="any"' : ""}
                ${tambahan}
                required
            >
        </label>
    `;
}

function buatPilihan(nama, label, pilihan) {
    return `
        <label class="field">
            <span>${label}</span>
            <select name="${nama}" required>
                <option value="">Pilih ${label.toLowerCase()}</option>
                ${pilihan.map(item =>
                    `<option value="${item.value}">${item.label}</option>`
                ).join("")}
            </select>
        </label>
    `;
}

function tampilkanForm(tool) {
    activeTool = tool;
    title.textContent = toolNames[tool];
    result.hidden = true;
    result.textContent = "";

    let html = "";

    if (tool === "ohm") {
        html =
            buatPilihan("metode", "Besaran yang dicari", [
                { value: "tegangan", label: "Tegangan (V)" },
                { value: "arus", label: "Arus (A)" },
                { value: "hambatan", label: "Hambatan (Ω)" }
            ]) +
            `<div id="nilai-input"></div>`;
    } else if (tool === "power") {
        html =
            buatPilihan("metode", "Rumus perhitungan daya", [
                { value: "tegangan_arus", label: "P = V × I (Tegangan dan Arus)" },
                { value: "arus_hambatan", label: "P = I² × R (Arus dan Hambatan)" },
                { value: "tegangan_hambatan", label: "P = V² / R (Tegangan dan Hambatan)" }
            ]) +
            `<div id="nilai-input"></div>`;
    } else if (tool === "divider") {
        html =
            buatInput("tegangan_masuk", "Tegangan masuk (V)") +
            buatInput("r1", "Resistor R1 (Ω)") +
            buatInput("r2", "Resistor R2 (Ω)");
    } else if (tool === "resistor") {
        const warna = [
            ["hitam", "Hitam"], ["cokelat", "Cokelat"],
            ["merah", "Merah"], ["jingga", "Jingga"],
            ["kuning", "Kuning"], ["hijau", "Hijau"],
            ["biru", "Biru"], ["ungu", "Ungu"],
            ["abu-abu", "Abu-abu"], ["putih", "Putih"]
        ].map(([value, label]) => ({ value, label }));

        html =
            buatPilihan("warna1", "Warna pita pertama", warna) +
            buatPilihan("warna2", "Warna pita kedua", warna) +
            buatPilihan("pengali", "Warna pengali", [
                ...warna,
                { value: "emas", label: "Emas" },
                { value: "perak", label: "Perak" }
            ]) +
            buatPilihan("toleransi", "Warna toleransi", [
                { value: "cokelat", label: "Cokelat (±1%)" },
                { value: "merah", label: "Merah (±2%)" },
                { value: "hijau", label: "Hijau (±0,5%)" },
                { value: "biru", label: "Biru (±0,25%)" },
                { value: "ungu", label: "Ungu (±0,1%)" },
                { value: "emas", label: "Emas (±5%)" },
                { value: "perak", label: "Perak (±10%)" }
            ]);
    } else if (tool === "series") {
        html =
            buatPilihan("jenis", "Jenis rangkaian", [
                { value: "seri", label: "Seri" },
                { value: "paralel", label: "Paralel" }
            ]) +
            buatInput(
                "hambatan",
                "Nilai resistor (Ω), pisahkan dengan koma",
                "text",
                'placeholder="misalnya 100, 220, 330"'
            );
    }

    fields.innerHTML = html;
    calculateButton.hidden = false;

    const metode = fields.querySelector('[name="metode"]');
    if (metode && (tool === "ohm" || tool === "power")) {
        metode.addEventListener("change", tampilkanInputBesaran);
        tampilkanInputBesaran();
    }
}

function tampilkanInputBesaran() {
    const metode = fields.querySelector('[name="metode"]').value;
    const tempat = document.getElementById("nilai-input");

    if (!tempat) return;

    let html = "";

    if (activeTool === "ohm") {
        if (metode === "tegangan") {
            html = buatInput("arus", "Arus (A)") +
                   buatInput("hambatan", "Hambatan (Ω)");
        } else if (metode === "arus") {
            html = buatInput("tegangan", "Tegangan (V)") +
                   buatInput("hambatan", "Hambatan (Ω)");
        } else if (metode === "hambatan") {
            html = buatInput("tegangan", "Tegangan (V)") +
                   buatInput("arus", "Arus (A)");
        }
    }
    if (activeTool === "power") {
        if (metode === "tegangan_arus") {
            html = buatInput("tegangan", "Tegangan (V)") +
                   buatInput("arus", "Arus (A)");
        } else if (metode === "arus_hambatan") {
            html = buatInput("arus", "Arus (A)") +
                   buatInput("hambatan", "Hambatan (Ω)");
        } else if (metode === "tegangan_hambatan") {
            html = buatInput("tegangan", "Tegangan (V)") +
                   buatInput("hambatan", "Hambatan (Ω)");
        }
    }

    tempat.innerHTML = html;
}

document.querySelectorAll("[data-tool]").forEach(button => {
    button.addEventListener("click", () => {
        tampilkanForm(button.dataset.tool);
        document.getElementById("calculator").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
});

form.addEventListener("submit", async event => {
    event.preventDefault();

    if (!activeTool) return;

    calculateButton.disabled = true;
    calculateButton.textContent = "Menghitung...";
    result.hidden = false;
    result.textContent = "Sedang menghitung...";
    result.className = "result";

    try {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        let payload = {};

        if (activeTool === "ohm") {
            payload = {
                kalkulator: "ohm",
                metode: data.metode
            };

            ["tegangan", "arus", "hambatan"].forEach(key => {
                if (data[key] !== undefined && data[key] !== "") {
                    payload[key] = Number(data[key]);
                }
            });
        } else if (activeTool === "power") {
            payload = {
                kalkulator: "daya",
                metode: data.metode
            };

            ["tegangan", "arus", "hambatan"].forEach(key => {
                if (data[key] !== undefined && data[key] !== "") {
                    payload[key] = Number(data[key]);
                }
            });
        } else if (activeTool === "divider") {
            payload = {
                kalkulator: "pembagi_tegangan",
                tegangan_masuk: Number(data.tegangan_masuk),
                r1: Number(data.r1),
                r2: Number(data.r2)
            };
        } else if (activeTool === "resistor") {
            payload = {
                kalkulator: "kode_resistor",
                warna1: data.warna1,
                warna2: data.warna2,
                pengali: data.pengali,
                toleransi: data.toleransi
            };
        } else if (activeTool === "series") {
            const daftar = data.hambatan
                .split(",")
                .map(nilai => nilai.trim())
                .filter(nilai => nilai !== "");

            payload = {
                kalkulator: "resistor_seri_paralel",
                jenis: data.jenis,
                hambatan: daftar.map(Number)
            };
        }

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const jawaban = await response.json();

        if (!response.ok || jawaban.status !== "ok") {
            throw new Error(jawaban.message || "Perhitungan gagal.");
        }

        result.textContent = formatHasil(jawaban.hasil);
        result.classList.add("success");
    } catch (error) {
        result.textContent = "Terjadi kesalahan: " + error.message;
        result.classList.add("error");
    } finally {
        calculateButton.disabled = false;
        calculateButton.textContent = "Hitung hasil →";
    }
});

function formatHasil(data) {
    if (data === null || typeof data !== "object") {
        return String(data);
    }

    return Object.entries(data)
        .map(([key, value]) => {
            const label = key
                .replace(/_/g, " ")
                .replace(/\b\w/g, huruf => huruf.toUpperCase());

            const isi = typeof value === "number"
                ? Number(value.toPrecision(8)).toString()
                : typeof value === "object"
                    ? JSON.stringify(value)
                    : String(value);

            return `${label}: ${isi}`;
        })
        .join("\n");
}