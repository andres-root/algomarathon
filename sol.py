


def pat(string, pattern):
    string = string.split()
    pattern = list(pattern)

    if len(string) != len(pattern):
        return False

    po = {}
    so = {}

    pl = []
    sl = []

    for i in range(len(string)):
        if string[i] not in so.keys():
            so[string[i]] = i + 1
        
        if pattern[i] not in po.keys():
            po[pattern[i]] = i + 1
        
    
    for e in string:
        sl.append(so[e])


    for e in pattern:
        pl.append(po[e])

    return(sl == pl)

pattern = 'abbab'
string = 'felipe luis luis felipe'

result = pat(string, pattern)

print(result)
