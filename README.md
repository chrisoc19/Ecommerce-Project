[![Build Status](https://travis-ci.com/chrisoc19/Ecommerce-Project.svg?branch=master)](https://travis-ci.com/chrisoc19/Ecommerce-Project)
# Viking POPS

In this project I am focusing on creating a website aimed towards the POP collector community.

Users will also be able to register and login to purchase items.

This project will use a postgres database, and the application itself will be set up using the Django web framework.

The primary target audience is anyone that has an interest in POP figures, whether they are casual collects or just shopping for the perfect gift. I Have added many diffrent types of POP figures to increase my target audience, Such as Disney figures, Looney Tunes for the younger audience and real life famous people and gaming figures for the older audience. In my opinion there is something for everyone. 
 
## UX
My wire frames were created in Balsamiq and can be found here:

[wire Frames](https://github.com/chrisoc19/Ecommerce-Project/blob/master/mockups/New%20Project%20(2)%20(2).pdf)
I choose to design a simple yet elegant site.
The navigation bar is responsive having break points for smaller, medium and large screens. The navigation links disappear on screen width below 992 pixels and a burger menu icon appears top left. When the burger icon is clicked, it brings a side navigation bar across from the left.
 
The site itself will follow standard web design conventions and so the layout and initial use of the site should feel immediately recognisable to almost all users, with those lacking experience in web browsing finding the website to be self-explanatory and easy to use/navigate.

The Home page will immediately inform the user of the site’s purpose, promoting the products that sell best. 

## User Stories

- As a user I’d like to be able to find and buy from the website.
- As a user, I’d like for the website to be user-friendly and easy to navigate.
- As a user, I’d like to be able to search the website/database for the products in the store that match the search criteria.
- As a user, I'd like to be able to access the data and experience all the site has to offer, regardless of device and browser type being used.
- As a user , I expect feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.

## Features
- Navbar - Allows users to easily Navigate the site, displaying the how many items in the cart and also a way to search for a specific product and also allows the user to log in and out.

- The Home page - This page which allows users to quickly see the most popular products and other categories on offer.

- All Products - This page displays all the products the site offers.

- Product details - When a user clicks on a product it redirects to a page with an extra information about the product and an extra product image.

- Categories Page - This page has a list of all the products the site offers, once the user chooses a category, the products are then filtered to show only those products.

- Login/Logout - If a user is not logged in a login button is displayed which will take the user to the login page, If the user is logged in a logout button is displayed which will qucickly and easily log the user out, a user needs to be logged in to make a purchase.

- Shopping Cart - This page shows the items the user have added for purchase it displays the product image, the price, the quantity and the ability to add more of a product or remove the product from the shopping cart. The user can the proceed to checkout or go back to do more shopping.

- Checkout page - This is a simple page thats shows the name, quantity and price of each product, then underneath a payment form is displayed which takes the users shipping address and also takes the users payment method.



### Features Left to Implement
- In the future I would like to add more categories of POP Figures.
- In the future I would like to add a way for the user to contact the site.

## Technologies Used
- [Python](https://www.python.org/) The project uses **Python**.

- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.

- [Stripe](https://stripe.com/en-se) as payment platform to validate and accept credit card payments securely.

- [Travis](https://travis-ci.org/) for continuous integration.

- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.

- [Django Heroku](https://pypi.org/project/django-heroku/) to improve deployment of django projects on heroku.

- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.

- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.

- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.

- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.

- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.

- [GitHub](https://github.com/) to store and share all project code remotely.

- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.

- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.

- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) to simplify the structure of the website and make the website responsive easily.

- [Google Fonts](https://fonts.google.com/) to style the website fonts.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

Heroku deployment - this is done as a last step to ensure that all installed packages are included in the requirements.txt file

1. Sign up for a Heroku account
2. Install Heroku using bash: sudo snap install heroku --classic
3. Install dependencies (gunicorn, Pillow, psycopg2, whitenoise, dj_database_url)
4. Add Whitenoise to middleware inside settings.py
5. Log into heroku account with heroku login -i
6. Create a new app in bash: heroku create <app_name>
7. Copy over uploadcare and Stripe key details from bashrc into Heroku Config vars
8. Create a Procfile and add the following line: web: gunicorn <PROJECT_FOLDER>.wsgi:application
9. Add heroku app url to allowed hosts in settings.py, and also change the static directory to STATIC_ROOT
10. Create the requirements.txt file using bash: pip3 freeze --local > requirements.txt
11. Commit and push the project to heroku
- git add .
- git commit -m "commit name"
- git push heroku master
12. Set up Postgre database with heroku addons:create heroku-postgresql
13. Get the updated databse url by typing heroku config, and copy it into settings.py and Heroku's Config vars
14. Migrate database and create a superuser to make changes to it'

I deployed the site to Github with the following steps:

1. Go to this repository's github [Link](https://github.com/chrisoc19/Ecommerce-Project)
2. Click on settings --> Github Pages
3. Select "none" for the Source and then select "master branch"

To deploy the page locally:

1. Go to the github [Link](https://github.com/chrisoc19/Ecommerce-Project)
2. Click on the Clone/download button and copy the URL
3. Set up and install your own Stripe and uploadcare accounts
4. To run the application locally, type python3 manage.py runserver 8080 in bash



## Credits

### Media
- The photos used in this site were obtained from a google search.

### Acknowledgements

- Id like to thank code institute for there teaching and helping during the process of this project.
