# get prices of each item
import time
import statistics
start = time.time()
file = open("C:\\Users\\banana\\PycharmProjects\\trivago\\data\\train.csv", 'r', encoding="utf8")
# file = open("C:\\Users\\banana\\PycharmProjects\\trivago\\data\\train.csv", 'r')

dict = {}
line = file.readline()
# print('Running')
while line:
# for i in range(1000):
    line = file.readline().split(',')
    if len(line) < 5:
        print('oof')
    elif line[4] == "clickout item":

        # line futzing
        items = line[-2].split('|')
        prices = line[-1].split('|')
        prices[-1] = prices[-1].strip('\n')

        if len(items) != len(prices):
            print('this should never print!!!')

        # print(type(items))
        # processing impression ITEMS & PRICES
        for j in range(len(items)):
            if items[j] in dict:
                if prices[j] != dict[items[j]][0]:
                    dict[items[j]].append(prices[j])
                    # print('hi')
            else:
                dict[items[j]] = [prices[j]]
                # print('hmm')

# UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 845: character maps to <undefined>


#print(len(dict))
end = time.time()
print(end - start)

for i in range(len(dict.keys())):
    if (len(dict[list(dict.keys())[i]])) > 1:
        ls = dict[list(dict.keys())[i]]
        for j in range(len(ls)):
            ls[j] = int(ls[j])
        avg_price = int(statistics.mean(ls))
        dict[list(dict.keys())[i]] = avg_price
    else:
        dict[list(dict.keys())[i]] = int(dict[list(dict.keys())[i]][0])

print(len(dict))



