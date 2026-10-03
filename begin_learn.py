import numpy as np

def guess_number():
    """
    Генерирует случайное число от 1 до 10 и предполагает, что пользователь угадал его.
    """
    try_items = 100000
    catch_items = 0
    for i in range(try_items):
        guess = np.random.randint(1, 10)
        predict = np.random.randint(1, 10)
        catch_items += 1 if guess == predict else 0
    print(catch_items / try_items)

guess_number()