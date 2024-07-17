import matplotlib.pyplot as plt

'''
created venv and installed matplotlib
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install matplotlib


venv is on the same level as the project folder with .gitignore (outside of matplotlib folder)
'''

# Create a figure and axis
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
population = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

plt.plot(year, population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population growth')
plt.show()