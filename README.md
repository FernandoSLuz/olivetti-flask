# Olivetti Flask Chatbot

This repository contains a Flask application that uses Dialogflow to create a chatbot capable of handling greetings, text and audio messages via Wassenger API to interact with users.

**EIT Digital DeepHack - Olivetti - Trento/Italy - 1st Place (October 2019)**

Project created for the first international hackathon, Social Olivetti is a solution that integrates the Olivetti API with one of the largest communication tools on the planet, WhatsApp, creating not only a chatbot using security and validation techniques but also a software that serves as an alternative to complex and difficult to handle apps, drastically lowering the learning curve for merchants.

With Social Olivetti, merchants will be able to receive notifications and set up and customize the features of the cash machines. They will also be able to control their business as a whole, always in a simple way and without the need to download any other tool/app, democratizing the use for everybody.

Basically, our goal is to turn back and raise with technology the merchant's focus on what matters most: his business.

## Features

- Flask application with a minimalistic structure.
- Interaction with Dialogflow using text input and audio input.
- Integrated with Wassenger API to handle messages.

## Getting Started

These instructions assume you have Python 3 and pip installed.

### Installing dependencies

First, clone the repository and navigate to the root directory:

```sh
git clone https://github.com/FernandoSLuz/olivetti-flask.git
cd olivetti-flask
```

Then, create a virtual environment to install dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```sh
pip install -r requirements.txt
```

### Running the server

To run the server, execute:

```sh
export FLASK_APP=app.py
flask run
```

The Flask application will start serving on `http://127.0.0.1:5000/`.

## Most Important Scripts

The main scripts in this repository are the following:

- **dialogflowBackend.py**: Contains the Dialogflow logic and routes for greeting users and handling text input and audio input messages.

- **app.py**: The main Flask application file, responsible for serving the application routes and registering the blueprints from the dialogflowBackend script.

- **requirements.txt**: A file with the necessary dependencies to run the application.

## License

This project is licensed under the MIT License.
