# RC TRX Simulator

An ESP32 + Python project that simulates RC transmitter channels. Designed for testing RC vehicle firmware and signal logic without the need for a physical transmitter.

---

## 📁 Project Structure

```
RC_SIM/
├── src/                  # ESP32 firmware (PlatformIO)
│   └── main.cpp
├── APP/                  # GUI applications (Python)
│   ├── rcsim.py          # Polish version
│   └── rcsim_en.py       # English version
├── platformio.ini        # PlatformIO configuration
├── Connection diagram.png
├── README.md             # This file
└── .gitignore
```

---

## ⚙️ Requirements

### ESP32 Firmware

- Visual Studio Code with PlatformIO extension
- ESP32 DevKit v1 board or compatible
- USB cable for flashing

### Python GUI

- Python 3 (recommended 3.8+)
- `tkinter` (comes preinstalled on macOS and most Python installs)
- Optionally: `pyserial` if using real serial communication

---

## 🚀 How to Use

### 1. Flash Firmware to ESP32

1. Open the `RC_SIM` folder in Visual Studio Code.
2. Make sure PlatformIO extension is installed.
3. Connect your ESP32 via USB.
4. In PlatformIO, click **Upload** to flash the firmware.

### 2. Run the RC Simulator GUI

#### Polish version:

```bash
cd [/sciezka/do/katalogu/]APP
python3 rcsim.py
```

#### English version:

```bash
cd [patch/to/your/catalogue/]APP
python3 rcsim_en.py
```

You can use this GUI to simulate signals from 6 RC channels:
- CH1: Steering
- CH2: Throttle / Brake
- CH3: Potentiometer
- CH4: Button (monostable)
- CH5: 3-way switch
- CH6: 3-way switch

Each channel outputs a simulated RC value (in microseconds) between ~1000–2000 µs.

---

## 🔌 Wiring Reference

Refer to `Connection diagram.png` for correct wiring between:
- ESP32
- RC signal inputs (PWM)


---

## 🧾 License

This project is licensed under the MIT License.

---

## 👤 Author

**Tomasz**, 2025  
Language support: 🇵🇱 Polish and 🇬🇧 English
