<h1 align="center">API test cases for OPEN API SCHEMA(OAS) 
using python .</h1>

## Overview
This repository contains test cases for OPEN API schema (artists.yaml) in root .
Test cases for above schema are under tests/tests/artists folder.

As the above schema is a dummy API , 
I have also added similar (and some more tests) for a live API (petstore.yaml)
You can find running tests under tests/tests_petstore folder .
You can also find the html report under reports/htmlreport.html and a log file with all minute details in eports/openapi_tests.log


## Run Locally on Linux/Mac :

Prerequisites
Git
Docker
Make
Python 3.7 and up

1) Open a terminal
2) Change to your favorite local directory (i.e. cd /opt)
Clone the repository / Unzip the attachment .

git clone 
3)Change to the project root directory
4)cd /opt/openapi-python-pytest-requests-artists
5) Create a new file, name it secrets.ini and add the following contents
APP_URL=http://host.docker.internal:8080
ADMIN_USER=admin
ADMIN_PASSWORD=admin
6)Start development environment
make dev
This command will remove any existing restapi_testfwk containers, 
build a new test/openapi-python-pytest-requests-artists image, 
start a container, mount local code under /opt/openapi-python-pytest-requests-artists
 and provide a /bin/bash terminal.
 7)Navigate to suites folder and run all_test_suite.sh by below command
 cd suites
 ./all_test_suite.sh
 
 ABove will run tests and generate reports (HTML and logs) under reports folder


## Integrating with CI-CD (Jenkins) : 
This test can be integrated with ci-cd tool like Jenkins and can be run on linux machine/docker image.
Refer Sample pipeline : jenkinsGroovyPythonSamplePipeline.groovy

Note we can also use the above same steps but on Jenkins server

## Technology used:

 - Python 
 - Behave 
 - Pytest
 - pytest-html
 - Jenkins
 - logging
 - PyCharm
  
 ## Folder structure
 - lib : Contains individual methods for artists and petstore api and some reusable methods in utils.
 - payload : Contains payload needed (valid/invalid)for our test cases.
 - reports : Contains log file and html report of tests .
 - tests : It contains actual tests under respective folder .
 - config.py : config file for test data like url  , username , password .
 - requirements.txt : contains all the dependencies required by this API framework .
 - suites/all_test_suite.sh : shell file to run the all tests which contain below lines .
 #!/bin/sh
set -eux

pytest --html=./reports/htmlreport.html --self-contained-html ../tests/tests_petstore/test_petstore_endpoint.py
 

 
  ## Scenarios automated for artists.yaml
  Note - For all tests the first step/assertion is to validate if response 
  received is 200(ok) except 4 and 5 where we expect 400 .
  
  
 1)Get all Artists wit limit and offset details 
 2)Post (Create) a new artist with Post method and valid and validate message is "Successfully created a new artist"
 3)Get the above artists details created above with passing username and validate data .
 4)Post a new artist with invalid data with Post method and validate response is 400 .
 5)Get artist with passing invalid request and validate response is 400 . 
 
  ## Scenarios automated for petstore.yaml
  Note - For all tests the first step/assertion is to validate if response received is 200(ok)
  except for 6 and 7 where we expect response as 404 and 405
  
 1)Post Pet details with valid payload .
 2)Get above pet details by passing petid created from above step with get method and validate petname .
 3)Update above pet details by POST method and update name and availability and validate update message is string .
 4)Get details of above updated pet details and valid if name and availability is updated .
 5)Delete above updated petid with delete method
 6)Get details of incorrect petid and validate response is 404 .
 7)Get details of invalid petid and validate response is 405 .
 
Actual run on my local 
 
 (venv) Pawans-Air:suites pawankalra2$ ./all_test_suite.sh
+ pytest --html=./reports/htmlreport.html --self-contained-html ../tests/tests_petstore/test_petstore_endpoint.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.7.1, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/pawankalra2/PycharmProjects/OpenApi-Python-pytest-requests-artists/tests, configfile: pytest.ini
plugins: metadata-2.0.1, html-3.1.1
collected 3 items                                                                                                                                         

../tests/tests_petstore/test_petstore_endpoint.py ...                                                                                               [100%]

---------- generated html file: file:///Users/pawankalra2/PycharmProjects/OpenApi-Python-pytest-requests-artists/suites/reports/htmlreport.html -----------
==================================================================== 3 passed in 3.28s ====================================================================

Via Docker 


====================================================== test session starts ========================================================
platform linux -- Python 3.7.13, pytest-7.1.1, pluggy-1.0.0
rootdir: /opt/openapi-python-pytest-requests-artists/tests, configfile: pytest.ini
plugins: metadata-2.0.1, html-3.1.1
collected 3 items                                                                                                                  

../tests/tests_petstore/test_petstore_endpoint.py ...                                                                        [100%]

-------------- generated html file: file:///opt/openapi-python-pytest-requests-artists/suites/reports/htmlreport.html --------------
======================================================== 3 passed in 7.86s =========================================================
root@05825173c19c:/opt/openapi-python-pytest-requests-artists/suites# 

