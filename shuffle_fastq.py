'''
    shuffle a fastq file
    speed code edition
    James M. Ferguson 2018
    
    python 2.7ish
    
    use:
        python shuffle_fastq.py my_lame.fastq > my_shiny_new.fastq
'''

import sys
from random import shuffle


fastq = sys.argv[1]

# quick and dirty way of ingesting fastq
count = 0
fq_dic = {}
with open(fastq, 'r') as fq:
    for line in fq:
        count += 1
        line = line.strip('\n')
        if count == 1:
            idx = line.split(' ')[0]
            fq_dic[idx] = [line]
        elif count < 5:
             fq_dic[idx].append(line)
             if count > 3:
                idx = ''
                count = 0
        
# Grab keys and shuffle
id_list = fq_dic.keys()
shuffle(id_list)

# Spit it all out
for x in id_list:
    print '{}\n{}\n{}\n{}'.format(fq_dic[x][0], fq_dic[x][1], fq_dic[x][2], fq_dic[x][3])

            
    
