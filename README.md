# arduino_radar

A radar-style object detection system built with an **Arduino Uno**, an **HC-SR04 ultrasonic sensor**, and an **SG90 servo**. Distance readings are streamed over serial and visualized in real time as a sweeping radar display using a **Python + Matplotlib** GUI.

## Files

| File | Purpose |
|------|---------|
| `arduino_radar.ino` | Arduino firmware — sweeps the servo and reads the HC-SR04 |
| `radar.py` | Python GUI that plots the radar in real time |
| `circuit_diagram.pdf` | Wiring reference |

## Hardware

- Arduino Uno
- HC-SR04 ultrasonic distance sensor
- SG90 micro servo

## Usage

1. Wire the circuit as shown in `circuit_diagram.pdf`.
2. Upload `arduino_radar.ino` to the Arduino.
3. Install the Python dependency and run the GUI:

   ```bash
   pip install pyserial matplotlib
   python radar.py
   ```

4. Set the serial port in `radar.py` (for example `COM3` on Windows, `/dev/ttyUSB0` on Linux) to match your board.
