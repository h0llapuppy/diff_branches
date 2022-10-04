# Shared library to get difference between OS Alt linux dev branch packages

## Steps for setup library:

> (sudo) apt-get 
> (sudo) update apt-get install python3

> git clone https://github.com/h0llapuppy/diff_branches.git

> tar xvzf get_diff_branches-1.0.tar.gz

> cd get_diff_branches-1.0/

> (sudo) python3 setup.py install

## Install complete

## Now enter the command in the terminal command line:

    get-diff-branches <branch1> <architecture1> <branch2> <architecture2> 

(For example: get-diff-branches p10 x86_64 p9 x86_64)

## After executing the command, a message will appear in the command line: "Select path to write result files:"

## Enter the path (for example: /home/user/) where 3 files will be written:

    b1-b2.txt - Packages exist in <branch1> but not in <branch2>

    b2-b1.txt - Packages exist in <branch2> but not in branch <branch1>

    same_pack_v1_more_v2.txt - Same packages for both specified branches, but only those whose version is greater for <branch1> then <branch2>
