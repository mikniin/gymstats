# gymstats

## Choise of poison

Initially, we started reading everything as just csv, this didn't get us very far.
Changed into depending upon pandas, which offers aggregations, grouping and some basic
data analysis tools out of the box.

For unit tests, opted for pytest

Architecture, started doing structure as a basic script, which evolved more into domain
driven design like structure. This can be converted into a format, where we'd be able to
add new data sources, different versions of same data (as long as the changes are not major)
and custom business logic (services)

## Environment

Personally I recommend on setting a virtual environment for running the project via
python3 -m venv <what ever path you like>
source <what ever path you typed>/bin/activate

## Installing dependencies

python 3.8 is required (would technically speaking work with older one, 3.5 is minimum)
pip3 -r requirements.txt

## Running

The script can be run with either python3 src/gymstats.py or cd src && ./gymstats.py
or the like.
