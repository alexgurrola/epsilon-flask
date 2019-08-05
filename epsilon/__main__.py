def main():
    import argparse
    from . import __version__

    parser = argparse.ArgumentParser(description='RESTful API Boilerplate')
    parser.add_argument('-v', '--version', dest='version', action='version', version=__version__)
    parser.parse_args()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
