# RC TRX Simulator

Projekt ESP32 + Python, który symuluje kanały nadajnika RC. Zaprojektowany do testowania firmware RC i logiki sygnałów bez potrzeby używania fizycznego nadajnika.

---

## 📁 Struktura projektu

```
RC_SIM/
├── src/                  # Firmware ESP32 (PlatformIO)
│   └── main.cpp
├── APP/                  # Aplikacje GUI (Python)
│   ├── rcsim.py          # Wersja polska
│   └── rcsim_en.py       # Wersja angielska
├── platformio.ini        # Konfiguracja PlatformIO
├── Connection diagram.png
├── README.md             # Ten plik
└── .gitignore
```

---

## ⚙️ Wymagania

### Firmware ESP32

- Visual Studio Code z rozszerzeniem PlatformIO
- Płytka ESP32 DevKit v1 lub kompatybilna
- Kabel USB do programowania

### GUI Python

- Python 3 (zalecana wersja 3.8+)
- `tkinter` (domyślnie dostępny w macOS i większości instalacji Pythona)
- Opcjonalnie: `pyserial`, jeśli używasz rzeczywistego połączenia szeregowego

---

## 🚀 Jak używać

### 1. Wgranie firmware na ESP32

1. Otwórz folder `RC_SIM` w Visual Studio Code.
2. Upewnij się, że masz zainstalowane rozszerzenie PlatformIO.
3. Podłącz ESP32 przez USB.
4. W PlatformIO kliknij **Upload**, aby wgrać firmware.

### 2. Uruchomienie GUI RC Simulator

#### Wersja polska:

```bash
cd [/sciezka/do/katalogu/]APP
python3 rcsim.py
```

#### Wersja angielska:

```bash
cd [patch/to/your/catalogue/]APP
python3 rcsim_en.py
```

GUI pozwala na symulację sygnałów z 6 kanałów RC:
- CH1: Kierownica
- CH2: Gaz / Hamulec
- CH3: Potencjometr
- CH4: Przycisk (monostabilny)
- CH5: Przełącznik trójpozycyjny
- CH6: Przełącznik trójpozycyjny

Każdy kanał emituje zasymulowaną wartość RC (w mikrosekundach) z przedziału ~1000–2000 µs.

---

## 🔌 Schemat połączeń

Zobacz `Connection diagram.png`, aby poprawnie połączyć:
- ESP32
- Wejścia sygnału RC (PWM)


---

## 🧾 Licencja

Projekt udostępniony na licencji MIT.

---

## 👤 Autor

**Tomasz**, 2025  
Obsługa języków: 🇵🇱 polski i 🇬🇧 angielski
