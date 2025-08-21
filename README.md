# WEB-CALCULATOR

#### Video Demo:  <URL HERE>

#### Description:

This project is a full-featured, web-based scientific calculator that offers more than just computation. It provides a personalized user experience by integrating user authentication and a persistent history of calculations, powered by a robust backend and a dynamic frontend. Users can sign up, log in to a secure account, perform complex mathematical operations, and revisit their work at any time.

The application is built to be intuitive and reliable, serving as a powerful tool for students, engineers, and anyone in need of a quick and dependable calculator. By saving all calculations to a database, it eliminates the need to manually record results and offers a convenient way to track and review past work.

Technologies Used

This application is built using a modern and efficient technology stack, with each component playing a crucial role in its functionality:

    Frontend:

        JavaScript: Provides the dynamic, interactive functionality for the calculator interface.

        HTML & CSS: Structure and style the user-facing web pages.

    Backend:

        Flask: A lightweight and powerful Python web framework that handles all server-side logic, including routing, data processing, and rendering templates.

    Database:

        SQL (or SQLite3): A relational database used to store user information and all calculation records, ensuring data persistence and integrity.

How to Run the Application

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites

You will need Python and pip installed on your system.
Setup and Installation

    Clone the Repository:

    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

    Install Dependencies:

    This project relies on a few Python packages that need to be installed. We recommend using a virtual environment to manage dependencies and avoid conflicts with other projects.

        Create a virtual environment:

        python -m venv venv

        Activate the virtual environment:

            On macOS and Linux:

            source venv/bin/activate

            On Windows:

            venv\Scripts\activate

        Install the required packages using pip:

        pip install Flask werkzeug

    If your project uses a specific database connector, such as psycopg2 for PostgreSQL or mysql-connector-python for MySQL, you would need to install that package here as well. For a simple local setup using SQLite, no additional package is needed.

    Run the Application:

    Once the dependencies are installed, you can start the Flask application.

    python app.py

    The server will start, and you'll see a message in the terminal indicating that the application is running.

Usage

    Access the Application: Open your web browser and navigate to the address provided in the terminal output, typically http://127.0.0.1:5000.

    Create an Account: You'll be prompted to either log in or sign up. Create a new account by providing a username and password. This will create a secure, personalized profile for you.

    Perform Calculations: After logging in, you'll be redirected to the main calculator interface. Use the buttons and input field to perform your desired scientific calculations.

    View History: Navigate to the History page to view a complete, chronological list of all the calculations you have performed while logged in. Each entry will show its result.

