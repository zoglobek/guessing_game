FROM python:3.13-alpine


COPY main.py /guess_game/.
COPY messages.py /guess_game/.
COPY logic.py /guess_game/.
COPY functions.py /guess_game/.
COPY README.md /guess_game/.
COPY __init__.py /guess_game/.




