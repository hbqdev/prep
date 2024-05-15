FROM python:3.8-slim
RUN pip install cog
ADD model.py /model.py
RUN cog run python /model.py