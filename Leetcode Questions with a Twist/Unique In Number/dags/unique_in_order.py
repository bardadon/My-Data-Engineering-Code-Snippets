from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from datetime import datetime


default_args = {
    'start_date': datetime(2022,1,1),
    'schedule_interval': '0 * * * *'
}


with DAG(dag_id='unique_in_order', default_args=default_args,  catchup=False) as dag:
    
    # Dag #1 - Load input data to MySQL
    create_table_mysql = MySqlOperator(
        task_id = 'create_table_mysql',
        mysql_conn_id = 'mysql',
        sql = "mysql_scripts/create_table.sql"
    )

    # Dag #2 - Insert Data
    insert_data_mysql = MySqlOperator(
        task_id = 'insert_data_mysql',
        mysql_conn_id='mysql',
        database='codeWars',
        sql = "mysql_scripts/insert_data.sql"
    )

    # DAG #3 - Extract Data to airflow-worker
    extract_data_mysql = BashOperator(
        task_id = 'extract_data_mysql',

        # 1. Connect to Mysql and export the table nums
        # 2. Remove headers
        bash_command= '''
        mysql -h 172.21.0.10 -u root --password=root codeWars -e "SELECT * FROM nums" > /tmp/unique_in_order.csv;
        sed -i 1d /tmp/unique_in_order.csv; 
        '''
    )
    
    # Dag #4 - Solving the problem in Bash using the CSV file from airflow-worker
    bash_solution = BashOperator(
        task_id = 'bash_solution',
        bash_command="bash_scripts/bash_solution.sh"
    )

    # Dependencies
    create_table_mysql >> insert_data_mysql >> extract_data_mysql >> bash_solution

