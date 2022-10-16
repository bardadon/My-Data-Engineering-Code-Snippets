def rank_score():
    
    # Starting a session
    spark = SparkSession.builder.appName('Nth_Highest_Salary').getOrCreate()

    # loading the data
    df = spark.read.option('header', 'true').option('inferSchema', 'true')\
    .csv('scores.csv')

    df.createOrReplaceTempView('scores')

    query = '''
    select 
        aaa.score,
        aaa.rank
    from 
    (
        select 
            s1.id,
            s1.score,
            count(*) as rank
        from scores as s1, (select distinct score from scores) as s2
        where s1.score <= s2.score
        group by s1.id, s1.score
        order by s1.score desc
    ) aaa
    '''

    result = spark.sql(query)
    return result
  
result = rank_score()
result.show()
