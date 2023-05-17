#!/bin/bash

psql -h "${HOST}" -p "${PORT}" -d "${NAME}" -U "${USER}" -f scripts/sql/initial_data.sql
