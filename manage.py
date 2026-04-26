#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeployML.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Auto-activate venv logic
        import subprocess
        venv_python = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")
        if os.path.exists(venv_python) and sys.executable != venv_python:
            result = subprocess.run([venv_python] + sys.argv)
            sys.exit(result.returncode)
        
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
