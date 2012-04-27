def shift_and(T,P):
    
    text_length = len(T)
    pattern_length = len(P)

    if pattern_length > text_length: return -1
    if pattern_length == text_length: return 0
    if pattern_length == 1: return T.find(P)
    
    accept = 1 << (pattern_length - 1)
        
    #Build bitmask 
    ch_mask = [0] * 256
    for j in range(pattern_length):
        ch_mask[ord(P[j])] |= 1 << j 

    #Searching
    State = 0
    for i in range(text_length):
        State = ((State << 1) | 1) & ch_mask[ord(T[i])]
        if (State & accept) != 0:
            return i - pattern_length + 1
    return -1

if __name__ == '__main__':
    T = "pypythonpypypypypypy"
    P = "python"
    print "Text : ", T
    print "Pattern : ", P
    print "Occurrence : ",  shift_and(T, P)
