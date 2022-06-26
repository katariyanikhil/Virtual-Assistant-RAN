# Virtual-Assistant-RAN
We have created a Virtual Assistant called RAN which can do basic task along with perform maths operations, get location, get latest news(india), weather information, etc..

## Features
It can do the following things:
1. Tell current Date and Time
2. Tell the current Location
3. Tell the top 5 news headlines
4. Make a note for the user
5. Open any software or app in the system
6. Show the system statistics
7. Perform any maths operations
8. Tell the weather of any city
9. Open any website
10. Search anything on wikipedia
11. Can tell a Joke

## API:
1. To perform the maths operations, we used the Wolframalpha API
2. To get weather information we used OpenWeather API
3. To get news we are using The times of India call
4. For Location we are using Google Map API call

## How to run?
1. Install pip
>sudo apt install python3-pip

2. Now using pip, install the dependencies and libraries required to run this project which are included in the requirements.txt file
>pip install -r requirements.txt

3. Run the Main python file
>python3 main.py

## Project Structure:
VA                  - Contains the features and init file
   features         - Has all the code for various features of the VA
   _init_.py        - For providing packages
main.py             - Main program file
readme.txt          - readme file
requirements.txt    - requirements file
