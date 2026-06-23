

## docker setup


### create new container with database
```bash
docker run --name gym
    -e MYSQL_ROOT_PASSWORD=secret
    -e MYSQL_DATABASE=gym_db
    -p 3306:3306
    -d mysql:latest
```

### Turn up container gym
```bash
docker start gym
```


## Folder Structure:

```
gym_management/
|
|--database/
|  |-- trainerDB.py
|  |-- traineeDB.py
|
|--routes/
|  |-- trainer_route.py
|  |-- trainee_route.py
|
|--logs/
|  |--logging_config.py
|  |--app.log
|
|-- main.py
|--.gitignore.py
|-- requirements.txt

```



## Tables Structure

### Table 'trainers'

```commandline
CREATE TABLE IF NOT EXISTS trainers (
id  INT  PRIMARY KEY  AUTO_INCREMENT,
name  VARCHAR(50)  NOT NULL,
specialty  ENUM('Cardio', 'Strength', 'Yoga', 'Pilates'),
is_active  BOOLEAN  DEFAULT TRUE
);
```


### Table 'trainees'

```commandline
CREATE TABLE IF NOT EXISTS trainees (
id  INT  PRIMARY KEY  AUTO_INCREMENT,
name  VARCHAR(50) NOT NULL,
email  VARCHAR(100)  UNIQUE  NOT NULL,
assigned_trainer_id  INT  NULL,
completed_workouts  INT  NOT NULL  DEFAULT 0
);
```









