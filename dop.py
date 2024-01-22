# import numpy as np
# import matplotlib.pyplot as plt
#
# # Определение диапазона координат
# x_range = np.linspace(-5, 5, 100)
# y_range = np.linspace(-5, 5, 100)
#
# # Создание сетки точек
# x, y = np.meshgrid(x_range, y_range)
#
# # Вычисление значения функции (i - z) / (i + z)
# z_values = x + 1j * y
# n_values = (1j - z_values) / (1j + z_values)
#
# # Построение карты цветов
# plt.figure()
# scatter_plot = plt.scatter(x.flatten(), y.flatten(), c=np.abs(n_values.flatten()), cmap='jet', s=30, edgecolors='none')
# plt.colorbar(scatter_plot)
#
# # Установка ограничений для цветовой шкалы
# plt.clim(0, 2)
#
# # Ограничение осей для лучшего отображения
# plt.axis([-5, 5, -5, 5])
#
# # Отображение сетки
# plt.grid(True)
#
# # Сохранение графика в файл
# plt.savefig('refractive_index_profile_custom_function.png')
#
# # Отображение графика
# plt.show()
#

import numpy as np
import matplotlib.pyplot as plt
import scipy.io

# Определение диапазона координат
x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)

# Создание сетки точек
x, y = np.meshgrid(x_range, y_range)

# Вычисление значения функции (i - z) / (i + z)
z_values = x + 1j * y
n_values = (1j - z_values) / (1j + z_values)

# Создание карты цветов
plt.figure()
scatter_plot = plt.scatter(x.flatten(), y.flatten(), c=np.abs(n_values.flatten()), cmap='jet', s=30, edgecolors='none')
plt.colorbar(scatter_plot)

# Установка ограничений для цветовой шкалы
plt.clim(0, 2)

# Ограничение осей для лучшего отображения
plt.axis([-5, 5, -5, 5])

# Отображение сетки
plt.grid(True)

# Сохранение данных
x_data = x.flatten()
y_data = y.flatten()
n_data = np.abs(n_values.flatten())

data_dict = {'x_data': x_data, 'y_data': y_data, 'n_data': n_data}
scipy.io.savemat('data.mat', data_dict)

# Сохранение карты цветов в файл
plt.savefig('color_map.png')

# Отображение графика
plt.show()
