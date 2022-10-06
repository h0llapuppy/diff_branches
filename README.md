# Shared library to get difference between OS Alt linux dev branch packages

## Requirements

+ **python3**

## Steps for setup library:

    git clone https://github.com/h0llapuppy/diff_branches.git
    python3 setup.py sdist
    cd dist/
    tar xvzf get_diff_branches-1.0.tar.gz
    cd get_diff_branches-1.0/
    (sudo) python3 setup.py install

## Install complete

## Now enter the command in the terminal command line:

    get-diff-branches <branch1> <branch2> <architecture> <calc-method>
    
### About Arguments

- **branch1** (required) - Argument that points to the 1st branch for next calculation 

- **branch2** (required) - Argument that points to the 2nd branch for next calculation 

- **architecture** (required) - Argument that points to architecture for both branches

- **calc-method** (optional) -  Argument that points to the method of calculation:

1. **b1-b2** - Print to the terminal a list of packages which exist in **branch1** but not in **branch2**
2. **b2-b1** - Print to the terminal a list of packages which exist in **branch2** but not in **branch1**
3. **b2andb1** - Print to the terminal a list of same packages for both specified branches, but only those whose version is greater for **branch1** then **branch2**
4. **None** - Message will appear in the command line: "Select path to write result files:" you must enter the path (for example: /home/user/) where 3 files will be written:

    b1-b2.txt - **b1-b2**
    b2-b1.txt - **b2-b1**
    same_pack_v1_more_v2.txt - **b2andb1**
