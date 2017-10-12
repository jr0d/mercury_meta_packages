import argparse


commands = [
    'inventory',
    'frontend',
    'backend',
    'log'
]


def arguments():
    parser = argparse.ArgumentParser(description='Mercury service launcher')
    parser.add_argument('command', choices=commands,
                        help='The service you would like to start')

    namespace, additional = parser.parse_known_args()

    print('command: {}'.format(namespace.command))


def main():
    arguments()


if __name__ == '__main__':
    main()