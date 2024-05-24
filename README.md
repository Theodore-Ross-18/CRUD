# CRUD - Final Exam Drill (IT6)

Building a CRUD REST API with MySQL, Testing, and XML/JSON Output

> A CRUD (Create, Read, Update, and Delete) REST API for your chosen MySQL database similar to the Python Flask API Programming. The API will allow users to interact with the database and will act as an Interface to any client that understands JSON or XML. You will also set up tests to ensure the functionality of the API, and provide the option to format the API output as XML or JSON.

# What is REST API?

> A REST API, or Representational State Transfer API, is a set of rules and conventions for building web services. It allows different software applications to communicate with each other over the internet.

> At its core, a REST API works by defining a set of endpoints (URLs) that represent various resources (such as users, products, or data). Each endpoint corresponds to a specific action, such as retrieving data (GET), creating new data (POST), updating existing data (PUT or PATCH), or deleting data (DELETE).

> The main purpose of using a REST API is to enable interoperability between different systems and platforms. It provides a standardized way for applications to exchange data regardless of their underlying technologies. REST APIs are widely used because they are simple, scalable, and can leverage the existing infrastructure of the World Wide Web, including HTTP protocols and data formats like JSON or XML.

# Instructions:

> 1. `Setup your database`: It will be assumed that you’ve installed a MySQL server with your chosen database in your system, make sure it contains enough (20 records and above) for testing.

MySQL Workbench: 

    Database Name: flask_db
    Table Name: users

> 2. Create a new `GitHub repository` for your project. Make sure to select the option to initialize the repository with a README file, write down the installation procedures of your project here once you’re done. Clone the repository to your local development environment.

    https://github.com/Theodore-Ross-18/CRUD

> 3. `Create a virtual environment` for your project, and ignore it in your. gitignore file and go into the virtual environment, do not include the environment when you upload your project in Github.

    Venv File Name: CRUD
    gitignore: CRUD/

    Purpose: To not include or ignore the libraries installed in the repository and lessen the file size of the project

> 4. Install `libraries` needed for this project

Directory: Inside the VENV CMD (Command Line Interface)

Note: Active the VENV first before installing

1. Flask

        pip install Flask

2. Flask-Restful

        pip install Flask-Restful

3. Flask-SQLAlchemy

        pip install Flask-SQLAlchemy

> 5. Develop your `Flask REST API Web Application`.

Project Source:

    https://drive.google.com/drive/u/0/folders/1njA25MwIUPDhw86ao7FAmVoL8wrSpfTr

# Grading Breakdown:

> 1. Github commit and push (containing multiple commits having different timestamp):

    Push your local Git repository to the remote repository on GitHub. search for git best practices, to have a basic idea how to organize your commits.

> 2. CRUD(Create, Read, Update, Delete) operations (contains input validations, error handling):

    Return appropriate HTTP responses based on the success or failure of the operations, search for the appropriate header values when providing responses for API’s.

> 3. CRUD Tests:

    Write test cases to cover all the CRUD operations for the API endpoints. Ensure that the tests cover different scenarios and edge cases.

> 4. Formatting options:

    Modify the API endpoints to check for a URI parameter (e.g., format) that specifies the desired output format (XML or JSON). If the parameter is not provided, JSON should be the default format.

> 5. Implement search functionality, allowing users to search for records based on specific criteria.

> 6. Add security mechanisms to secure the API endpoints (search JWT or similar)

> 7. Documentation:

    Update the README file in your GitHub repository to include project details, installation instructions, usage examples, API usage (see documentation of popular APIs for more info.) and any additional information that would help others understand and run your project.

> 8. Video explainer: 

    No points, but is required for this drill, submission without a video explainer means No Grade, features which are implemented in the code but without explanation in the video means No points. (You must be visible in the video. Explain your work as technical as possible)

# SUBMISSION REQUIREMENTS:

- public Google drive folder link containing the project (source code, ERD for db, SQL dump etc.)

- Video explainer (MP4 format) link (you can source this anywhere as long as it’s publicly accessible)

- Github URL that points to your project repository, every feature added to the project and bug fixed must be encapsulated in a commit with logical commit message, too few and inconsistent/illogical commits will be graded below passing score.

- Provide all of the above links to a Google form provided in our Google classroom post (other form of submission will not be accepted).