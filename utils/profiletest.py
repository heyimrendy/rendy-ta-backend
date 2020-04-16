# profile.py

import pstats
import cProfile

import files

cProfile.runctx('files.get_full_path("files.py")', globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
