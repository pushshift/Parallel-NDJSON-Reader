#!/usr/bin/env python3
import os.path, io
import multiprocessing as mp
import ujson as json

n_chunks = 12  # Number of processes to use -- will split the file up into this many pieces
filename = '/data/file/path'

def worker(start,end):

    f = io.open(filename,'r',encoding='utf-8')
    counter = 0
    f.seek(start)
    total_len = 0
    for line in f:
        counter+=1
        j = json.loads(line)
         # Do stuff with data here
        ...
        total_len += len(line)
        if (total_len+start) >= end: break

def find_newline_pos(f,n):
    f.seek(n)
    c = f.read(1)
    while c != '\n' and n > 0:
        n-=1
        f.seek(n)
        c = f.read(1)
    return(n)

def prestart():
    fsize = os.path.getsize(filename)
    pieces = []   # Holds start and stop position of each chunk
    initial_chunks=list(range(0,fsize,int(fsize/n_chunks)))[:-1]
    f = io.open(filename,'r',encoding='utf-8')
    pieces = sorted(set([find_newline_pos(f,n) for n in initial_chunks]))
    pieces.append(fsize)
    args = zip([x+1 if x > 0 else x for x in pieces],[x for x in pieces[1:]])
    return(args)

args = prestart()

workers = [mp.Process(target=worker, args=(start,end)) for start,end in list(args)]

def main():
    for worker in workers:
        worker.start()

if __name__ == '__main__':
    main()
