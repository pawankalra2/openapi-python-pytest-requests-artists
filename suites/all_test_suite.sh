#!/bin/sh
set -eux

pytest --html=../reports/htmlreport.html --self-contained-html ../tests/tests_petstore/test_petstore_endpoint.py
