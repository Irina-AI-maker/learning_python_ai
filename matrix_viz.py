import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем сетку точек (наше пространство)
x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
points = np.vstack([x.flatten(), y.flatten()])

# 2. Определяем матрицу трансформации (например, сдвиг)
# Попробуйте поменять числа: [1, 2], [0, 1] — это растяжение и наклон
matrix = np.array([[2, 10], 
                   [0, 1]])

# 3. Применяем линейную алгебру: умножаем матрицу на все точки сразу
transformed_points = matrix @ points

# 4. Визуализация
plt.figure(figsize=(8, 8))
plt.scatter(points[0], points[1], color='gray', alpha=0.3, label='До (Original)')
plt.scatter(transformed_points[0], transformed_points[1], color='blue', label='После (Transformed)')

# Рисуем стрелки векторов для наглядности
plt.quiver(0, 0, matrix[0,0], matrix[1,0], color='red', angles='xy', scale_units='xy', scale=1, label='Вектор i')
plt.quiver(0, 0, matrix[0,1], matrix[1,1], color='green', angles='xy', scale_units='xy', scale=1, label='Вектор j')

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.grid(True, linestyle='--')
plt.legend()
plt.title("Визуализация линейной трансформации")
plt.show()