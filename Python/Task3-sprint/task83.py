import zlib
import bz2

def comptest(s):
    print( 'original length:', len(s))
    print( 'zlib compressed length:', len(zlib.compress(s)))
    print( 'bz2 compressed length:', len(bz2.compress(s)))


comptest(b'asfsfcws wefwef eferge'.decode('utf-8'))