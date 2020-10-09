from chapter10.modify_module import imported_action

@imported_action('threading')
def warn_threads(mod):
    print('Call Threads.')

import threading