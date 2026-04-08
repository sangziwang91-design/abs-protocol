import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.scheduler import run_all_tasks

run_all_tasks()
