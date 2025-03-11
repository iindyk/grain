# import importlib
# print("importlib", flush=True)

# original_import = importlib.__import__
# def _import_module(*args, **kwargs):
#   print(f"iindyk importing: {args[0]}", flush=True)
#   return original_import(*args, **kwargs)

# importlib.__import__=original_import

# import abc
# print("abc", flush=True)
# import typing
# print("typing", flush=True)
# import base64
# print("base64", flush=True)
# import re
# print("re", flush=True)

#import gc
#gc.disable()
import tensorflow as tf
print(f"iindyk: imported TF", flush=True)
from array_record.python import array_record_module

# print("tf", flush=True)
print(f"iindyk: Done {tf.Tensor}", flush=True)
