import random
import matplotlib.pyplot as plt
import numpy as np

# Функція для симуляції кидання двох кубиків
def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: (value / num_rolls) * 100 for key, value in results.items()}
    return results, probabilities

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Симуляція
num_rolls = 100000
simulated_results, simulated_probabilities = simulate_dice_rolls(num_rolls)

# Таблиця результатів
print("Сума\tІмовірність (Метод Монте-Карло)\tАналітична ймовірність")
for total in range(2, 13):
    print(f"{total}\t{simulated_probabilities[total]:.2f}%\t\t\t{analytical_probabilities[total]}%")

# Побудова графіка
x = np.arange(2, 13)
simulated = [simulated_probabilities[i] for i in x]
analytical = [analytical_probabilities[i] for i in x]

plt.bar(x - 0.2, simulated, width=0.4, label='Метод Монте-Карло', color='skyblue')
plt.bar(x + 0.2, analytical, width=0.4, label='Аналітичні ймовірності', color='orange')

plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Імовірність (%)')
plt.title('Порівняння ймовірностей сум для двох кубиків')
plt.xticks(x)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
