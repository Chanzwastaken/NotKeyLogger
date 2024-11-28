# NotKeylogger

`NotKeylogger` is a lightweight, minimalistic keylogger written in Python using the `pynput` library. This project captures keystrokes in the background and logs them to a file with a timestamp. 

> **Disclaimer**: This project is for educational purposes only. Unauthorized use of keyloggers may violate laws and regulations. Ensure you have proper consent before using this tool.

---

## Features
- **Background Execution**: Runs silently in the background with no visible terminal window.
- **Accurate Timestamps**: Logs keystrokes every second with timestamps.
- **Thread-Safe Buffering**: Keystrokes are stored in a buffer and written to the log file at regular intervals.
- **Formatted Log File**: Outputs keystrokes in an easy-to-read format.

---

## Requirements
- Python 3.6+
- Libraries: `pynput` (install via `pip install pynput`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NotKeylogger.git
   cd NotKeylogger
   ```

2. Install dependencies:
   ```bash
   pip install pynput
   ```

3. Save the script as `notkeylogger.pyw` to hide the terminal window when running.

---

## How It Works

1. **Keystroke Logging**:
   - Captures all typed characters, including special keys like Enter, Shift, etc.
   - Logs these keystrokes every second as a single entry, appending them to `keylogger.log`.

2. **Log File Format**:
   The log file `keylogger.log` will look like:
   ```
   [2024-11-28 10:25:01] password123
   [2024-11-28 10:25:02] [SHIFT]Hello[SPACE]World[ENTER]
   ```

3. **Stealth Mode**:
   - The script hides the console window using the `ctypes` library, ensuring it runs silently in the background.
   - The script can only be terminated via Task Manager, where it appears under the name `notkeylogger`.

---

## Running the Keylogger

1. **Run in the Background**:
   - Execute the script:
     ```bash
     pythonw notkeylogger.pyw
     ```

   - Alternatively, convert it to an executable:
     ```bash
     pyinstaller --onefile --noconsole --name notkeylogger notkeylogger.pyw
     ```
     The output executable can be run directly.

2. **Output File**:
   - The captured keystrokes are saved to `keylogger.log` in the same directory as the script.

---

## Configurable Behavior

- **Log Interval**:
  The log interval is set to **1 second**. Modify the `time.sleep(1)` in the `write_to_file` function to adjust this.

- **Special Key Formatting**:
  Special keys are wrapped in square brackets, e.g., `[ENTER]`, `[SHIFT]`. This behavior can be customized in the `on_press` function.

---

## Example Use Cases
- Testing keyboard inputs.
- Educational purposes for understanding how keyloggers work.
- Learning about Python multithreading and file handling.
- Stealing your friend gaming account! (not recommended)

---

## Legal Disclaimer
This software is intended for ethical and educational use only. The developer is not responsible for any misuse or damage caused by this tool. Ensure compliance with all applicable laws and regulations.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and create a pull request for any improvements.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
