# Elden Ring Death Counter 💀

A lightweight computer vision tool that automatically counts player deaths in **Elden Ring**
by detecting the death screen using screen-based template matching.

Lekki projekt wykorzystujący computer vision do automatycznego zliczania zgonów w **Elden Ring**
na podstawie wykrywania ekranu śmierci.

---

## 🇬🇧 English

### Features
- Automatic death detection (no manual input)
- Screen-based approach (no memory access, anti-cheat safe)
- Always-on-top counter window
- CSV logging with timestamps

### How it works
The application captures the game screen in real time and uses OpenCV template
matching to detect the death screen. A cooldown mechanism prevents duplicate
counts for a single death.

### Requirements
- Python 3.11+ (recommended: Python 3.12)
- Windows (tested on Windows 11)
- Elden Ring running in windowed or borderless mode

### Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
Setup
Run the game and trigger the death screen.

Take a screenshot of the death message.

Crop only the central death text and save it as:

Skopiuj kod
you_died_template.png
in the project root directory.

Run
bash
Skopiuj kod
python main.py
A small always-on-top counter window will appear and update automatically after
each detected death.

Why screen-based detection?
This project intentionally avoids reading game memory or injecting code into
the game process. Instead, it uses real-time screen capture and computer vision
techniques to detect death events.

Benefits:

Anti-cheat safe

Game-version independent

Easily adaptable to other games or screen-based events

Project status
The project is fully functional for its core purpose.
Future improvements may include session persistence, boss-specific statistics,
and historical data visualization.

Disclaimer
This project is not affiliated with FromSoftware or Bandai Namco.
It is a personal, non-commercial project created for educational purposes.

🇵🇱 Polski
Funkcjonalności
Automatyczne wykrywanie zgonów (bez ręcznego klikania)

Podejście oparte na obrazie (brak ingerencji w pamięć gry, bezpieczne dla anti-cheat)

Małe okienko z licznikiem zawsze na wierzchu

Zapisywanie danych do pliku CSV wraz ze znacznikiem czasu

Jak to działa
Aplikacja przechwytuje obraz ekranu w czasie rzeczywistym i wykorzystuje
template matching z biblioteki OpenCV do wykrywania ekranu śmierci.
Mechanizm cooldown zapobiega wielokrotnemu zliczaniu jednego zgonu.

Wymagania
Python 3.11+ (rekomendowany: Python 3.12)

Windows (testowane na Windows 11)

Elden Ring uruchomiony w trybie okna lub borderless

Instalacja
Sklonuj repozytorium i zainstaluj zależności:

bash
Skopiuj kod
pip install -r requirements.txt
Konfiguracja
Uruchom grę i doprowadź do ekranu śmierci.

Wykonaj zrzut ekranu komunikatu o śmierci.

Wytnij centralny fragment z tekstem i zapisz go jako:

Skopiuj kod
you_died_template.png
w głównym katalogu projektu.

Uruchomienie
bash
Skopiuj kod
python main.py
Na ekranie pojawi się niewielkie okienko z licznikiem zgonów, które automatycznie
aktualizuje się po każdej wykrytej śmierci.

Dlaczego wykrywanie na podstawie obrazu?
Projekt celowo nie korzysta z odczytu pamięci gry ani nie ingeruje w jej proces.
Zamiast tego używa przechwytywania ekranu oraz technik computer vision do
wykrywania zdarzeń.

Zalety:

Bezpieczne dla systemów anti-cheat

Niezależne od wersji gry

Łatwe do zaadaptowania do innych gier lub zdarzeń ekranowych

Status projektu
Projekt jest w pełni funkcjonalny w zakresie swojego głównego celu.
W przyszłości możliwa jest rozbudowa m.in. o zapamiętywanie sesji,
statystyki bossów oraz wizualizację danych historycznych.

Informacja prawna
Projekt nie jest powiązany z FromSoftware ani Bandai Namco.
Jest to projekt niekomercyjny, stworzony w celach edukacyjnych.
