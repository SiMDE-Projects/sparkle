ARG BASE=builder

FROM python:3.8-buster AS builder
MAINTAINER Cesar Richard <cesar.richard2@gmail.com>

ENV PYTHONUNBUFFERED 1

# Setup working directory
RUN mkdir -p /code /home/sparkle/.ssh /static
WORKDIR /code

# Setup user
RUN groupadd -r sparkle && useradd -r -g sparkle sparkle

# Install tmate for shells
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev --no-install-recommends && rm -r /var/lib/apt/lists/*

# Setup SSH KEY for tmate
RUN ssh-keygen -b 2048 -t rsa -f /home/sparkle/.ssh/id_rsa -q -N ""
RUN chown sparkle:sparkle -R /home/sparkle

# Install uwsgi
RUN pip install --no-cache-dir uwsgi

# Install sparkle requirements (doing this before copying code improves caching)
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Uwsgi runs on port 8000
EXPOSE 8000

#COPY --from=front_builder /code/node_modules.bin.txt /code/node_modules.bin.txt

# Add code
ADD . /code/

# Collect static files
RUN SPARKLE_DJANGO_SECRET=whatever python manage.py collectstatic --noinput --clear

# Switch to unprivileged user
USER sparkle

# Run uwsgi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
