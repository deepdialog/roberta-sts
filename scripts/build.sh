#!/bin/bash

set -e
docker build -t qhduan/roberta-sts .
docker push qhduan/roberta-sts

