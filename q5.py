import matplotlib.pyplot as plot

# Question 5
# Create a chart of the popularity of the programming Languages below.

# Sample data
langs = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# creates subplot
fig, axes = plot.subplots()

# creates the pie chart, formats float values, applies a shadow, and pushes the highest valued section out of the chart
axes.pie(pop, labels=langs, autopct='%1.1f%%', shadow=True, explode=(0.1, 0, 0, 0, 0, 0))

# shows the pie chart
plot.show()
