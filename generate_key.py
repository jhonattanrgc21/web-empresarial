''' Genera un SECRET_KEY aleatorio de 0 caracteres '''
import random

SECRET_KEY = ''.join(
    [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]
)

f = open(".env", "a")
f.write('\nSECRET_KEY = {}'.format(SECRET_KEY))
f.close()