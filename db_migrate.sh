#!/bin/bash
source env.sh

CURRENT_ID_STR=`ls migrations/versions | tail -1`
NEXT_ID=`expr ${CURRENT_ID_STR:0:4} + 1`
flask db migrate -m $1 --rev-id=`printf "%04d" ${NEXT_ID}`