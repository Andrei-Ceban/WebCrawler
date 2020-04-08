from mpi4py import MPI
from folder import getDictFromAdjList, getLinksFromMapFiles
from map import map
from reduce import reduce
from folder import getLinkFromHash

# source = status.Get_source()
# tag = status.Get_tag()

mapTag = 11
reduceTag = 12
stopTag = 13
ready = 14

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()
condition = True

if rank != 0:
    comm.send(ready, dest=0, tag=mapTag)

if rank == 0:
    reverseLinks = getLinksFromMapFiles()
    links = getDictFromAdjList()

    for i, link in enumerate(links):
        data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        if data == ready:
            comm.send(link, dest=status.source, tag=mapTag)


    for link in reverseLinks:
        data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
        if data == ready:
            comm.send(link, dest=status.source, tag=reduceTag)

    data = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
    if data == ready:
        comm.send("", dest=status.source, tag=stopTag)


else:
    while(condition):
        data = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
        tag = status.tag
        if tag == mapTag:
            map(data)
            comm.send(ready, dest=0, tag=mapTag)
        elif tag == reduceTag:
            result = reduce(data)
            # if len(result) > 0:
            print(data, end=" ")
            # print(result,end=" ")
            print(' rank: ' + str(len(result)))
            comm.send(ready, dest=0, tag=reduceTag)
        elif tag == stopTag:
            condition = False
            print('Aici')
print(rank)