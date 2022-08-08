# Compilation of my Learnings in PyQt5

## setup and installation Process

1. Created a virtual environment in my project folder and activated it.

```sh
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```

2. Updgraded python and updated pip

```sh
python3 -m pip install --upgrade pip
```

3. Tried installing PyQt5 in virtual environment and failed

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

4. Installed pyqt5 globally using homebrew

```sh
brew install pyqt@5
```

Although it beats the point of virtual environments, I found this to be the only way.
