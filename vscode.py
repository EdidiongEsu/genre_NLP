import re
import os
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from itertools import repeat
from sklearn.feature_extraction import stop_words
from collections import Counter
from operator import itemgetter


pd.set_option('display.max_colwidth', -1)
a=[3,5,6,7]
b=[4,6,7]

a= set(a)
b= set(b)

a.intersection(b)

print('\nEdidiong Esu')

import pandas as pd
df= pd.read_csv('okadabooks_main.csv')

df.info()

pd.set_option('display.max_colwidth', -1)

df.head()



def poll():
    return print('Test running this')


import os
import matplotlib.pyplot as plt  
plt.hist([3,2,3,4])
plt.show()

os.getcwd()