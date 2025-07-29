import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading
import time

channels = [0] * 6

root = tk.Tk()
root.title("Symulator RC na ESP32")

us_labels = [tk.StringVar() for _ in range(6)]
ch5_var = tk.IntVar()
ch6_var = tk.IntVar()

ser = None
running = True

def send_loop():
    global ser
    while running:
        if ser:
            packet = ",".join(str(ch) for ch in channels) + "\n"
            try:
                ser.write(packet.encode())
            except Exception as e:
                status_var.set(f"Błąd: {e}")
        time.sleep(0.05)

def update_channel(index, value):
    channels[index] = int(float(value))

def toggle_button():
    channels[3] = 100
    root.after(1000, lambda: update_channel(3, 0))

def set_switch(chan, val):
    channels[chan] = val

def connect_serial():
    global ser
    port = port_var.get()
    try:
        ser = serial.Serial(port, 115200)
        status_var.set(f"Połączono z {port}")
    except Exception as e:
        status_var.set(f"Błąd: {e}")

def update_us_labels():
    for i in range(6):
        us = int(1500 + (channels[i] / 100) * 500)
        us_labels[i].set(f"{us} µs")
    root.after(50, update_us_labels)

port_var = tk.StringVar()
status_var = tk.StringVar(value="Niepołączono")

# Wiersz 0 – port
ttk.Label(root, text="Port:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ports = serial.tools.list_ports.comports()
port_menu = ttk.Combobox(root, textvariable=port_var, width=20)
port_menu["values"] = [port.device for port in ports]
port_menu.grid(row=0, column=1, padx=5, sticky="we")
ttk.Button(root, text="Połącz", command=connect_serial).grid(row=0, column=2, padx=5)

# Nagłówek
ttk.Label(root, text="Kanały", font=("TkDefaultFont", 10, "bold")).grid(row=1, column=0, pady=(10, 0), sticky="w")

# CH1–CH3
for i, label in enumerate(["CH1 Kierownica", "CH2 Gaz/Hamulec", "CH3 Potencjometr"]):
    ttk.Label(root, text=label).grid(row=i+2, column=0, sticky="w", padx=5)
    ttk.Scale(root, from_=-100, to=100, orient="horizontal",
              command=lambda val, idx=i: update_channel(idx, val)).grid(row=i+2, column=1, padx=5, sticky="we")
    ttk.Label(root, textvariable=us_labels[i], width=7).grid(row=i+2, column=2, padx=5, sticky="e")

# CH4 – przycisk
ttk.Label(root, text="CH4 Przycisk").grid(row=5, column=0, sticky="w", padx=5)
ttk.Button(root, text="Naciśnij", command=toggle_button, width=10).grid(row=5, column=1, padx=5)
ttk.Label(root, textvariable=us_labels[3], width=7).grid(row=5, column=2, padx=5, sticky="e")

# CH5 i CH6
for idx, (ch, label, var) in enumerate([
    (4, "CH5 Przełącznik", ch5_var),
    (5, "CH6 Przełącznik", ch6_var)
]):
    row = 6 + idx
    ttk.Label(root, text=label).grid(row=row, column=0, sticky="w", padx=5)
    frame = ttk.Frame(root)
    frame.grid(row=row, column=1)
    for i, val in enumerate([-100, 0, 100]):
        ttk.Radiobutton(
            frame, text=str(val), value=val, variable=var,
            command=lambda v=val, ch=ch: set_switch(ch, v)
        ).pack(side="left", padx=4)
    ttk.Label(root, textvariable=us_labels[ch], width=7).grid(row=row, column=2, padx=5, sticky="e")

# Status
ttk.Label(root, textvariable=status_var).grid(row=8, column=0, columnspan=3, pady=10)

# Uruchomienie
threading.Thread(target=send_loop, daemon=True).start()
update_us_labels()

def on_closing():
    global running
    running = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
