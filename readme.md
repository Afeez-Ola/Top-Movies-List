Movie Rating App - Flask
========================

This is a simple Flask web application that allows users to create a list of movies along with their ratings and reviews. The app uses the Movie Database (TMDb) API to fetch movie information based on user input, and users can add, edit, and delete movies from their list.

Features
--------

-   Add a new movie to the list along with its title, year, description, rating, and review.
-   Fetch movie information using the TMDb API based on the movie name provided by the user.
-   Display a list of all movies with their respective ratings and reviews, ordered by rating.
-   Allow users to edit the rating and review for each movie.
-   Provide the option to delete movies from the list.

Setup
-----

1.  Install Dependencies:

    First, you need to install the required Python packages. You can do this by running the following command in your terminal:

    Copy code

    `pip install Flask Flask-Bootstrap Flask-SQLAlchemy requests`

2.  API Key:

    The application uses TMDb API to fetch movie data. To get the API key, you need to sign up on the TMDb website (<https://www.themoviedb.org/>) and obtain your API key.

3.  Database Setup:

    The app uses SQLite as the database, and it will create a new file `movie-list.db` in the project directory. You can create the database tables by running the following commands in the Python shell:

    pythonCopy code

    `from your_app import db
    with your_app.app_context():
        db.create_all()`

    Replace `your_app` with the name of your Flask application instance.

4.  Run the App:

    Now, you can run the Flask app by executing the following command in the terminal:

    Copy code

    `python your_app.py`

    Replace `your_app.py` with the name of your Python file containing the Flask app.

5.  Access the App:

    The app will be accessible at `http://127.0.0.1:5000/` in your web browser.

How to Use
----------

1.  Home Page:

    The home page displays a list of all the movies in the database, sorted by their ratings. Each movie card shows the movie title, year of release, rating, and review. The rating is given as a floating-point number between 0 and 10.

2.  Add Movie:

    Click on the "Add Movie" button on the home page to add a new movie to the list. You can enter the movie name, and the app will fetch the movie details from the TMDb API based on the name provided. The movie details will be displayed in the form. Review the details and click the "Save" button to add the movie to the list.

3.  Edit Movie:

    Click on the "Update" button on a movie card to edit its rating and review. You can change the rating and/or review and click the "Save Changes" button to update the movie details.

4.  Delete Movie:

    To delete a movie, click on the "Delete" button on its card. The movie will be permanently removed from the list.

Technologies Used
-----------------

-   Flask: A micro web framework for Python used for building the web application.
-   Flask-Bootstrap: A Flask extension that integrates the Bootstrap CSS framework to provide better styling and responsiveness to the app.
-   Flask-SQLAlchemy: A Flask extension that simplifies working with the database by providing an Object-Relational Mapping (ORM) system.
-   requests: A Python library used to make HTTP requests to the TMDb API.

Note
----

-   This app uses the TMDb API to fetch movie details based on user input. Please ensure you have an active internet connection while adding a new movie to the list.
-   The TMDb API key used in the code is provided as a bearer token. Make sure to replace it with your actual TMDb API key when running the app.

License
-------

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code for both personal and commercial purposes. However, keep in mind the usage of the TMDb API should comply with their terms and conditions.

Disclaimer
----------

This project is intended for educational purposes and should be used responsibly. It is your responsibility to comply with all copyright and licensing restrictions related to the movie data obtained from the TMDb API. The developer of this project shall not be held liable for any misuse or unauthorized use of copyrighted materials.