from mpi4py import MPI
from folder import getDictFromAdjList
from map import map

# source = status.Get_source()
# tag = status.Get_tag()

mapTag = 18
reduceTag = 12
stopTag = 13
ready = 14

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()


if rank != 4:
    comm.send(ready, dest=4, tag=mapTag)

if rank == 4:
    links = getDictFromAdjList()
    for i, link in enumerate(links):
        data = comm.recv(source=MPI.ANY_SOURCE, tag=mapTag, status=status)
        if data == ready:
            req1 = comm.send(link, dest=i, tag=mapTag)

        if i == 3: break

else:
    res = comm.recv(source=4, tag=MPI.ANY_TAG, status=status)
    source = status.tag
    print(source)

    tag = status.Get_source()

    # map(data)
    # comm.isend(ready, dest=0, tag=mapTag).wait()
