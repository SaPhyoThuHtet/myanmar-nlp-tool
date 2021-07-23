# Syllable Segmenter for zawgyi encoding (burmese)
# Usage: python syllbreak-zawgyi.py input
# Phyo Thu Htet, Information Science Student, UTYCC
# Stay at Home
# 2020, Last Modified : 29 Dec 2019

import sys
import re

with open(sys.argv[1],'r') as input_file:
    for i in input_file:

        line = re.sub(r'(ေ*ျ*ႀ*ၿ*ၾ*[က-အ|႐|ႏ|ဥ|ဦ|႒]([က-အ]့*္[့း]*|[ါ-ာ]|[ိ-ူ]|[ဲ-္]|်|[ြ-ှ]|[ၐ-ၽ]|[ႁ-ႎ]|[႑-႟]){0,}|.)',r'\1 ',i.strip())
        print(line)
