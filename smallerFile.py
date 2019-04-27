file = open('C:\\Users\\banana\\PycharmProjects\\trivago\\data\\train.csv', encoding="utf8")
line = file.readline()

output = open("small_train.csv", 'w', encoding="utf8")

for i in range(10000):
    output.write(line)
    line = file.readline()

file.close()
output.close()
