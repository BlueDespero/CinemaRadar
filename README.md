# CinemaRadar

1. Description
    
    This repository contains a web scraping program created for cinema enthusiasts. When run, the program will ask the user to input the title of a movie he is looking forward to see and the date he is interested in. Then CinemaRadar will proceed to search for the screening of the movie in local cinemas. In the end it will present the user with a list of cinemas and hours at which the movie can be seen.

2. Running

    CinemaRadar can be used by running the main.py command with a line:
        
        python3 main.py

    An alternative to that is using a docker container. With Dockerfile provided all that is required from the user is to build a docker image with a line:
        
        sudo docker build -t cinema_docker .
        
    And then starting it by typing:
        
        sudo sh start.sh
        
    That will put you inside the container where you can start enjoying CinemaRadar with:
        
        python3 docker_main.py

3. Workings

    The program is using selenium python library with headless Chrome driver to scrap interesting information about the movies straight from the web pages of the cinemas. Cinemas it has access to are stored in dataset/cinemas.p pickle file in a form of instances of Cinema class.

    Because cinemas of the same brand have the same design of their websites it is enough to write a procedure for scraping one of them to be able to scrap info from any cinema of that brand. In the current state of CinemaRadar the program can handle scraping CinemaCity, Multikino and Kino Odra (but this one is just a local cinema). That means any cinema of those brands can be added to the search pool in a matter of a few lines of code.

4. Limitations

    The project is still a work in progress, so right now it is only able to detect cinemas in Wroclaw and Olawa. It will be changed in future versions.

5. Goals

    + Adding more cinemas
    + Allowing the users to select cinemas they are interested in
    + Creating GUI for CinemaRadar
