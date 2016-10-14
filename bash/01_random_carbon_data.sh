#!/usr/bin/bash

# We need a script that can generate random carbon data. The data should be in the form of:
#
# <metric.name> <value> <timestamp>
#
# For example:
# foo.bar.1 12 1476468440
# foo.bar.2 53 1476468440
# foo.bar.3 71 1476468440
# foo.bar.1 18 1476468450
# foo.bar.2 53 1476468450
# foo.bar.3 71 1476468450
#
# Output should be for three metric names. Each value should be a random number between 0 and 99
# The timestamps should be every ten seconds from 10 days back to now aligned on the 10 second
# boundary
#
# Note: To get date to work as expected, use gdate
