#!/bin/sh

export OTEL_TRACES_EXPORTER=jaeger-thrift-splunk
splunk-py-trace-bootstrap
splunk-py-trace python3 app.py