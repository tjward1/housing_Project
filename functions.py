# import numpy
import numpy as np
# import regular expressions
import re


# function to clean multiple columns by replacing corrupt data
# with specified ranges of random numbers
def cleanRandom(fileNum, column, randLeast, randMost):
    for data in fileNum[column]:
        # generate a random number (randLeast inclusive, randMost exclusive)
        clean = np.random.randint(randLeast, randMost)
        # for each corrupt data, replace with the random number
        cleanData = re.sub(r"[A-Z]{4}$", f'{clean}', data)
        # replace old column with new column of clean data
        fileNum[column] = fileNum[column].replace(f"{data}", f"{cleanData}")

