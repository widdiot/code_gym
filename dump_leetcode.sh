#!/bin/bash

# Script to export LeetCode submissions using provided cookies.

# Function to display usage information
usage() {
    echo "Usage: $0 <cookies_file>"
    echo "  <cookies_file> - Path to the cookies file for LeetCode."
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    usage
fi

# Assign the first argument to the cookies variable
cookies=$1

# Check if the cookies file exists
if [ ! -f "$cookies" ]; then
    echo "Error: Cookies file '$cookies' not found."
    exit 1
fi

# Export LeetCode submissions using the provided cookies
leetcode-export --cookies "$cookies" --folder ./submissions
