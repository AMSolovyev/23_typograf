# Typograf Service

The typograf prepares your text for web-publish.
It does the most routine operations, for example:
- replacement of quotes ' and " to « »;
- in the right places, replace hyphens with dashes;
- replacement of hyphens with short dashes in telephone numbers;
- linking numbers with subsequent words with an indissoluble space;
- removing extra spaces and line breaks;
- linking any words of 1-2 characters followed by words.

# How to use

```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python server.py.

```

Open [http://localhost:5000/](http://localhost:5000/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)