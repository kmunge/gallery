#Gallery-Arena

#### This is an application to make your gallery collection and showcase  your beauty

#### By **Munge Kevin Oroko**

## Description
Gallery arena is modern day photography and art work collection, where the owner has rights to upload his/her collection  and user can be able
to view search ,and copy images for their own download and usage.
## BDD Specifications

|    Users Requirements    |                Input              |               Output                     |
| :---------------------:  |   :----------------------------:  |  :------------------------------------:  |
| To view all images       |   Navigate to the home page       | All the images will be displayed         |
| View image details       |   Click on the image              | Image details will be displayed          |
| Search for images in the same category| Input the image category in the search bar |Images in that category will be displayed |
| Filter images based on location |  Navigate to the filter button and select a location | Displays images for that location|
| Copy image Link|   Click on copy link on the image footer  | Copies the image link path |


## Setup/Installation Requirements
* Ensure you have Installed Python3.6
* Clone the My Gallery Repository
* Create and Activate your virtual environment - `python3.6 -m venv --without-pip virtual` && `source virtual/bin/activate`
* Install dependencies - `pip install -r requirements.txt`
* Create a Database - `psql` then `CREATE DATABASE gallery`
* Run Migrations - `python3.6 manage.py makemigrations gallery` then `python3.6 manage.py migrate`
* Run the App - `python3.6 manage.py runserver`
* Application should open on `localhost:8000` 

## Known Bugs
There are currently no known bugs

## Technologies Used
* Python 3.6
* Bootstrap
* Heroku
* HTML
* Django

## Support and contact details
for support contact Munge Kevin : tel - 0707280118, email - orokomunge@gmail.com
### License
MIT
Copyright (c) {2019} **Munge Kevin Oroko**
  