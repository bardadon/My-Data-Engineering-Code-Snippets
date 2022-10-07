## Prerequisites for using PostgreSQL

Run:

```docker
docker-compose up -d
```

- Log into [localhost](http://localhost):5050. Add a new server, use the credentials:
    - Username = root
    - Password = root
- Grab the ip address of the postgres container by using:
    
    ```python
    docker inspect <ContainerId>
    ```
    

And now we have our own PostgreSQL database.

![Untitled(41)](https://user-images.githubusercontent.com/65648983/194544904-090a6459-c95f-460e-9cae-e55b2d5e1e1c.png)
