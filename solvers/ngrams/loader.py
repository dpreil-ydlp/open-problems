"""Quadgram table loading interface."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from cipherkit import LANGS, load_table, score
__all__=['LANGS','load_table','score']
