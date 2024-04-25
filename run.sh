#!/bin/bash

# Install dependencies
# pip install --no-cache-dir -r requirements.txt

# Run the application and database in parallel
docker-compose up --build &
