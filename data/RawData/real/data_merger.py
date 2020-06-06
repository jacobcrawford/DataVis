from pathlib import Path
import pandas as pd
import numpy as np
################################################################################################################
# This file is for merging the csv files in testSet and trainSet into one big datafile for each of the tables. #
################################################################################################################

ptest = Path('./testSet')
ptrain = Path('./trainingSet')

test_files = [x for x in ptest.iterdir() if x.is_file()]
train_files = [x for x in ptrain.iterdir() if x.is_file()]

for p1 in test_files:
    name1 = p1.as_posix().replace("testSet/","").replace("test_","")
    print(name1)
    for p2 in train_files:
        name2 = p2.as_posix().replace("trainingSet/","").replace("training_","")
        if name1 == name2:

            df1 = pd.read_csv(p1.as_posix())

            df2 = pd.read_csv(p2.as_posix())

            if name1 != "SyncPatient.csv": # SyncPatient has a diabetes column in trainingSet
                assert np.array_equal(df1.columns,df2.columns)

            df3 = df1.append(df2)
            assert df3.shape[0] == df1.shape[0] + df2.shape[0] # check that the rows numbers are summed

            df3.to_csv(name1)

