# Dummy Package Manager
This is a dummy package manager app. 

**This code assumes you are in a Linux environment**

## Requirememnts

You need to have installed Python 3, preferebaly with virtual environment. We recommend Venv:

    python3 -m venv <YOUR_VENV_PATH>

activate it with

    source <YOUR_VENV_PATH>/bin/activate

and then execute the app with this command to use it directly from the console

    python3 myApt.py

Or if you have an input file

    python3 myApt.py < inputfile

Or if youd like to redirect the output to another file
    
    python3 myApt.py < inputfile > outputfile

## Tests

If you'd like to run the tests you'll need Pytest

    pip install pytest

and just execute it on the terminal like so

    pytest

## The App