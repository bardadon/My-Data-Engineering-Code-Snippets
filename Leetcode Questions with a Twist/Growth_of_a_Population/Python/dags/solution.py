import sys


def nb_year(p0, percent, aug, p):
    
    current_population = p0
    years = 0

    while current_population < p:
        
        population_increase = round(current_population * (percent/100) + aug)
        current_population += population_increase 
        years += 1

    return years



if __name__ == '__main__':
    #number_of_years = nb_year(p0 = 1000, percent=5, aug=50, p=1000)
    #sys.path.append('/projects/CodeWares_Project/Growth_of_a_Population/solution.py')
    print(sys.path)