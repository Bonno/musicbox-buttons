#!/bin/bash


SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
#echo "Script directory: $SCRIPT_DIR"

source $SCRIPT_DIR/venv/bin/activate

$SCRIPT_DIR/venv/bin/python $SCRIPT_DIR/buttons.py
