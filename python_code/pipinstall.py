import os
import subprocess
import sys

def install_pip():
    try:
        import pip
        print("")
    except ImportError:
        print("Package not Found: pip")
        try:
            import urllib.request
            url = "https://bootstrap.pypa.io/get-pip.py"
            print("Installing Package: pip - https://bootstrap.pypa.io/get-pip.py")
            urllib.request.urlretrieve(url, "get-pip.py")
            print("Installing: pip")
            subprocess.check_call([sys.executable, "get-pip.py"])

            print("Package Sucessful Installed!")
            os.remove("get-pip.py")
        except Exception as e:
            print(f"Error while Installing pip: {e}")
            
install_pip()
try:
    import pip
    print("")
except ImportError:
    print("ERROR while Istalling Package: pip")

def install_pyserial():
    try:
        import serial
        print("Instalation Sucess!")
    except ImportError:
        print("Install in progress...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyserial"])
        print("Instalation Sucess!")
install_pyserial()

try:
    import serial
except ImportError:
    print("ERROR- Can not Import PySerial")
    
def install_tkinter():
    try:
        import tkinter
        print("Instalation Sucess!")
    except ImportError:
        print("Install in progress...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinter"])
        print("Instalation Sucess!")
install_tkinter()

try:
    import tkinter
except ImportError:
    print("ERROR- Can not Import tkinter")
    
    
def install_custt():
    try:
        import customtkinter
        print("Instalation Sucess!")
    except ImportError:
        print("Install in progress...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "customtkinter"])
        print("Instalation Sucess!")
install_custt()

try:
    import customtkinter
except ImportError:
    print("ERROR- Can not Import customtkinter")

