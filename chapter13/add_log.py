import logging

def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
        # level = logging.WARNING,
        # format = f'%(levelname)s:%(asctime)s:%(message)s'
    )

    host_name = 'www.python.org'
    item = 'spam'
    file_name = 'data.csv'
    mode = 'r'

    logging.critical(f'Host {host_name} unknown')
    logging.error(f"Couldn't find {item}")
    logging.warning('Feature is deprecated')
    logging.info(f'Opening file {file_name}, mode={mode}')
    logging.debug('Got here')

if __name__ == '__main__':
    main()


def config_call():
    import logging.config
    logging.config.fileConfig('log_config.ini')