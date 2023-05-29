To build and run docker put in terminal: `sudo docker-compose up -d`

To create new short link write:

`curl -X POST -H "Content-Type: application/json" -d '{"long_link": "http://example.com/very-very/long/url/even-longer"}' http://localhost:8000`

To get long link write:

`curl http://localhost:8000/<short_link>`