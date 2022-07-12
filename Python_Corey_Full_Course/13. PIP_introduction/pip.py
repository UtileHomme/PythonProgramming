# How to get description of a particular package

# pip help install
# pip search install

# How to get a list of packages already installed along with the version

# pip list

# How to install a package

# pip install <package_name>

# How to get a list of packages which are not using the latest version
# pip list -o / -outdated

# How to upgrade a particular package
# pip install -U <package_name>

# How to output all the current packages and version into another file so that it can be reused by another

# pip freeze > requirements.txt

# how to print contents of a file

# cat requirements.txt

# How to install all packages from a file

# pip install -r requirements.txt

# How to upgrade all packages list which are currently not upgraded

# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs =n1 pip install -U






