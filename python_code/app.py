import customtkinter as ctk
import serial
import serial.tools.list_ports
import threading

class SerialLCDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LCD Controller")
        self.root.geometry("500x400")
        ctk.set_appearance_mode("dark")  # Alternativ: "light"
        ctk.set_default_color_theme("blue")  # Alternativ: "green", "dark-blue"

        # Variablen
        self.selected_port = ctk.StringVar(value="Select Port")
        self.baudrate = ctk.StringVar(value="9600")
        self.text_to_send = ctk.StringVar()
        self.serial_connection = None

        # GUI erstellen
        self.create_widgets()

    def create_widgets(self):
        # Titel
        ctk.CTkLabel(self.root, text="LCD Controller", font=("Arial", 20, "bold")).pack(pady=10)

        # Verbindungsrahmen
        connection_frame = ctk.CTkFrame(self.root)
        connection_frame.pack(pady=10, padx=10, fill="x")

        # Port-Auswahl
        ctk.CTkLabel(connection_frame, text="Port:").grid(row=0, column=0, padx=5, pady=5)
        self.port_menu = ctk.CTkOptionMenu(connection_frame, variable=self.selected_port, values=self.get_ports())
        self.port_menu.grid(row=0, column=1, padx=5, pady=5)

        # Baudrate-Auswahl
        ctk.CTkLabel(connection_frame, text="Baudrate:").grid(row=1, column=0, padx=5, pady=5)
        self.baud_menu = ctk.CTkOptionMenu(connection_frame, variable=self.baudrate, values=["9600", "115200", "57600", "19200"])
        self.baud_menu.grid(row=1, column=1, padx=5, pady=5)

        # Verbinden/Trennen-Knopf
        self.connect_button = ctk.CTkButton(connection_frame, text="Verbinden", command=self.connect_serial)
        self.connect_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Text-Steuerung
        text_frame = ctk.CTkFrame(self.root)
        text_frame.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(text_frame, text="Text eingeben:").grid(row=0, column=0, padx=5, pady=5)
        self.text_entry = ctk.CTkEntry(text_frame, textvariable=self.text_to_send, width=300)
        self.text_entry.grid(row=0, column=1, padx=5, pady=5)

        # Senden-Knöpfe
        ctk.CTkButton(self.root, text="Text Senden", command=self.send_text).pack(pady=5)
        ctk.CTkButton(self.root, text="Text Scrollen", command=self.send_scroll).pack(pady=5)

        # Log-Anzeige
        self.log_box = ctk.CTkTextbox(self.root, width=450, height=100)
        self.log_box.pack(pady=10, padx=10)
        self.log_message("Willkommen beim LCD Controller!")

    def get_ports(self):
        """Listet verfügbare Ports auf."""
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports] or ["Keine Ports gefunden"]

    def connect_serial(self):
        """Verbindet oder trennt die serielle Verbindung."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            self.serial_connection = None
            self.connect_button.configure(text="Verbinden")
            self.log_message("Verbindung getrennt.")
        else:
            try:
                self.serial_connection = serial.Serial(
                    self.selected_port.get(),
                    int(self.baudrate.get()),
                    timeout=1
                )
                self.connect_button.configure(text="Trennen")
                self.log_message(f"Verbunden mit {self.selected_port.get()} @ {self.baudrate.get()} baud.")
            except Exception as e:
                self.log_message(f"Fehler: {e}")

    def send_text(self):
        """Sendet Text an den Arduino."""
        if self.serial_connection and self.serial_connection.is_open:
            text = self.text_to_send.get()
            self.serial_connection.write(f"text:{text}\n".encode('utf-8'))
            self.log_message(f"Gesendet: {text}")
        else:
            self.log_message("Fehler: Keine serielle Verbindung.")

    def send_scroll(self):
        """Sendet einen Scroll-Befehl an den Arduino."""
        if self.serial_connection and self.serial_connection.is_open:
            text = self.text_to_send.get()
            self.serial_connection.write(f"scroll:{text}\n".encode('utf-8'))
            self.log_message(f"Scroll-Befehl gesendet: {text}")
        else:
            self.log_message("Fehler: Keine serielle Verbindung.")

    def log_message(self, message):
        """Zeigt eine Nachricht im Log an."""
        self.log_box.insert("end", f"{message}\n")
        self.log_box.see("end")

def run_app():
    root = ctk.CTk()
    app = SerialLCDApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
