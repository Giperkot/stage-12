import random;
import matplotlib.pyplot as plt

nums = [];
values = [];

tryCount = 500000;
i = 2;
while (i < 21):
    j = 0;
    deathRate = 0;
    while (j < tryCount):
        position = -2;
        k = 0;
        while (k < i):
            number = random.randint(1, 3);
            if (number == 1):
                position = position + 1;
            else:
                position = position - 1;

            if (position >= 0):
                deathRate = deathRate + 1;
                break;
            k = k + 1;

        j = j + 1;

    nums.append(i);
    values.append(deathRate / tryCount);

    i = i + 2;

plt.plot(nums, values);
plt.show()

print (nums);
print (values);
