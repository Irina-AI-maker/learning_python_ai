import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем тензор (высота 100, ширина 100, 3 цвета RGB)
# Числа от 0 до 255 (стандарт для цвета)
image_tensor = np.random.randint(0, 256, (100, 100, 3))
red_only = image_tensor.copy()
red_only[:, :, 1:] = 0 

# 2. Команда "покажи этот тензор как картинку"
plt.imshow(red_only)
plt.axis('off') # Убираем оси координат, чтобы было красиво
plt.show()