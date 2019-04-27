import pandas as pd
import time

#
# train = pd.read_csv("C:\\Users\\banana\\PycharmProjects\\trivago\\data\\train.csv", nrows=1000)
# # train = pd.read_csv("C:\\Users\\banana\\PycharmProjects\\trivago\\data\\train.csv")
#
# print(train.shape)
#
# users = list(set(list(train['user_id'])))
# users.sort()
#
# pd.set_option('display.max_colwidth', 10000)
# pd.set_option('display.width', 10000)
# pd.set_option('display.max_columns', 10000)
#
# print(len(users))
# print(train)
#

# print('done!!')


print('Formatting utility matrix...')
def util_matrix_format():
    start = time.time()
    util_mat_file = open('C:\\Users\\banana\\PycharmProjects\\trivago\\src\\content_based\\output.csv')
    line = util_mat_file.readline()
    util_mat = {}
    while line:
        line = line.split(',')
        name = line[0]
        item_weights = line[1:]
        weights = {}
        j = 0
        for i in range(len(item_weights)//2):
            weights[item_weights[j]] = item_weights[j+1].strip('\n')
            j += 2
        util_mat[name] = weights
        line = util_mat_file.readline()
    end = time.time()
    print(end - start)
    return util_mat

print(util_matrix_format())