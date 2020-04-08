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
    comm.isend(ready, dest=0, tag=mapTag).wait()

if rank == 0:
    links = getDictFromAdjList()
    reverseLinks = getLinksFromMapFiles()
    for i, link in enumerate(links):
        data = comm.irecv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG).wait()
        if data == ready:
            req = comm.isend(link, dest=status.Get_source(), tag=mapTag)
            req.wait()


    for link in reverseLinks:
        data = comm.irecv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG).wait()
        if data == ready:
            req = comm.isend(link, dest=status.Get_source(), tag=reduceTag)
            req.wait()
    data = comm.irecv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG).wait()
    req = comm.isend("", dest=status.Get_source(), tag=stopTag)
    req.wait()

else:
    while(condition):
        res = comm.irecv(source=0, tag=MPI.ANY_TAG)
        data = res.wait()
        tag = status.Get_tag()
        if tag == mapTag:
            map(data)
            comm.isend(ready, dest=0, tag=mapTag).wait()
        elif tag == reduceTag:
            result = reduce(data)
            if len(result) > 20:
                print(getLinkFromHash(data), end=" ")
                # print(result,end=" ")
                print(' rank: ' + str(len(result)))
            comm.isend(ready, dest=0, tag=reduceTag).wait()
        elif tag == stopTag:
            condition = False