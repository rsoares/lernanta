To get the API working you will have to install the dependencies in requirements/prod.txt
After that, start up the server and go to:
http://localhost:8000/en/api/v1/?format=json

That is a 'summary' of the things the API shows (endpoints). Each of them has
the following uses (only showing projects here but also works with user profile
and schools):

http://localhost:8000/en/api/v1/project/?format=json
http://localhost:8000/en/api/v1/project/1/?format=json
http://localhost:8000/en/api/v1/project/set/1;3/?format=json
http://localhost:8000/en/api/v1/project/schema/?format=json

The API is read-only by default but it does not have to be.
