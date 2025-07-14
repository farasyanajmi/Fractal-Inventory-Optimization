import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def input_data(n):  # Method
    data_x = []
    data_y = []
    for i in range(n):
        x_value = float(input(f"Masukkan nilai x{i + 3} : "))
        y_value = float(input(f"Masukkan nilai y{i + 3} : "))
        data_x.append(x_value)
        data_y.append(y_value)
    return data_x, data_y


def sort_data(x, y):
    x_copy = x.copy()
    x_copy.sort()
    y_copy = [y[x.index(x_data)] for x_data in x_copy]
    return [x_copy, y_copy]


def data_extern(path):
    data = pd.read_excel(f"{path}.xlsx")
    price_list = data["Price"].to_list()
    demand_list = data["Demand"].to_list()
    return [price_list, demand_list]


def x_data_and_y_data(x_pure, y_pure, x, y):
    x_pure_copy = x_pure.copy()
    y_pure_copy = y_pure.copy()
    x_pure_copy.extend(x)
    y_pure_copy.extend(y)
    return x_pure_copy, y_pure_copy


class Module:
    def __init__(self):
        self.color = "red"  # Property
        pass

    def generate_y_data(self, value, x, y):
        global y_minimum, y_maximum
        x_sort = x.copy()
        x_sort.sort()

        for i in range(len(x_sort)):
            if value < x_sort[i]:
                y_maximum = x_sort[i]
                break

        for j in range(len(x_sort) - 1, -1, -1):
            if value > x_sort[j]:
                y_minimum = x_sort[j]
                break

        x_minimum_index = x.index(y_minimum)
        x_maximum_index = x.index(y_maximum)

        y_range = [y[x_minimum_index], y[x_maximum_index]]

        return random.randint(int(min(y_range)), int(max(y_range))) + (random.randint(0, 9) / 10)

    def generate_data(self, x, y, n):
        x_data = x.copy()
        x_data_2 = x.copy()
        y_data = y.copy()
        minimum = x_data[0]
        maximum = x_data[1]
        mean = x_data[2]
        pilihan = x_data[3]
        x_dummy = 0
        x_generate = []
        y_generate = []

        while not (maximum > x_dummy > minimum):
            x_generate = [random.randint(int(minimum), int(maximum)) + (random.randint(0, 9) / 10) for _ in
                          range(n - 5)]
            x_dummy = round((mean * n) - (sum(x_generate) + minimum + maximum + mean + pilihan), 1)

        x_generate.append(x_dummy)
        x_data.extend(x_generate)

        for x in range(4, len(x_data)):
            y_generate.append(self.generate_y_data(x_data[x], x_data_2, y_data))

        y_data.extend(y_generate)

        return x_data, x_generate, y_data, y_generate

    def a_and_e_value(self, x, x_min, x_max):
        a_list = []
        e_list = []

        for i in range(len(x) - 1):
            a = (x[i + 1] - x[i]) / (x_max - x_min)
            e = (x_max * x[i] - x_min * x[i + 1]) / (x_max - x_min)
            a_list.append(a)
            e_list.append(e)

        return a_list, e_list

    def create_fungsi(self):
        print("Buat fungsi dengan inputan a, b, c, d (ax^d+bx+c | ay^d+by+c : ")
        f = []
        # a = int(input("Masukkan nilai a : "))
        # d = int(input("Masukkan nilai d : "))
        # b = int(input("Masukkan nilai b : "))
        # c = int(input("Masukkan nilai c : "))
        f.extend([1, 1.1, -1, -10000])
        return f

    def g_y_x(self, g_h, x, y):
        [a, d, b, c] = g_h
        x_h = [(a * (x_i ** d)) + (b * x_i) + c for x_i in x]
        y_h = [(a * (y_i ** d)) + (b * y_i) + c for y_i in y]
        return [[x_h[0], x_h[3]], [y_h[0], y_h[3]]]

    def c_and_f_value(self, x, y, d, x_g, y_g):
        c_list = []
        f_list = []

        for i in range(len(x) - 1):
            y1 = y[x.index(x[i + 1])]
            y0 = y[x.index(x[i])]
            # print(f"x1 {x_sort[i+1]}, x0 {x_sort[i]}, y1 {y1}, y0 {y0}")
            c_value = ((y1 - y0) / (x_g[1] - x_g[0])) - (d * ((y_g[1] - y_g[0]) / (x_g[1] - x_g[0])))
            f_value = (((x_g[1] * y0) - (x_g[0] * y1)) / (x_g[1] - x_g[0])) - (
                    d * (((x_g[1] * y_g[0]) - (x_g[0] * y_g[1])) / (x_g[1] - x_g[0])))
            c_list.append(c_value)
            f_list.append(f_value)

        return c_list, f_list

    def matrix1(self, a_list, c_list, d_value):
        matrix_list = []
        n = len(a_list)
        for i in range(n):
            matrix_list.append(np.array([[a_list[i], 0], [c_list[i], d_value]]))
        return matrix_list

    def matrix2(self, e_list, f_list):
        matrix_list = []
        n = len(e_list)
        for i in range(n):
            matrix_list.append(np.array([e_list[i], f_list[i]]).reshape((2, 1)))
        return matrix_list

    def matrix3(self, x, x_gen, y_gen):
        global x_minimum, x_maximum, num
        x_sort = x.copy()
        # x_sort.sort()

        matrix_list = []
        num_list = []
        n = len(x_gen)
        for i in range(n):
            matrix_list.append(np.array([x_gen[i], y_gen[i]]).reshape((2, 1)))

            for j in range(len(x_sort)):
                if x_gen[i] < x_sort[j]:
                    x_maximum = x_sort[j]
                    break

            for k in range(len(x_sort) - 1, -1, -1):
                if x_gen[i] > x_sort[k]:
                    x_minimum = x_sort[k]
                    break

            num = 0

            x_minimum_index = x_sort.index(x_minimum)
            x_maximum_index = x_sort.index(x_maximum)

            if (x_minimum_index == 0 and x_maximum_index == 1):
                num = 0
            elif (x_minimum_index == 1 and x_maximum_index == 2):
                num = 1
            elif (x_minimum_index == 2 and x_maximum_index == 3):
                num = 2

            num_list.append(num)

        return matrix_list, num_list

    def matrix_result(self, m1, m2, m3, num):
        n = len(m3)
        matrix_result = []

        for i in range(n):
            result = m1[num[i]].dot(m3[i]) + m2[num[i]]
            matrix_result.append(result)

        return matrix_result

    def tampil_grafik(self, x, y, y_result):
        x_copy = x.copy()
        x_copy.sort()
        y_copy = [y[x.index(x_copy[i])] for i in range(len(x_copy))]
        y_result_copy = [y_result[x.index(x_copy[i])] for i in range(len(x_copy))]
        plt.plot(x_copy, y_copy)
        plt.plot(x_copy, y_result_copy)
        plt.legend(["y data", "y result"], loc="best")
        plt.show()

    def mape(self, y, result):
        return [abs((y[i] - result[i]) / y[i]) * 100 for i in range(len(y))]

    def gi_and_hi_value(self, x, y, x_excel, y_excel):

        pass
