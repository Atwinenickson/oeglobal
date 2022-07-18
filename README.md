# TO RUN THIS APPLICATION

## RUN MIGRATIONS

**cd oeglobal/oeglobal**

**CREATE VIRTUAL ENVIRONMENT: python3 -m venv venv**

**ACTIVATE VIRTUAL ENVIRONMENT: . venv/bin/activate**

**PIP3 INSTALL ALL REQUIREMENTS (beautifulsoup, requests,django,rest framework, etc)**

## RUN APPLICATION

**RUN python3 manage.py makemigrations**

**RUN python3 manage.py migrate**

**RUN python3 manage.py runserver**

## ADD DATA TO DATABASE

**cd oeglobal/oeglobal/oeglobal\_api/usecases**

**python3 savearticles.py**

**python3 savepodcast.py**

**python3 savepodcastsummary.py**

## RUN

**[http://localhost:8000/oeglobal](http://localhost:8000/oeglobal) to view the api&#39;s and select the required api to view data.**



### View all apis
![image info](oeglobal/pictures/apis.png)

### View all articles
![image info](oeglobal/pictures/articles.png)

### view podcasts
![image info](oeglobal/pictures/podcasts.png)

### View recent podcasts
![image info](oeglobal/pictures/recentpodcasts.png)

### View single podcasts
![image info](oeglobal/pictures/singlepodcast.png)

### View topics
![image info](oeglobal/pictures/topics.png)

### View topic urls
![image info](oeglobal/pictures/topicurls.png)

### View database
![image info](oeglobal/pictures/databases.png)
