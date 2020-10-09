from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('test.ini')

print(f'sections is: {cfg.sections()}')
print(f"library is: {cfg.get('installation','library')}")
print(f"log errors: {cfg.getboolean('debug','log_errors')}")
print(f"port is: {cfg.getint('server','port')}")
print(f"nworkers is: {cfg.getint('server','nworkers')}")
print(f"signature is: {cfg.get('server','signature')}")


cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')

print(f"new debug is: {cfg.getboolean('debug','log_errors')}")
print(f"After change,port is: {cfg.getint('server','port')}")


print(cfg.get('installation','PREFIX'))
print(cfg.get('installation','prefix'))