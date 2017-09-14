#!/usr/bin/env bash
#
# test.sh
# 
# Test all exercices for each yearly competition.
# (except 2013 and 2016 sessions)

cd "$(dirname "$0")"
cd ..

find . -name launch | grep -v 2016 | xargs -n1 bash -c
