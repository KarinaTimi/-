#Подключение библиотек
import os
import numpy as np
import matplotlib.pyplot as plt
import math
#Автоматическое определение пути к файлу в папке, в которой находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Переменные для расчета.txt')
#Проверка наличия файла
if not os.path.exists(file_path):
    print(f"Ошибка: Файл '{file_path}' не найден!")
    print("Убедитесь, что файл находится в той же папке, что и скрипт")
    exit()
#Чтение параметров из файла
params = {}
with open(file_path, 'r') as file: 
    for line in file:
        if line.strip():
            name, value = line.split()
            params[name] = float(value)
            print(f"{name} = {params[name]}")
#Создание временного массива и хранение значений дебита для каждого момента времени 
t = np.linspace(params['time_min'], params['time_max'], int(params['num_points']))
Q = [] 
#Расчет формулы Дюпюи
for time in t:
    K, h, P_i, P_wf = params['K'], params['h'], params['P_i'], params['P_wf']
    mu, B, m, C_t, r_w = params['mu_o'], params['B_o'], params['m'], params['C_t'], params['r_w']

    debit = (K * h * (P_i - P_wf)) / ((18.41 * mu * B) * math.log((K * time) / (m * mu * C_t * (r_w**2))))
    Q.append(debit)
#Построение и сохранение графика дебита от времени в эту же папку
plt.figure(figsize=(10, 5))
plt.plot(t, Q, 'blue', linewidth=2)
plt.xlabel('Время, часы')
plt.ylabel('Дебит, м³/сутки')
plt.title('Зависимость дебита от времени')
plt.grid(True)
output_path = os.path.join(script_dir, 'Дебит.png')
plt.savefig(output_path)
print(f"График сохранен как '{output_path}'")
plt.show()