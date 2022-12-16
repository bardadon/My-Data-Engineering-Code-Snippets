from airflow.decorators import task, dag

from solution import nb_year
from datetime import datetime

default_args = {
    'start_date':datetime(2022,1,1),
    'schedule_interval':'0 0 * * *'
}


@dag(
    dag_id = 'growth_of_population',
    default_args = default_args,
    catchup = False
)

def growth_of_population():
    
    # Dag #1 - Solution in Python
    @task
    def dag1_nb_year(p0, percent, aug, p):
        number_of_years = nb_year(p0, percent, aug, p)

        with open('/tmp/solution.txt', 'w') as write_file:
            write_file.write(str(number_of_years))
            
        return number_of_years

    # Workflow
    dag1_nb_year(1500000, 0.25, 1000, 2000000)
    


# Instantiating the DAG
growth_of_population = growth_of_population()


if __name__ == '__main__':
    number_of_years = nb_year(1500000, 0.25, 1000, 2000000)
    print(number_of_years)