# Dummy Package Manager
This is a dummy package manager app. 

**This code assumes you are in a Linux environment**

## Requirememnts

You need to have installed Python 3, preferebaly with virtual environment. We recommend Venv:

    python3 -m venv <YOUR_VENV_PATH>

activate it with

    source <YOUR_VENV_PATH>/bin/activate

and then execute the app with this command to use it directly from the console

    python3 dummyApt.py

Or if you have an input file

    python3 dummyApt.py < inputfile

Or if youd like to redirect the output to another file
    
    python3 dummyApt.py < inputfile > outputfile

## Tests

If you'd like to run the tests you'll need Pytest

    pip install pytest

and just execute it on the terminal like so

    pytest

## The App

Much like `apt`, `dummyApt` "installs" applications on a REPL loop or from an input file accoring to the 

    DEPEND pk1 pk2 [pk3]
    INSTALL pk
    REMOVE pk
    LIST
    END

syntax