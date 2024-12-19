#!/bin/bash


# Variables
check_third_arg=false
file=""
dir=""
count=0

# Parse command-line options
while getopts ":atf:d:h" opt; do
    ((count++))
    if [[ $count -eq 3 ]]; then
        third_option=$opt
        third_argument=$OPTARG
    fi
    case $opt in
        a)
            show_all_params=true
            ;;
        f)
            file=$OPTARG
            ;;
        d)
            dir=$OPTARG
            ;;
        t)
            check_third_arg=true
            ;;
        \?)
            echo "Invalid option: " 
            exit 1
            ;;
    esac
done

if $check_third_arg; then
    if [ -n $third_option ]; then
        echo "The third option is: -$third_option"
        if [[ -n $third_argument ]]; then
            echo "The argument for the third option is: $third_argument"
        else
            echo "The third option has no argument."
        fi
    else
        echo "Less than three options were provided."
    fi
fi


# Display all passed parameters
if $show_all_params; then
    for param in "$@"; do
        echo "\"$param\""
    done
fi


# Handle the -f option (file content display)
if [[ -n $file ]]; then
    if [[ -f $file ]]; then
        echo "Contents of $file:"
        cat "$file"
    else
        echo "File '$file' does not exist."
    fi
fi

# Handle the -d option (create directory)
if [[ -n $dir ]]; then
    if [[ ! -d $dir ]]; then
        mkdir "$dir"
        echo "Directory '$dir' created."
    else
        echo "Directory '$dir' already exists."
    fi
fi


