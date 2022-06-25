import numpy as np
import pygad
import Nonogramy


print("genetyczny")

l_kolumn,l_wierszy=Nonogramy.Panda.wielkosc()
kratki_kol, kratki_wier, bloki_kol, bloki_wier=Nonogramy.Panda.nonogram()

### Genetic algorithm

gene_space=[0,1]

def fitness_func(solution, solution_idx):
    
    #tworzymy macierz (plansze zamalowanych kratek)
    l=np.copy(solution)
    M = []
    while l.size > 0:
      M.append(l[:(l_kolumn)])
      l = l[(l_kolumn):]
    M=np.array(M)
    
    zamblK=[]
    zamblW=[]
    zamKrK=[]
    zamKrW=[]

    for i in range(l_kolumn):
        zam=False
        bl=0
        kr=0
        for j in range(l_wierszy):
            if M[i,j]==1:
                kr=kr+1
                zam=True
                if j==l_wierszy-1:
                    bl=bl+1
            elif zam==True:
                bl=bl+1
                zam=False
        zamblW.append(bl)
        zamKrW.append(kr)       
    for i in range(l_wierszy):
        zam=False
        bl=0
        kr=0
        for j in range(l_kolumn):
            if M[j,i]==1:
                kr=kr+1 
                zam=True
                if j==l_kolumn-1:
                    bl=bl+1
            elif zam==True:
                bl=bl+1
                zam=False
        zamblK.append(bl)
        zamKrK.append(kr)

    suma=0
    for i in range(l_kolumn):
        suma=suma-np.abs(zamblK[i]-bloki_kol[i])- np.abs(zamKrK[i]-kratki_kol[i])
    
    for i in range(l_wierszy):
        suma=suma-np.abs(zamblW[i]-bloki_wier[i])- np.abs(zamKrW[i]-kratki_wier[i])

    fitness = suma
    return fitness
fitness_function = fitness_func

sol_per_pop = 100
num_genes = l_kolumn*l_wierszy

num_parents_mating = int(sol_per_pop/2)
num_generations = 4000
keep_parents = 10

parent_selection_type = "rank"

crossover_type = "two_points"

mutation_type = "random"
mutation_percent_genes = 0.5




ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : \n{solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))


l=np.copy(solution)
M = []
while l.size > 0:
    M.append(l[:(l_kolumn)])
    l = l[(l_kolumn):]
M=np.array(M)


roz=''
for i in range(l_wierszy):
    w='|'
    for j in M[i]:
        if j==0:
            w=w+'  '
        else: w=w+'##'
    roz=roz+w+"|\n"
print(roz)


print("\n\n\n")

ga_instance.plot_fitness()

