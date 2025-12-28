import time
import csv
from datetime import datetime
import threading

import cv2
import numpy as np
import mss
import tkinter as tk

# ====== USTAWIENIA ======
TEMPLATE_PATH = "you_died_template.png"

THRESHOLD = 0.72
PULL_INTERVAL = 0.20
COOLDOWN_SEC = 8.0

# centrum ekranu
CROP_X1, CROP_X2 = 0.25, 0.75
CROP_Y1, CROP_Y2 = 0.35, 0.70

CSV_PATH = "deaths.csv"


MONITOR_INDEX = 2
# ========================


def load_template(path: str) -> np.ndarray:
    tmpl = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if tmpl is None:
        raise FileNotFoundError(
            f"Nie widzę template: {path}\n"
            f"Upewnij się, że plik jest w tym samym folderze co main.py."
        )
    return tmpl


def append_csv(death_no: int, match_score: float) -> None:
    new_file = False
    try:
        with open(CSV_PATH, "r", encoding="utf-8") as _:
            pass
    except FileNotFoundError:
        new_file = True

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "death_number", "match_score"])
        writer.writerow([datetime.now().isoformat(timespec="seconds"), death_no, f"{match_score:.3f}"])


def counter_loop(shared_state: dict, stop_event: threading.Event):
    template = load_template(TEMPLATE_PATH)
    th, tw = template.shape[:2]

    death_count = 0
    last_count_time = 0.0

    with mss.mss() as sct:
        monitor = sct.monitors[MONITOR_INDEX]

        print("Start. Ctrl+C w oknie terminala nie zawsze zatrzyma wątek; zamknij okienko licznika.")
        print(f"THRESHOLD={THRESHOLD}, COOLDOWN={COOLDOWN_SEC}s, INTERVAL={PULL_INTERVAL}s")
        print(f"Zapis do: {CSV_PATH}")

        while not stop_event.is_set():
            img = np.array(sct.grab(monitor))  # BGRA
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            H, W = gray.shape[:2]
            x1, x2 = int(W * CROP_X1), int(W * CROP_X2)
            y1, y2 = int(H * CROP_Y1), int(H * CROP_Y2)
            roi = gray[y1:y2, x1:x2]

            if roi.shape[0] < th or roi.shape[1] < tw:
                # jeśli ktoś zmieni rozdzielczość/ROI na absurd
                time.sleep(PULL_INTERVAL)
                continue

            res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)

            now = time.time()
            if max_val >= THRESHOLD and (now - last_count_time) >= COOLDOWN_SEC:
                death_count += 1
                last_count_time = now
                shared_state["count"] = death_count
                shared_state["last_match"] = float(max_val)
                append_csv(death_count, max_val)
                print(f"💀 Zgon #{death_count} (match={max_val:.3f})")

            time.sleep(PULL_INTERVAL)


def start_ui():
    shared_state = {"count": 0, "last_match": 0.0}
    stop_event = threading.Event()

    # --- UI (Tkinter) ---
    root = tk.Tk()
    root.title("Death Counter")
    root.attributes("-topmost", True)  # zawsze na wierzchu
    root.resizable(False, False)

    # małe okienko
    root.geometry("260x90+20+20")  # szer x wys + x + y

    label_count = tk.Label(root, text="💀Śmierci: 0", font=("Segoe UI", 24, "bold"))
    label_count.pack(expand=True)


    def tick():
        label_count.config(text=f"💀Śmierci: {shared_state['count']}")
        root.after(200, tick)

    def on_close():
        stop_event.set()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # wątek liczenia
    t = threading.Thread(target=counter_loop, args=(shared_state, stop_event), daemon=True)
    t.start()

    tick()
    root.mainloop()


if __name__ == "__main__":
    start_ui()
