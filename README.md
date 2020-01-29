# Let's Skate
# http://13.57.201.1/

Let's Skate! is a full-stack web application, built using Python with Django framework. 
By integrating Google Maps API, users can view unique places to skateboard. 
Markers of each skate spot populate on a map centered on Southern California. 
Each marker is clickable and displays additional information including name, description and an image of each spot. 
Registered users can create, update or delete existing spots. Uploaded images are stored using an AWS S3 Bucket. 
The map markers are stored as objects in a MySQL database and are rendered dynamically when the page loads. 
Let's Skate is deployed using AWS EC2 on an Ubuntu server with NGINX and Gunicorn.

## Getting Started

Upon loading the page, users will be prompted to either create an account, or login to an existing accout. 
When registering, each inout field must be validated in order for the account to be created. Validation includes minimum age, length of name,
uniqeness, and RegEx filters.
For demonstration purpases, a Demo User login is pre-populated so that account creation is not neccessary to view the map.
```
User: demo@demo.com
```
```
Password: Password1!
```

## Using the Map

After logging in, Google Maps API is used to load a map which displays all of the unique map markers stored in the MySQL database. 
Each map marker is clickable, and will desplay information about a unique skate spot, including the Name, Description, Type and a Photo. 
Users also have the ability to edit or delete each spot from the map.

## Adding a new Spot

To add a new skate spot to the map, users are required input the Name, Description, Type, Longitude, Latitude and a Photo. 
Spots are stored as objects in a MySQL database, and the images are stored in an AWS S3 Bucket. 

## Updating User profile

Users can also update their profile information, including their Name, Email or Birthday
