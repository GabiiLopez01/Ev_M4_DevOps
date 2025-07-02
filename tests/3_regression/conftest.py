import sys
import os
from pathlib import Path

# Añade el directorio src al PATH
sys.path.append(str(Path(__file__).parent.parent.parent / 'src'))

from app import app as flask_app