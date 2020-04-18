def vec_print ( n, a, title ):

    print ' '
    print title
    print '\n'
    for i in range(n):
        print '%6d:  %10f' % (i,a[i])
    return
