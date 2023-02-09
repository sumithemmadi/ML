import csv
import matplotlib.pyplot as plt


with open('Salary_Data.csv', 'r') as file:
    csvreader = csv.reader(file)
    lines = file.readlines()

lines.remove(lines[0])
X = []
Y = []

for x in lines:
    x = x.replace('\n', '')
    x = x.split(',')
    X.append(float(x[0]))
    Y.append(float(x[1]))
n = len(X)


def linear_regression(X, Y):
    Xm = (sum(X))/n
    Ym = (sum(Y))/n

    XY = [X[i]*Y[i] for i in range(n)]
    XX = [X[i]**2 for i in range(n)]

    sum_xy = sum(XY) - n*Xm*Ym
    sum_xx = sum(XX) - n*Xm*Xm
    b = sum_xy/sum_xx
    a = Ym - b*Xm
    return a, b


a, b = linear_regression(X, Y)
plt.figure(1)
plt.plot(X, Y, 'o')
X = [X[0], X[n-1]]
Y = [a+b*X[0], a+b*X[1]]
plt.plot(X, Y)
plt.show()
