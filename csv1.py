# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import csv
# # # x = []
# # # y = []



# # # a = pd.read_csv('Sample.csv')
# # # pd.scatter(a)

# # # a.plot.scatter(x='x', y='y',title='Scatter Plot')
# # # plt.show()


# # # # with open('Sample.csv','r') as csvfile:
# # # #     plots = csv.reader(csvfile, delimiter=',')

# # # #     for row in plots:
# # # #         x.append(int(row[1]))
# # # #         y.append(int(row[1]))

# # # # plt.scatter(x, y, label='Loaded from file!')
# # # # plt.xlabel('x')
# # # # plt.ylabel('y')
# # # # plt.title('Interesting Graph\nCheck it out')
# # # # plt.legend()
# # # # plt.show()


# # import pandas as pd
# # import matplotlib.pyplot as plt
# # df = pd.read_csv("Sample.csv")
# # df.plot.scatter(x='x', y='y',title='Scatter Plot')
# # plt.show()



# import matplotlib.pyplot as plt
# import csv
# from scipy import stats

# x = plots['X'].values
# y = df[]

# with open('Sample.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')

#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)


# plt.plot(x,intercept+slope*x, 'r', label='fitted line')

# plt.scatter(x, y)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Scatter Plot')
# plt.show()


from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sample.csv")
x = df['X'].values
y = df['Y'].values

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create a scatter plot of the data
df.plot.scatter(x='X', y='Y',title='Scatter Plot')

# Plot the regression line on top of the scatter plot
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()

