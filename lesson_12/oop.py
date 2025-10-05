import json

# data1.txt
q = {"Country": "Turkey", "avg_temp": 30}
# data2.txt
w = {"Country": "Greece", "avg_temp": 28}
# data3.txt
e = {"Country": "Poland", "avg_temp": 15, "min_temp": 2}

def read_file1(filename):
    file_data = open(filename, 'r')
    # data = file_data.read()
    data = json.load(file_data) # Преобразование из json в питоновский список
    print(data)
    file_data.close()
    return data

data1 = read_file1("data1.txt")
data2 = read_file1("data2.txt")
print()

print(data1['Country'])
print(data1['avg_temp'])
print(data2['Country'])
print(data2['avg_temp'])
print()


class CountryData:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()
        self.country = self.data['Country']
        self.avg_temp = self.data['avg_temp']
        self.comfort = self.is_comfort()

    # @property
    # def data(self):
    #     return self.__data
    #
    # @property
    # def country(self):
    #     return self.__country
    # @property
    # def avg_temp(self):
    #     return self.__avg_temp
    # @property
    # def comfort(self):
    #     return self._comfort
    # @comfort.setter
    # def comfort(self, value):
    #     self._comfort = value

    def read_file(self):
        file_data = open(self.filename, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

    def is_comfort(self):
        return self.avg_temp > 25

class CountryDataWithMinTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']


data1 = CountryData('data1.txt')
data1.comfort = False
print(data1.comfort)
print(data1.data)
print(data1.country)
print(data1.avg_temp)
data2 = CountryData('data2.txt')
print(data2.data)
print(data2.country)
print(data2.avg_temp)
print(data1.comfort)
print(data2.comfort)
print()
data3 = CountryDataWithMinTemp('data3.txt')
print(data3.avg_temp)
print(data3.min_temp)
print()
print(data1.data)