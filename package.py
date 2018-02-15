name='ptex'
version='2.1.28'

def commands():
    env.CMAKE_PREFIX_PATH.append('{root}/cmake')
    env.DYLD_LIBRARY_PATH.append('{root}/lib')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/bin')
