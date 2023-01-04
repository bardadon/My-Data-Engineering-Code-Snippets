select 
    e.job
from emp as e
order by SUBSTRING(job, length(job) - 2, length(job));