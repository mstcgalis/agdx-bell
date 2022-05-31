from logic import *

harmonogram_path = os.path.normpath("data/harmonogram.json")

bell = timer(load_harmonogram(harmonogram_path))
bell.arm