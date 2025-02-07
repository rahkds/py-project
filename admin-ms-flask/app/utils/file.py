import os
from app.extensions.mongodb import MongoConnection
import importlib
import subprocess

class FileUitl:
    @staticmethod
    def execute_mongo_script(script_file : str, conn : MongoConnection):
        if os.path.exists(script_file):
            script_file = os.path.abspath(script_file)
            conn_str = conn.conn_str
            result = subprocess.run([f"mongosh", f"{conn_str}", "--file", f"{script_file}"], capture_output=True, text=True)
            return result.stdout  # Output of the command

    @staticmethod
    def load_module_by_path(module_path):
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module