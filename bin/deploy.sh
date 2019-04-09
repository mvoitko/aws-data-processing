#!/usr/bin/env bash

export AWS_REGION=eu-west-1
export AWS_PROFILE=personal

cd ..

apex deploy
apex infra apply -auto-approve
