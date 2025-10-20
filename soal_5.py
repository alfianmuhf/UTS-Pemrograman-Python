import os
import csv
import json
import logging

# === 1. Setup folder dan logging ===
os.makedirs("data", exist_ok=True)

# Setup logging (disimpan ke file)
logging.basicConfig(
    filename="data/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program dimulai.")

# === 2. Menulis file CSV ===
csv_file = "data/presensi.csv"
data_presensi = [
    ["nim", "nama", "hadir_uts"],
    ["2310001", "Andi", 1],
    ["2310002", "Budi", 0],
    ["2310003", "Citra", 1]
]

try:
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data_presensi)
    logging.info(f"Berhasil menulis file CSV: {csv_file}")
except Exception as e:
    logging.error(f"Gagal menulis file CSV: {e}")
    print("Terjadi kesalahan saat menulis file CSV.")

# === 3. Membaca CSV dan menghitung ringkasan ===
json_file = "data/ringkasan.json"

try:
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = len(rows)
    hadir = sum(int(r["hadir_uts"]) for r in rows)
    persentase = (hadir / total * 100) if total > 0 else 0

    ringkasan = {
        "total_mahasiswa": total,
        "jumlah_hadir": hadir,
        "persentase_hadir": round(persentase, 2)
    }

    with open(json_file, mode="w", encoding="utf-8") as f:
        json.dump(ringkasan, f, indent=4)

    logging.info(f"Berhasil membuat ringkasan JSON: {json_file}")
    print("Proses selesai. File ringkasan disimpan di 'data/ringkasan.json'.")

except FileNotFoundError:
    logging.error("File CSV tidak ditemukan saat membaca.")
    print("File CSV tidak ditemukan.")
except Exception as e:
    logging.error(f"Terjadi kesalahan saat membaca/mengolah data: {e}")
    print("Terjadi kesalahan saat membaca/mengolah data.")

logging.info("Program selesai.")
