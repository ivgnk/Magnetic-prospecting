# Calculation of the magnetic field of the ball on the profile
# Расчет магнитного поля шара на профиле
# Calculation of the magnetic field of the ball on the profile

# Параметры исходного шара
# h - глубина центра шара в метрах
# r - радиус шара в метрах
# j - намагниченность в А/м
import math
import copy
import numpy as np
import matplotlib.pyplot as plt

h: float = 50.0
r: float = 25.0
j: float = 0.5

coo: list = []
for i in range(-250,255,5):
    coo = coo + [i]

m:float = (4/3)*j*math.pi*(r**3)
h2 = h**2;   h22 = 2*h2

z_sgs: list =[]   #готовим пустой список элементов для верт.составл.
h_sgs : list =[]  #готовим пустой список элементов длягориз.составл.

for x in coo:
    x2:float = x**2
    bottom:float = (h2+x2)**2.5
    z_sgs = z_sgs + [m*(h22-x2)/bottom]
    h_sgs = h_sgs + [-3*m*h*x/bottom]

z_si = copy.deepcopy(z_sgs) #Делаем полную копию списка для вертикальной составляющей
h_si = copy.deepcopy(h_sgs) # Делаем полную копию списка для горизонтальной составляющей

numel:int = len(z_sgs) #определяем число элементов списка
coeff :float = math.pow(10,-7)/(4*math.pi)
coeff  = coeff*math.pow(10,9)
i:int = 0 #счетчик
while i < numel:
    z_si[i] = z_sgs[i]*coeff
    h_si[i] = h_sgs[i]*coeff
    i = i + 1

### --- Второе занятие с заочниками
## -- Часть 1 - Вычисление полного вектора и построенние графиков
t_si = copy.deepcopy(h_sgs) # Делаем полную копию списка для полного вектора
for i in range(numel):
    t_si[i]= math.hypot(z_si[i], h_si[i])
    print(i, coo[i], z_si[i], h_si[i], t_si[i])


# Построение графиков
plt.plot(coo, z_si,  label = 'Верт.компонента')
plt.plot(coo, h_si,  label = 'Гориз.компонента')
plt.plot(coo, t_si,  label = 'Полный вектор')
plt.title('Магнитное поле шара', alpha=1, color='r', fontsize=18, fontstyle='italic', fontweight='bold')
plt.legend(loc='upper right') # положение легенды в верхнем правом углу
plt.grid()      # включение отображение сетки
plt.xlabel('x, м') # название оси абсцисс
plt.ylabel('Магнитное поле, нТл') # название оси ординат
plt.show() # показываем график

## -- Часть 2 - Вычисление нескольких вариантов полей и построенние их графиков
# Варьируем
# h - глубина центра шара в метрах
# r - радиус шара в метрах
# j - намагниченность в А/м

hi = [50.0, 100, 150, 200]
ri = [10.0, 20.0]
ji = [0.250, 0.500]


plt.figure(figsize=(18, 12)) # x и y – ширина и высота рис. в  дюймах

colors = ['red','cyan', 'green','magenta']
for i in range(len(hi)):
    plt.subplot(2, 2, i+1)  # 2 - количество строк; 1 - количество столбцов; 1 - индекс ячейки в которой работаем
    plt.title('Магнитное поле шара для глубины '+str(hi[i])+', м', alpha=1, color='b', fontsize=10, fontstyle='italic', fontweight='bold')
    print('i=',i)
    for k in range(len(ri)):
        # print('k=', k)
        for l in range(len(ji)):
            # print('l=', l)
            m:float = (4/3)*ji[l]*math.pi*(ri[k]**3)
            h2 = hi[i]**2;   h22 = 2*h2
            for n in range(numel):
                # print('n=', n)
                x2 = coo[n]**2
                bottom = (h2 + x2)**2.5
                z_sgs[n] = m * (h22 - x2) / bottom
                h_sgs[n] = (-3 * m * h * coo[n]) / bottom
                z_si[n] = z_sgs[n]*coeff
                h_si[n] = h_sgs[n]*coeff
                t_si[n]= math.hypot(z_si[n], h_si[n])

            plt.plot(coo, z_si,  label = 'Верт., r='+str(ri[k])+',м  j='+str(ji[l])+' А/м')
            plt.plot(coo, h_si,  label = 'Гориз., r='+str(ri[k])+',м  j='+str(ji[l])+' А/м')
            plt.plot(coo, t_si,  label = 'Полный, r='+str(ri[k])+',м  j='+str(ji[l])+' А/м \n')
    plt.legend(loc='upper right', fontsize=7) # положение легенды в верхнем правом углу
    plt.grid()  # включение отображение сетки
plt.show() # показываем график
print('Нормальное завершение')
