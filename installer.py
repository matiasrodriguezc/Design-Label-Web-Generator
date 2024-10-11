import zipfile
import os
import subprocess
import sys


def check_python_version():
    """Verifica que la versión de Python sea 3.8."""
    current_version = sys.version_info
    if current_version.major != 3 or current_version.minor != 8:
        raise Exception("Se requiere Python 3.8 para continuar y se detecto Python " + str(current_version.major) + "." + str(current_version.minor))


def unzip_source_code():
    """Descomprime el .zip con el código fuente"""
    zip_file_path = os.path.join(os.getcwd(), "Web-Generator.zip")
    extract_folder = os.path.join(os.getcwd(), "Web-Generator")

    if not os.path.isfile(zip_file_path):
        raise FileNotFoundError(f"No se encontró el archivo {zip_file_path}")

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)


def change_dir():
    """Nos posicionamos en el directorio con el código fuente"""
    os.chdir(os.path.join(os.getcwd(), "Web-Generator"))


def setup_python_environment():
    """Configura el entorno virtual y actualiza pip."""
    try:
        # Configurar el entorno virtual
        subprocess.run(["python", "-m", "venv", "venv"], check=True)

        interpreter_path = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")

        # Instalar las dependencias dentro del entorno virtual
        subprocess.run([interpreter_path, "-m", "pip", "install", "--upgrade", "setuptools", "pip"], check=True)
        subprocess.run([interpreter_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([interpreter_path, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

    except subprocess.CalledProcessError as e:
        if e.output:
            error_message = e.output.decode().strip()
        else:
            error_message = str(e)
        print(f"Error durante la instalación de dependencias: {error_message}")
        raise

    except Exception as e:
        print(f"Error general durante la configuración del entorno: {str(e)}")
        raise


def create_pythonpath_variable():
    """Crea la variable de usuario PythonPath apuntando al directorio del proyecto."""
    project_dir = os.getcwd()
    os.system(f'setx PythonPath "{project_dir}"')


def install_rasa():
    """Instala Rasa 3.1.0 en el entorno virtual activado."""
    # Reemplaza el archivo venv/Lib/site-packages/rasa/core/channels/channel.py con resources/channel.py
    replace_file("resources/channel.py", "venv/Lib/site-packages/rasa/core/channels/channel.py")

    # Reemplaza el archivo venv/Lib/site-packages/rasa/core/channels/telegram.py con resources/telegram.py
    replace_file("resources/telegram.py", "venv/Lib/site-packages/rasa/core/channels/telegram.py")


def install_chocolatey():
    """Instala Chocolatey en el sistema si no está ya instalado."""
    print("------EN INSTALL CHOCOLATEY------")
    try:
        # Intenta verificar la versión de Chocolatey
        subprocess.run(["choco", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        # Si choco no está instalado, procede a instalarlo
        try:
            subprocess.run(["powershell.exe", "-Command", "Get-ExecutionPolicy -Scope CurrentUser"], check=True)
            subprocess.run(["powershell.exe", "-Command", "Set-ExecutionPolicy AllSigned -Scope CurrentUser"],
                           check=True)
            subprocess.run([
                "powershell.exe",
                "-Command",
                "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
            ], check=True)

            # Después de instalar Chocolatey, actualizar la variable PATH
            choco_install_path = "C:\\ProgramData\\chocolatey\\bin"
            current_path = os.getenv("PATH", "")
            if choco_install_path not in current_path:
                os.environ["PATH"] = f"{current_path};{choco_install_path}"
        except subprocess.CalledProcessError as e:
            print(f"Error durante la instalación de Chocolatey: {e}")
            raise  # Propaga el error para terminar la ejecución si falla la instalación


def install_ngrok():
    """Instala Ngrok utilizando Chocolatey."""
    print("------EN INSTALL NGROK------")
    try:
        subprocess.run(["powershell.exe", "-Command", "choco install ngrok -y"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación de ngrok: {e}")
        raise  # Propaga el error para terminar la ejecución si falla la instalación


def install_node():
    """Instala Node.js utilizando Chocolatey."""
    print("------EN INSTALL NODE------")
    try:
        subprocess.run(["powershell.exe", "-Command", "choco install nodejs-lts --version=\"20.15.0\" -y"], check=True)
        node_path = r"C:\Program Files\nodejs"
        npm_path = os.path.expandvars(r"%APPDATA%\npm")
        os.environ["PATH"] += os.pathsep + node_path + os.pathsep + npm_path
        subprocess.run(["powershell.exe", "-Command", "npm install -g create-next-app@14.2.4 -y"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación de Node.js: {e}")
        raise  # Propaga el error para terminar la ejecución si falla la instalación


def replace_file(source_file, target_file):
    """Reemplaza el contenido de un archivo con el contenido de otro archivo"""
    source_path = os.path.abspath(source_file)
    target_path = os.path.abspath(target_file)
    with open(source_path, 'rb') as source:
        with open(target_path, 'wb') as target:
            target.write(source.read())


if __name__ == "__main__":
    try:
        check_python_version()
        unzip_source_code()
        change_dir()
        setup_python_environment()
        create_pythonpath_variable()
        install_rasa()
        install_chocolatey()
        install_ngrok()
        install_node()
        print("Instalación completada con éxito. Reinicie su PC antes de proceder a la ejecución.")
    except Exception as e:
        print(f"Error durante la instalación: {str(e)}")
    finally:
        input("Presione Enter para cerrar...")  # Pausa al final del script
        sys.exit(1)
