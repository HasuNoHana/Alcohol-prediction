import numpy as np
import pandas as pd

from Tree import Tree


class RandomForest:

    #n = Number of samples in one tree
    #d = Number of features in one tree
    #n_estimators = Number of trees

    def __init__(self, n: int, d: int, n_estimators: int):
        self.n = n
        self.d = d
        self.n_estimators = n_estimators
        self.treesInfo = []

    def predict(self, test_df):
        for treeinfo in self.treesInfo:
            # take only features on with the tree was trained
            lables = test_df.drop(test_df.columns.difference(treeinfo[1]), axis=1)
            print(lables.head())

            #TODO get predictions from trees

    def fit(self, train_df):

        for treeIndex in range(self.n_estimators):#TODO works only if n = all samples
            #get n rows from train_df
            fsamples = train_df.sample(n=self.n, replace=False, axis=0)
            #get Dalc
            lables = fsamples.drop(fsamples.columns.difference(["Dalc"]), axis=1)
            #get d features
            samples = fsamples.sample(n=self.d, replace=False, axis=1)
            #add dalc to features
            samples["Dalc"] = lables

            tree = Tree(samples.columns.get_loc("Dalc"))
            newTree = tree.buildTree(samples, 0)

            columns = list(samples.columns)
            treeInfo = [newTree, columns]

            self.treesInfo.append(treeInfo)


    # def fit(self, xTrain, yTrain, feature_list):
    #     for i in range(self.n_estimators):
    #         chosenSamples = self.randomSamples(self.n, xTrain)
    #         for chosenSample in chosenSamples:
    #             chosenSamplesAndFeatures = self.randomFeatures(self.d, feature_list)
    #             print (chosenSamplesAndFeatures)
    #             train_df = pd.DataFrame(data=chosenSample[0:, 0:])  # values
    #             #             # index = data[1:, 0],  # 1st column as index
    #             #             # columns = data[0, 1:])
    #         # readyDataset = np.array()
    #         # # print(readyDataset)
    #         # # np.delete(readyDataset,0)
    #         # # print(readyDataset)
    #         # for chosenSample in chosenSamples:
    #         #     np.append(readyDataset,[self.randomFeatures(self.d, chosenSample)])
    #
    #         break

        # print(readyDataset)
            # cd = randomFeatures(d,)
        # train_df = pd.DataFrame(data=readyDataset[0:, 0:])  # values
        #             # index = data[1:, 0],  # 1st column as index
        #             # columns = data[0, 1:])
        # print(train_df)





    # def randomSamples(self, n, xTrain):
    #     number_of_rows = xTrain.shape[0]
    #     random_indices = np.random.choice(number_of_rows, size=n, replace=False)
    #     random_rows = xTrain[random_indices, :]
    #     # print(random_rows.shape)
    #     return random_rows
    #
    # def randomFeatures(self, d, chosenSamples):
    #     # number_of_columns = chosenSamples.shape[0]
    #     rng = np.random.default_rng()
    #     random_indices = rng.choice(chosenSamples, size=d, replace=False, axis = 0)
    #     # random_rows = chosenSamples[random_indices]
    #     # print(random_rows.shape)
    #     # print(random_rows)
    #     return random_indices