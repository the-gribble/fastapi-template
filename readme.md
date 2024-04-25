### This tempalte was created for possible future reuse. This was built just for practice ###

The Scenario - an API backend for a real estate website that caters to various players of a brokerage: the brokerage (i.e. agent admin staff), client, agent, etc. Built using Python, FastAPI, Pydantic, and SQLAlchemy, with Postgres as a backend, all running in docker. 

The api needs to authenticate each type of user and provide routing to sub-applications that cater to functionality specific to each user type, but data can be linked between user types. E.g. Brokerage can optionally manage aspects of agent accounts but agents' contacts cannot be seen by anyone else, including other other agents in the same brokerage.

If running Windows WSL/Ubuntu, you may need to run: sudo apt-get install python<version>-dev
