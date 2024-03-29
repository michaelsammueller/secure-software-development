'''
This file is necessary for importing from regular packages contained elsewhere
in the project i.e files not nested in this folder.

The code below ensures that the root of the project is included
in the system path. This allows us to import from files using the relative
path from the root of the project.

'''
from pathlib import Path
import sys


path = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(path))

from classes.commandline_interface import CommandLineInterface
from classes.sensors.geigercounter import GeigerCounter
from classes.sensors.thermometer import Thermometer
from classes.infosec.authorisation_service import AuthorisationService
