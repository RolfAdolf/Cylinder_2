import numpy as np

#функция среднего линейного отклонения
def linear(x):
    m = np.mean(x)
    return sum([abs(x[i] - m) for i in range(len(x))]) / len(x)


###JADE - алгоритм минимизации

# f - исследуемая функция
# N - количество векторов в популяции
# n - размерность векторов
# G - количество итераций
# a, b - границы для выбора компонент вектора
# p_best - доля лучших векторов в популяции
def JADE(f, N=20, n=3, G=100, a = -10000, b = 10000, p_best = 0.3, c = 0.5, max = False):
    
    if (max):
        m=-1
    else:
        m=1
    # Генерируем начальную популяцию
    X = []
    for i in range(N):
        X.append([(b-a)*(j-0.5) + (b+a)/2 for j in np.random.random(n)])
    
    #Сортируем X по значениям
    Y = [m*f(x) for x in X]
    ind = np.argsort(Y)
    X = [X[t] for t in ind]
    Y = [Y[t] for t in ind]

    # Архив исключенных родителей
    A = []

    # Инициализируем начальные средние значения для вероятности и силы мутации
    p_mean = 0.5
    F_mean = 0.5

    
    for g in range(G):

        # Массивы удачных параметров
        S_p = []            # Успешные вероятности
        S_F = []            # Успешные силы мутации
        
        
        for i in range(N):
            # Найдем значения вероятности и силы мутации
            # для данного вектора при заданных средних
            # значениях вероятности и силы мутации
            p = np.random.normal(p_mean, 0.1)
            F = np.random.normal(F_mean, 0.1)

            #Создадим X_A
            X_A = X + A
            #Выберем индексы предков
            j_best = np.random.randint(round(N * p_best))
            j1 = j_best
            while (j_best == j1):
                j1 = np.random.randint(len(X))
            
            j2 = j1
            while ((j_best == j2) or (j1 == j2)):
                j2 = np.random.randint(len(X_A))
            
            x_best = X[j_best]
            x1 = X[j1]
            x2 = X_A[j2]

            # Создаем мутантный вектор
            v = [x + F * (x_b - x) - F * (x_1 - x_2) for x, x_b, x_1, x_2 in zip(X[i], x_best, x1, x2)]

            # Скрещиваем вектор из популяции с мутантным
            for j in range(n):
                if (np.random.random() <= p):
                    v[j] = X[i][j]
                    
            # Архивируем родительский вектор, если пробный вектор оказался лучше
            # Добавляем значения вероятности и силы мутации в созданные ранее
            # массивы успешных вероятностей и сил мутации
            Y_v = m*f(v)
            if (m*f(X[i]) > Y_v):
                A.append(X[i])
                for j in range(i+1):
                    if (Y[j] > Y_v):
                        del Y[i]
                        del X[i]
                        X.insert(j, v)
                        Y.insert(j, Y_v)
                        break
                S_p.append(p)
                S_F.append(F)
        
        # Если родительский вектор оказался лучше пробного,
        # то обновляем значения вероятности и силы мутации
        if (len(S_p) > 0) and (len(S_F) > 0):
            p = (1 - c) * p + np.mean(S_p)
            F = (1 - c) * F + linear(S_F)
            # F = (1 - c) * F + np.mean(S_F)
        
        # Удаляем рандомные векторы из архива исключенных 
        # родительских векторов, если размер архива превышает 
        # количество векторов в популяции
        while (len(A) > N):
            del A[np.random.randint(len(A))]
    
    L = [m*f(j) for j in X]
    x_ = X[np.argmin(L)]
    return [m*np.min(L), x_]
