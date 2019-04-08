# OpenVAS Reporting Server:  

A tool to automatically receive and convert [OpenVAS](http://www.openvas.org/) XML into reports.


## Requirements

 - [Python](https://www.python.org/) version 3
 - [OpenVAS Reporting](https://github.com/TheGroundZero/openvasreporting)


## Installation

    # install requirements
    apt(-get) install python3 python3-pip # Debian, Ubuntu
    yum -y install python3 python3-pip    # CentOS
    dnf install python3 python3-pip       # Fedora
    pip3 install -r requirements.txt
    # clone repo
    git clone git@github.com:TheGroundZero/openvasreporting_server.git


## Usage

    # When working from the Git repo
    python3 ./server.py -i [OpenVAS xml file(s)] [-o [Output file]] [-f [Output format]] [-l [minimal threat level (n, l, m, h, c)]] [-f [docx template]]


### Parameters

| Short param | Long param | Description     | Required | Default value |
| :---------: | :--------- | :-------------- | :------: | :------------ |
| -i          | --ip       | Listener IP     | No       | 127.0.0.1     |
| -p          | --port     | Listener Port   | No       | 8081          |
| -f          | --format   | Output format   | No       | xlsx          |


## Examples

### Start listener with default settings

    > python3 server.py 
    Server started on 127.0.0.1:8081
    Will create reports in xlsx format

### Start listener with custom settings

    > python3 server.py -i 127.0.0.2 -p 4321 -f docx
    Server started on 127.0.0.2:4321
    Will create reports in docx format