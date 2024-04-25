If you're running in Ubuntu, run the following: sudo apt-get install python<version>-dev

### This tempalte was created for possible future reuse. This was built just for practice ###

The Scenario - an API backend for a real estate website that caters to various players of a brokerage: the brokerage, client, agent, etc

The api needs to authenticate each type of user and provide routing to sub-applications that cater to functionality specific to each user type, but, database can be linked between user types. E.g. Brokerage can optionally manage aspects of agent accounts but agents' contacts cannot be seen by anyone else.