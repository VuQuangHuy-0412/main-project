from main_app.service import TeacherService, GroupTeacherService
import os
import time
import random

def genetic_algorithm(data, PopulationSize, population, objective, NumOfCross, NumLoop):
    population = init(data, PopulationSize, population)

    for i in range(0, NumLoop):
        objective = evaluate(data, PopulationSize, population, objective)
        print_result(data, PopulationSize, population, objective)
        population = selection(PopulationSize, population, objective)
        population = crossover(data, PopulationSize, NumOfCross, population)
        population = mutation(data, PopulationSize, population)

def init(data, PopulationSize, population):
    NumOfTeachers = data['num_of_teachers']
    NumOfClassCode = data['num_of_classes']

    for ind in range(0, PopulationSize):
        A = dict()
        for j in range(0, NumOfClassCode):
            ran = random.randint(0, NumOfTeachers - 1)
            for i in range(0, NumOfTeachers):
                if i == ran:
                    A[i, j] = 1
                else:
                    A[i, j] = 0
        population.append(A)
    return population
    

def objective_function(data, A):
    NumOfTeachers = data['num_of_teachers']
    NumOfClassCode = data['num_of_classes']
    Classes = data['classes']
    Teachers = data['teachers']

    obj = 0
    for i in range(0, NumOfTeachers):
        time_teaching = 0
        for j in range(0, NumOfClassCode):
            if A[i, j] == 1:
                time_teaching += Classes[j]['time_of_class']
        obj = max(obj, Teachers[i]['gd_time'] - time_teaching)
    return obj

def evaluate(data, PopulationSize, population, objective):
    NumOfTeachers, NumOfLanguages, NumOfProfessionalGroup, NumOfClassCode, NumOfSubjects = data['num_of_teachers'], data['num_of_classes'], data['num_of_groups'], data['num_of_classes'], data['num_of_subjects']
    Teachers = data['teachers']
    LanguageTeacherMapping = data['lt_mappings']
    GroupTeacherMapping = data['gt_mappings']
    Classes = data['classes']
    Subjects = data['subjects']
    Groups = data['group_teachers']
    Languages = data['languages']
    ClassConflict = data['class_conflicts']
    objective.clear()

    for ind in range(0, PopulationSize):
        A = population[ind]
        objective.append(objective_function(data, A))
        for j in range(0, NumOfClassCode):
            ct1 = 0
            for i in range(0, NumOfTeachers):
                if A[i, j] == 1:
                    for m in range(0, NumOfProfessionalGroup):
                        for s in range(0, NumOfLanguages):
                            for subject in range(0, NumOfSubjects):
                                subjectGroup = 0
                                subjectClass = 0
                                classLanguage = 0
                                if (Subjects[subject]['group_id'] == Groups[m]['id']):
                                    subjectGroup = 1
                                if (Classes[j]['subject_id'] == Subjects[subject]['id']):
                                    subjectClass = 1
                                if (Classes[j]['language_id'] == Languages[s]['id']):
                                    classLanguage = 1                            
                                ct1 += GroupTeacherMapping[i][m] * subjectClass * subjectGroup * LanguageTeacherMapping[i][s] * classLanguage
            if ct1 != 1:
                objective[ind] += 100000

            ct3 = 0
            for i in range(0, NumOfTeachers):
                if A[i, j] == 1:
                    ct3 += 1
            if ct3 != 1:
                objective[ind] += 100000
        
        for i in range(0, NumOfTeachers):
            ct2 = 0
            for j in range(0, NumOfClassCode):
                if A[i, j] == 1:
                    ct2 += Classes[j]['time_of_class']
            if ct2 > Teachers[i]['gd_time']:
                objective[ind] += 100000
            
            ct4 = 0
            for j in range(0, NumOfClassCode):
                if A[i, j] == 1:
                    ct4 += 1
            if ct4 < 1:
                objective[ind] += 100000
            
            for j in range(0, NumOfClassCode):
                if A[i, j] == 1:
                    for k in range(0, NumOfClassCode):
                        if ClassConflict[j][k] == 1 and A[i, k] == 1:
                            objective[ind] += 100000
    return objective

def selection(PopulationSize, population, objective):
    temp = objective.copy()
    temp.sort()
    limit_index = (int) (PopulationSize * 80 / 100)
    limit = temp[limit_index]
    
    for ind in range(0, PopulationSize):
        if objective[ind] > limit:
            population[ind] = population[random.randint(0, PopulationSize - 1)].copy()
    
    return population

def crossover(data, PopulationSize, NumOfCross, population):
    NumOfTeachers, NumOfClassCode = data['num_of_teachers'], data['num_of_classes']

    for ind in range(NumOfCross):
        father = random.randint(0, PopulationSize - 1)
        mother = random.randint(0, PopulationSize - 1)
        for j in range(0, NumOfClassCode):
            if random.randint(0, 1) == 1:
                for i1 in range(0, NumOfTeachers):
                    if population[father][i1, j] == 1:
                        population[mother][i1, j] = 1
                        population[father][i1, j] = 0
                for i2 in range(0, NumOfTeachers):
                    if population[mother][i2, j] == 1:
                        population[father][i1, j] = 1
                        population[mother][i1, j] = 0
    
    return population


def mutation(data, PopulationSize, population):
    NumOfTeachers, NumOfClassCode = data['num_of_teachers'], data['num_of_classes']
    
    index = random.randint(0, PopulationSize - 1)
    j1 = random.randint(0, NumOfClassCode - 1)
    new_list = [e for e in list(range(0, NumOfClassCode)) if e != j1]
    j2 = random.choice(new_list)
    i1 = 0
    i2 = 0
    for i in range(0, NumOfTeachers):
        if population[index][i, j1] == 1:
            i1 = i
    for ind in range(0, NumOfTeachers):
        if population[index][ind, j2] == 1:
            i2 = ind
    population[index][i1, j1] = 0
    population[index][i2, j1] = 1
    population[index][i2, j2] = 0
    population[index][i1, j2] = 1

    return population

def print_result(data, PopulationSize, population, objective):
    NumOfTeachers, NumOfClassCode = data['num_of_teachers'], data['num_of_classes']
    Classes = data['classes']
    Teachers = data['teachers']

    temp = objective.copy()
    temp.sort()
    best = temp[0]
    for i in range(0, PopulationSize):
        if (objective[i] == best):
            A = population[i]
            time = list()
            for i in range(0, NumOfTeachers):
                time.append(0)
                for j in range(0, NumOfClassCode):
                    if A[i, j] == 1:
                        print("Lớp %d -> GV %d\n"%(j, i))
                        time[i] += Classes[j]['time_of_class']
            print(time)
            maxTime = list()
            for i in range(0, NumOfTeachers):
                maxTime.append(Teachers[i]['gd_time'])
            break

