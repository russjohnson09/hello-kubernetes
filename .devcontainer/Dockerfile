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


RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

RUN source ~/.bashrc

RUN nvm list-remote

RUN nvm install v24.1.0

RUN nvm alias default v24.1.0

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
# CMD ["/bin/bash", "-c"]

#perl: warning: Falling back to the standard locale ("C").

#RUN curl -L https://cpanmin.us | perl - -M https://cpan.metacpan.org -n Mojolicious

# INSTALL PERL

#https://github.com/Tekki/docker-mojolicious
#https://mojolicious.io/blog/2017/12/01/day-1-getting-started/


#



# Install MariaDB client
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get install -y mariadb-client \ 
#     && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# # Install php-mysql driver
# RUN docker-php-ext-install mysqli pdo pdo_mysql

# # [Optional] Uncomment this section to install additional OS packages.
# # RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
# #     && apt-get -y install --no-install-recommends <your-package-list-here>

# # [Optional] Uncomment this line to install global node packages.
# # RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1


# prevent exit
#ENTRYPOINT ["tail", "-f", "/dev/null"]