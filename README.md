# README

This repository is to help get you started with python/anaconda.

Hopefully this README gets updated as this repo grows.

# Installing Packages


## Beginning Instructions

### Git

Git is a tool to track software developement.

Git is most easily used from the command line. This means that
you will need to know a few window command line commands before
you can effectively use git. 

#### Install git and make a github account.

do it.

1. open the windows command line. 
	* in win10 you can type in sequence: StartButton -> 'cmd' -> Enter
2. type 'git' and hit enter
3. you should see a git specific help text. If you do not figure out
what is wrong via googling

#### create a directory

We want a place to hold our python programs we are going to write.
Lets make a folder on the commandline because it is good to know how
to do.

Windows has some specific commands for navigating folders (directories).

* cd - show the current directory
* cd `<directory>` - change directory to the provided directory
* dir - show a list of the directories in the current directory
* mkdir `<directory>` - create an empty directory with the given name

We want to navigate to 'Documents' and create a folder 'python' it
will probably look something like this:
```bash
dir 
cd Documents
mkdir python
cd python
```
 
we should now be in a python directory inside documents. This is
where we will put the git repo.

#### Cloning this repository

The first thing we are using git for is a way to download the
latest versions of the files stored here. This is called a 
'clone'. Clone will copy the current versions of the files as
well as the history of revisions that the files went through to
to get there latest forms.

on the main page of this repository on github.com there is a button
'clone or download'. click this and copy the url that comes up.

In the terminal in the python directory that we created run
git clone `<url>`
to paste the url into the terminal you can hit shift+insert

doing 
```bash
dir
```
should show the newly cloned repository. We did our first git thing
yay.


### Anaconda/Python

We setting up a python environment and installing packages to that 
environment. You can think of an environment as customizable 
version of python. All the packages and configurations for that
environment are saved to that environment alone.

Creating an environment ultimately yields a version of the python
interpreter that has all of the correct libraries installed.
Anaconda provides funtionality to manage/run multiple python 
environments.


#### Create a new python environment

1. open anaconda
2. Look at the tabs on the left. Click 'Environments'
3. One column over at the bottom of the screen click 'Create'
4. Check python
5. name it whatever you want
6. select '3.7' from the dropdown menu

#### Opening your environement

Anaconda is cool because of all the different ways you can
launch your environment. We are going to focus on the terminal.

1. hit the play button on the newly created environment.
2. click 'Open terminal'
	* this will open the windows command prompt
	* this particular window of the windows command prompt will 
	use the version of the python interpreter that we setup 
	in anaconda.

#### Pip

Pip is a package installer for python. The version of pip in the 
newly opened terminal will install packages to our python 
environment that we created in anaconda.

pip can install many packages at once. The packages are listed one
per line in 'requirements.txt' in this repository. 

The command to install all the packages:
```bash
pip install -r requirements.txt
```

now run this to see if everything worked:
```bash
python hi.py
```