from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from datetime import datetime
import subprocess
import logging


default_args = {
    'start_date': datetime(2022, 1, 1),
    'schedule_interval' : None
}

# Extract data from Postgres and export as csv file to airflow-worker
def _extract_data_python(copy_sql):
    hook = PostgresHook(postgres_conn_id = 'postgres')
    logging.info('Exporting query to file')
    hook.copy_expert(copy_sql, filename='/tmp/majorityelement.csv'
    )

# Read csv file from airflow-worker
# Solve problem and export solution back to airflow-worker
def _solve_problem_python():
    import pandas as pd

    # Read Data
    df = pd.read_csv('/tmp/majorityelement.csv')
    nums = df.nums.to_list()

    # Run Solution
    def majorityElement(nums):
    
        count_dict = dict()
        
        # Count appearances in a dictionary
        for i in nums:

            count_dict[i] = count_dict.get(i,0) + 1
            
        # Grab the key that belongs to the max value
        for key, value in count_dict.items():

            if value == max(count_dict.values()):
                return key

    solution = majorityElement(nums)

    # Export Solution to airflow-worker
    df = pd.DataFrame([solution], columns=['nums'])
    df.to_csv('/tmp/python_solution.csv', header=None, index=None)




with DAG('majorityElement', default_args=default_args, catchup=False ) as dag:

    # DAG #1 - Create Postgres table
    create_table_postgres = PostgresOperator(
        task_id = 'create_table_postgres',
        postgres_conn_id='postgres',
        sql='''
        
        drop table if exists majorityelement;

        create table majorityelement(
            nums int not null
        );        
        '''
    )

    # DAG #2 - Insert Data Postgres
    insert_data_postgres = PostgresOperator(
        task_id = 'insert_data_postgres',
        postgres_conn_id='postgres',
        sql='''
        insert into majorityelement
        (nums)
        values
        (3),
        (2),
        (3);
        '''
    )

    # DAG #3 - Solve Problem Postgres
    solve_problem_postgres = PostgresOperator(
        task_id = 'solve_problem_postgres',
        postgres_conn_id='postgres',
        sql='''
        drop table if exists majorityelement_solution;
        create table majorityelement_solution as
        select nums
        from majorityelement
        group by nums
        order by count(*) desc
        limit 1;
        '''
    )

    # DAG #4 - Extract Solution Postgres
    extract_solution_postgres = PostgresOperator(
        task_id = 'extract_solution_postgres',
        postgres_conn_id='postgres',
        sql='''
        COPY majorityelement_solution(nums)
        TO '/tmp/postgres_solution.csv' 
        DELIMITER ',' 
        CSV;
        '''
    )


    # DAG #5 - Create MySQL table
    create_table_mysql = MySqlOperator(
        task_id = 'create_table_mysql',
        mysql_conn_id='mysql',
        sql='''
        create database if not exists airflow;

        use airflow;

        drop table if exists majorityelement;

        create table majorityelement(
            nums int not null
        );        
        '''
    )

    # DAG #6 - Insert Data MySQL
    insert_data_mysql = MySqlOperator(
        task_id = 'insert_data_mysql',
        mysql_conn_id='mysql',
        sql='''
        insert into majorityelement
        (nums)
        values
        (3),
        (2),
        (3);     
        '''
    )

    # DAG #7 - Solve Problem MySQL
    solve_problem_mysql = MySqlOperator(
        task_id = 'solve_problem_mysql',
        mysql_conn_id='mysql',
        sql='''
        drop table if exists majorityelement_solution;
        create table majorityelement_solution as
        select nums
        from majorityelement
        group by nums
        order by count(*) desc
        limit 1;
        '''
    )

    # DAG #8 - Extract Solution MySQL
    extract_solution_mysql = BashOperator(
        task_id = 'extract_solution_mysql',

        # 1. Connect to Mysql and output the table majorityelement_solution
        # 2. Remove headers
        bash_command= '''
        mysql -h 192.168.176.4 -u root --password=root airflow -e "SELECT * FROM majorityelement_solution" > /tmp/mysql_solution.csv;
        sed -i 1d /tmp/mysql_solution.csv; 
        '''
    )

    # DAG #9 - Extract Data python
    extract_data_python = PythonOperator(
        task_id = 'extract_data_python',
        python_callable=_extract_data_python,
        op_kwargs={
        "copy_sql": "COPY (SELECT * FROM majorityelement) TO STDOUT WITH CSV HEADER"
        }
    )

    # DAG #10 - Solve Problem Python
    solve_problem_python = PythonOperator(
        task_id = 'solve_problem_python',
        python_callable=_solve_problem_python
    )


    # Dependencies
    create_table_postgres >> insert_data_postgres >> solve_problem_postgres >> extract_solution_postgres
    create_table_mysql >> insert_data_mysql >> solve_problem_mysql >> extract_solution_mysql
    
    insert_data_postgres >> extract_data_python >> solve_problem_python
