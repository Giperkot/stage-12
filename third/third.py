# Нормальное, быстрое решение задачи с графиком выживаемости.
# Идея состоит в том, чтобы построить дерево вероятностей.
# Каждачя следующая строчка рассчитывается из предудущей.

import matplotlib.pyplot as plt;

result = [];

leftShift = 1 / 3;
rightShift = 2 / 3;

# ввод количества шагов.
print("Введите количество шагов:");
n = int(input());

# Приседания с входными данными.
if (n < 2):
    print("Выживаемость - 1");
    exit(0)

if (n < 3):
    n = 3;

#Инициализация массивов.
prevLine = [ 0 for i in range(1, n + 1)];
nextLine = [ 0 for i in range(1, n + 1)];

prevLine[1] = leftShift;
prevLine[2] = rightShift;

# Заполнение массивов.
i = 1;
while (i < n):
    j = 0;
    while (j < len(prevLine) - 1):
        if (i % 2 == 0):
            if (j == 0):
                nextLine[j] = prevLine[j];
                j = j + 1;
                continue;

            if (j == 1):
                nextLine[j] = prevLine[j] * leftShift;
                j = j + 1;
                continue;

            nextLine[j] = prevLine[j - 1] * rightShift + prevLine[j] * leftShift;
        else:
            if (j == 0):
                nextLine[j] = prevLine[j + 1] * leftShift + prevLine[j];
                j = j + 1;
                continue;

            nextLine[j] = prevLine[j + 1] * leftShift + prevLine[j] * rightShift;

        j = j + 1;
    #print(nextLine);
    result.append(1 - nextLine[0]);
    prevLine = nextLine[:];

    i = i + 1;

# Вывод ответа.
print("Ответ:");
print("Выживаемость - ", result[len(result) - 1]);

x = [ i for i in range(0, len(result))]
plt.plot(x, result);
plt.show()