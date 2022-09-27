FROM python:3.10-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_ROOT_WARNING 1

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # sql server dependencies
  # https://docs.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#debian10
  && ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends msodbcsql17 unixodbc-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # ldap dependencies
  && apt-get install -y libsasl2-dev libldap2-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Requirements are installed here to ensure they will be cached.
COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY start.sh start.sh
RUN sed -i 's/\r$//g' start.sh
RUN chmod +x start.sh

ENTRYPOINT ["bash", "start.sh"]
