#! /bin/sh

if test "$1" = ""; then
  PYINTERP="python"
else
  PYINTERP="$1"
fi

$PYINTERP -m pudb.run debug_me.py
