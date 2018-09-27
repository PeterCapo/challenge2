[![Build Status](https://travis-ci.org/PeterCapo/challenge2.svg?branch=develop)](https://travis-ci.org/PeterCapo/challenge2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/441712ba837443e1bcf5983fbf8d9ef4)](https://app.codacy.com/app/PeterCapo/challenge2?utm_source=github.com&utm_medium=referral&utm_content=PeterCapo/challenge2&utm_campaign=Badge_Grade_Settings)
[![Maintainability](https://api.codeclimate.com/v1/badges/3ed8671c4de83bbb17d8/maintainability)](https://codeclimate.com/github/PeterCapo/challenge2/maintainability) 
[![Coverage Status](https://coveralls.io/repos/github/PeterCapo/challenge2/badge.svg?branch=develop)](https://coveralls.io/github/PeterCapo/challenge2?branch=develop)

CHALLENGE2

Installation and Setup

Clone the repository 

Create a virtual environment

    virtualenv venv --python=python3.7

Activate virtual environment

    source venv/bin/activate
    or for windows OS
    venv\scripts\activate

Install required Dependencies

    pip install -r requirements.txt



API Endpoints 

| Method | Endpoint                        | Description                           |
| ------ | ------------------------------- | ------------------------------------- |
| POST   | /api/v1/orders                  | Place an order                        |
| GET    | /api/v1/orders                  | Get all orders                        |
| PUT    | /api/v1/orders/<{id}>           | Update order status                   |
| GET    | /api/v1/orders/<{id}>           | Get a specific order                  |

Test on Postman 

Run Test
- nosetests
