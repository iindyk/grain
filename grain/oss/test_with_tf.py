import importlib
print("importlib")

original_import = importlib.import_module
def _import_module(name, package=None):
  print(f"iindyk importing: {name}")
  return original_import(name, package)

importlib.import_module=original_import

import abc
print("abc")
import typing
print("typing")
import base64
print("base64")
import re
print("re")

import tensorflow as tf
print("re")
from grain import python as grain
print("grain")
print(f"iindyk: Done {grain.MapDataset}")
