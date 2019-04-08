#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# Project name: OpenVAS Reporting Server: Automatically receive and parse OpenVAS XML reports using OpenVAS Reporting.
# Project URL: https://github.com/TheGroundZero/openvasreporting_server

import argparse
import os
import socket
import tempfile

from openvasreporting import openvasreporting


def main():
    parser = argparse.ArgumentParser(
        prog='OpenVAS Reporting Server',
        description='Automatically receive and parse XML reports from finished tasks',
        allow_abbrev=True
    )
    parser.add_argument('-i', '--ip', dest='ip', required=False, default='127.0.0.1',
                        help='IP this server will listen on')
    parser.add_argument('-p', '--port', dest='port', required=False, default=8081,
                        help='Port this server will listen on')
    parser.add_argument('-f', '--format', dest='format', required=False, default='xlsx',
                        help='OpenVAS Reporting format to parse the report into')

    args = parser.parse_args()

    openvasreporting.check_filetype(args.format)

    setup_socket(args.ip, args.port, args.format)


def setup_socket(host, port, report_format):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, int(port)))
        print('Server started on {}:{}'.format(host, str(port)))
        print('Will create reports in {} format'.format(report_format))

        s.listen(5)

        while True:
            conn, addr = s.accept()

            file = create_temp_file()
            print('Temp file creates at: {}'.format(file))

            with conn:
                print('Connected by: {}'.format(addr))
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    print('Received data, writing to temp file at: {}'.format(file))
                    write_to_file(file, data)

                    report = '{}/openvas_report_{}'.format(os.getcwd(), file)
                    print('Writing report to: {}.{}'.format(report, report_format))
                    config = openvasreporting.create_config([file], report, filetype=report_format)
                    openvasreporting.convert(config)

            print('Connection closed')
            os.remove(file)


def create_temp_file():
    fd, path = tempfile.mkstemp(suffix='.xml')
    return path


def write_to_file(file, data):
    with open(file, 'ab') as f:
        f.write(data)


if __name__ == '__main__':
    main()
