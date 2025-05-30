#FROM mcr.microsoft.com/devcontainers/php:1-8.2-bookworm

#FROM ubuntu:plucky
FROM perl:5.40.2

#RUN apt-get update

#RUN apt-get install curl -y

WORKDIR /usr/src/app


EXPOSE 3000 8080

RUN groupadd --gid 1000 perl \
  && useradd --uid 1000 --gid perl --shell /bin/bash --create-home perl

RUN set -ex \
  && apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    dirmngr \
  && cpanm \
    Cpanel::JSON::XS \
    CryptX \
    DBI \
    EV \
    Future::AsyncAwait \
    IO::Socket::Socks \
    Net::SSLeay \
    IO::Socket::SSL \
    Net::DNS::Native \
    Role::Tiny \
    SQL::Abstract \
  && rm -r /var/lib/apt/lists/* \
  && rm -r /root/.cpanm

ENV MOJO_VERSION=9.40

RUN cpanm Mojolicious@"$MOJO_VERSION" \
  && rm -r /root/.cpanm

RUN set -ex \
  && export GNUPGHOME="$(mktemp -d)" \
  && for key in \
    177F4010FE56CA3336300305F1656F24C74CD1D8 \
    430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \
    4D1BB29D63D98E422B2113B19334A25F8507EFA5 \
  ; do \
    gpg --batch --keyserver hkp://keys.opengpg.org --recv-keys "$key" || \
    gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \
    gpg --batch --keyserver hkp://keyserver.ubuntu.com --recv-keys "$key" ; \
  done \
  && gpg --batch --export 177F4010FE56CA3336300305F1656F24C74CD1D8 430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A 4D1BB29D63D98E422B2113B19334A25F8507EFA5 > /etc/apt/trusted.gpg.d/mariadb.gpg \
  && command -v gpgconf > /dev/null && gpgconf --kill all \
  && rm -rf "$GNUPGHOME" \
  && add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/11.1/debian bookworm main' \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    libmariadb-dev \
  && rm -r /var/lib/apt/lists/*

ENV DBD_MYSQL_CONFIG=mariadb_config

RUN cpanm DBD::MariaDB Mojo::mysql \
  && rm -r /root/.cpanm

ARG NOW=not-set
LABEL org.opencontainers.image.authors="Tekki <tekki@tekki.ch>"
LABEL org.opencontainers.image.created=$NOW
LABEL org.opencontainers.image.description="Mojolicious is a real-time web framework and web development toolkit written in Perl."
LABEL org.opencontainers.image.documentation=https://github.com/Tekki/docker-mojolicious/blob/master/README.md
LABEL org.opencontainers.image.licenses=Artistic-2.0
LABEL org.opencontainers.image.source=https://github.com/Tekki/docker-mojolicious/blob/master/mariadb/Dockerfile
LABEL org.opencontainers.image.title=Mojolicious
LABEL org.opencontainers.image.url=https://github.com/Tekki/docker-mojolicious
LABEL org.opencontainers.image.version=9.40-mariadb


#RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

#RUN source ~/.bashrc

#ENV NVM_DIR /usr/local/nvm

#ENV NVM_DIR=/usr/bin
#RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

#RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

#RUN . "$NVM_DIR/nvm.sh" && nvm install 6.9.1
#https://github.com/moby/moby/issues/30066
#RUN . "$NVM_DIR/nvm.sh"

#/bin/sh: 1: source: not found
#RUN source $NVM_DIR/nvm.sh

#RUN nvm list-remote

#RUN nvm install v24.1.0

#RUN nvm alias default v24.1.0

# or ~/.nvm , depending
#ENV NVM_DIR /usr/local/nvm 

#ENV NVM_DIR ~/.nvm

#usr/local/bin/perl
ENV NVM_DIR /root/.nvm

ENV NODE_VERSION v24.1.0

RUN curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh  | bash \
    # && . $NVM_DIR/nvm.sh \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
# ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH


RUN cpanm Test::Needs --force
RUN cpanm JSON::MaybeXS

RUN cpanm Try::Tiny --force

RUN cpanm Test::Fatal


RUN cpanm Test2
RUN cpanm IPC::Run3 --force
RUN cpanm Test2::Plugin::NoWarnings
RUN cpanm Params::ValidationCompiler
RUN cpanm DateTime

RUN cpanm GraphQL::Schema

RUN cpanm Mojolicious::Plugin::GraphQL

RUN cpanm GraphQL




ENTRYPOINT ["tail", "-f", "/dev/null"]