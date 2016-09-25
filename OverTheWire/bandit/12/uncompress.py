#! /usr/bin/env python

def basenamify(name):
    return name.split('.')[0]


def uncompress_command(filename):
    from scriptine.shell import backtick as bt
    
    print("uncompressing %s", filename)

    while(True):
        fileres = bt('file ' + filename)
        fini = "ASCII" in fileres
        tar = "tar" in fileres
        gz = "gzip" in fileres
        bz = "bzip" in fileres

        basename = basenamify(filename)
        bt('mv ' + filename + ' ' + basename + '.in')
        filename = basename + '.in'

        if fini:
            print("Done! check " + filename)
        elif tar:
            print('tar archive')
            print('tar xf ' + filename + ' -O > ' + basename + '.out')
            bt('tar xf ' + filename + ' -O > ' + basename + '.out')
        elif bz:
            print('bzip')
            print('bzip2 -d ' + filename+ ' -c > ' + basename + '.out')
            bt('bzip2 -d ' + filename+ ' -c > ' + basename + '.out')
        elif gz:
            print('gzip')
            print('gzip -d ' + filename + ' -c > ' + basename + '.out')
            bt('gzip -d ' + filename + ' -c > ' + basename + '.out')
        filename = basename + '.out'

if __name__ == '__main__':
    import scriptine
    scriptine.run()
