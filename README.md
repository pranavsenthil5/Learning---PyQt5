# Compilation of my Learnings in PyQt5

## Setup and Installation Process

1. Created a virtual environment in my project folder and activated it.

```sh
python3 -m venv venv
# The last argument is the path to the virtual environment

source venv/bin/activate
```

2. Updated pip

```sh
python3 -m pip install --upgrade pip
```

3. Tried installing PyQt5 in virtual environment and failed

**[ If it works you are good to go ]**

```sh
pip install pyqt5
```

Some people also had the same issue, so I tried following the steps on [Stack Overflow](https://stackoverflow.com/questions/70961915/error-while-installing-pytq5-with-pip-preparing-metadata-pyproject-toml-did-n) and a billion other sites but they all failed.

I also tried [this](<https://peaku.co/questions/19480-error-while-installing-pytq5-with-pip:-preparing-metadata-(pyprojecttoml)-did-not-run-successfully>): I installed qt globally on my mac using homebrew, added the path to qmake in environment variables and tried installing pyqt5 again in the virtual environment. But, the last step failed.

```sh
brew install qt5
echo 'export PATH="/usr/local/opt/qt/bin:$PATH"' >> ~/.zshrc
```

[Building pyqt5](http://www.niladicpodcast.com/blog/2017/8/install-pyqt5-inside-a-virtual-environment/) might have been another option but I didn't want to get into that.

4. Installed pyqt5 globally using homebrew (the previous step is needed for this)

```sh
brew install pyqt@5
```

Although it beats the point of virtual environments, I found this to be the only way.

5. Allowed the virtual environment to access global packages ([Stack Overflow](https://stackoverflow.com/questions/25701133/how-to-tell-homebrew-to-install-inside-virtualenv#:~:text=What%20you%20can%20do%2C%20if,existing%20virtual%20environments%2C%20as%20well.))

```sh
python3 -m venv --system-site-packages venv
```
