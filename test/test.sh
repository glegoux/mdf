#!/usr/bin/env bash
#
# test.sh
#
# Test all exercices for each yearly competition.
# (except 2013, 2016 and 2017 sessions)

cd "$(dirname "$0")"
cd ..

find . -name launch | grep -vE '2013|2016' | xargs -n1 bash -c
