import random

def _01_sale_volume():
    day_sales = []
    total_volume = 0
    counter = 0
    for day in range(1,8,1):
        print("Enter sales volume for day ", day)
        day_sales.append(int(input()))
        day_sales_idx = day_sales.index(day_sales[counter])
        total_volume += int(day_sales[day_sales_idx])
        counter += 1
    print("list ", day_sales)
    print("Total is ", total_volume)


def _02_lottery_generator():
    lottery_list = []
    for el in range(0, 7):
        lottery_list.append(random.randint(0, 9))
    for list_el in range(len(lottery_list)):
        print(lottery_list[list_el])


def _03_rain_stat():
    rain_stat = []
    total_year = 0
    index = 0
    max_rain_month = []
    min_rain_month = []
    for month in range(1, 13):  # to modify to 0,12 for optimization
        print("Enter sales volume for month ", month)
        rain_stat.append(int(input())) # adding number from key
        month_idx = rain_stat.index(rain_stat[index])
        total_year += int(rain_stat[month_idx])
        # highest amount
        if rain_stat[index] == max(rain_stat):
            max_rain_month = rain_stat[index]
        # lowest amount
        if rain_stat[index] == min(rain_stat):
            min_rain_month = rain_stat[index]
        index += 1
    print("total ", total_year)
    print("avg ", total_year/len(rain_stat))
    print("max ", max_rain_month)
    print("min", min_rain_month)
    print(rain_stat)


if __name__ == "__main__":
    _03_rain_stat()
