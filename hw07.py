# Problem A.
def cg_pairs(dna):
    '''
    Purpose: To take a string of DNA and return the ratio
    of amount of CG pairs present

    Parameter: A DNA string

    Return Value: The ratio of amount of CG pairs present
    '''
    dna = dna.lower()
    cg_num = 0
    pair_num = 0
    for i in range(len(dna)-1):
        if dna[i] not in 'actg':
            print('Error in DNA strand')
            return 0.0
        elif dna[i:i+2] == 'cg':
            cg_num += 1
        pair_num += 1
    return float(cg_num)/pair_num

# Problem B.
def segment(dna, num):
    '''
    Purpose: To split up a DNA strand either by reading frame
    0, 1, or 2

    Parameters: A DNA string and a frame number

    Return Value: A string of DNA split based on the frame number
    '''
    frame = []
    if num == 0:
        for i in range(0,len(dna),3):
            frame = frame + [dna[i:i+3]]
        return frame
    elif num == 1:
        frame = frame + [dna[:1]]
        for i in range(1,len(dna),3):
            frame = frame + [dna[i:i+3]]
        return frame
    elif num == 2:
        frame = frame + [dna[:2]]
        for i in range(2,len(dna),3):
            frame = frame + [dna[i:i+3]]
        return frame
    else:
        print("u can't use that number, silly!")

# Problem C.
def mark_dna(dna, seq):
    '''
    Purpose: To find and mark a specific dna sequence within
    a longer one

    Parameters: A DNA string and a smaller DNA sequence

    Return Value: A string of DNA with arrows marking where
    the smaller sequences are found
    '''
    final = ''
    index = 0
    while index < len(dna):
        if dna[index:index+len(seq)] == seq:
            final += ">>" + seq + "<<"
            index += len(seq)
        else:
            final += dna[index:index+1]
            index += 1
    return final

#Problem D.
def find_url(html):
    '''
    Purpose: To find an URL within html text and return it

    Parameters: A string of html text

    Return Value: The URL within the string
    '''
    URL = ''
    fq = html.find('href="') + 6
    lq = html.find('"',fq)
    URL = URL + html[fq:lq]
    return URL
