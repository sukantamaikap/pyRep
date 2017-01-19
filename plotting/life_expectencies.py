from matplotlib import pyplot
all_data = open("life_expectancies_usa.txt", "r").readlines()
years = []
male_life_expectancies = []
female_life_expectancies = []

for data in all_data:
    year, male_life_expectancy, female_life_expectency = data.split(',')
    years.append(year)
    male_life_expectancies.append(male_life_expectancy)
    female_life_expectancies.append(female_life_expectency)

pyplot.plot(years, male_life_expectancies, "bo-", label="Men")
pyplot.plot(years, female_life_expectancies, "mo-", label="female")
pyplot.ylabel("Age")
pyplot.xlabel("Expectancy")
pyplot.legend(loc="upper left")
pyplot.title("Life expectancy in US")
pyplot.show()
