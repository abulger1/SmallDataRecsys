from itertools import islice
import csv
import math

numSteps = 0

utmat = {}


def userImpressionWeights():
    global utmat
    with open('small_train.csv',  encoding="utf8") as file:
        reader = csv.reader(file)
        next(reader)
        currID = ""
        output = []
        useractions = []
        stop = False
        while not stop:
            try:
                curr = next(reader)
                if curr == None:
                    stop = True
                    break
                else:
                    if curr[0] != currID:
                        if len(useractions) != 0:
                            output.append(getweight(useractions))
                        useractions = []
                        currID = curr[0]
                    else:
                        useractions.append(curr)
            except StopIteration as e:
                output.append(getweight(useractions))
                break
    with open('output.csv', 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(output)


def getweight(userActions):
    global utmat
    userDict = {}
    count = 0
    for x in userActions:
        if isnumber(x[5]):
            if x[4] == "clickout item":
                store(userDict, x[5], -100000)
            else:
                proximity = len(userActions) - count
                if count == 0:
                    multiplier = 1
                else:
                    multiplier = userActions[count[2]] - userActions[(count - 1)[2]]
                store(userDict, x[5], 1000 * math.sqrt(multiplier) / proximity)
    ret = [userActions[0][0]]
    # Added some code to normalize values
    sumvalues = 0
    for k, v in userDict.items():
        sumvalues += v
    if len(list(userDict.items())) > 0:
        avgscore = sumvalues / len(list(userDict.items()))
    else:
        avgscore = 0
    for k, v in userDict.items():
        ret.append(k)
        ret.append(v - avgscore)
        userDict[k] = v - avgscore
    return ret


def store(dict, num, store):
    if num not in dict:
        dict[num] = store
    else:
        dict[num] += store


def isnumber(s):
    return s.replace('.', '', 1).isdigit()


userImpressionWeights()



# print(utmat)

# def getnextuser():
#     with open('kevoutput.csv', newline='') as f:
#         reader = csv.reader(f)
#         row1 = next(reader)
#         output=[]
#         row1=next(reader)
#         output.append(row1)
#         stop=False
#         userID = row1[0]
#         while(not stop):
#             row1=next(reader)
#             idNum=row1[0]
#             if idNum != userID:
#                 stop=True
#             else:
#                 output.append(row1)
#         numSteps=len(output)
