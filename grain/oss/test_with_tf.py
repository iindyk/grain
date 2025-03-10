import importlib

original_import = importlib.import_module
def _import_module(name, package=None):
  print(f"iindyk importing: {name}")
  return original_import(name, package)

importlib.import_module=original_import

import abc
import typing
import base64
import re

import tensorflow as tf
from grain import python as grain

print(f"iindyk: Done {grain.MapDataset}")
