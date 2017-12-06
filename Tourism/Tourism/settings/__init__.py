from .base import *

# from .production import *
# print(BASE_DIR)

try:
	from .local import *
except:
	pass
