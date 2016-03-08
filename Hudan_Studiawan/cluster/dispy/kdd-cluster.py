#!/usr/bin/env python

# run worker first: ./dispynode.py -d -i ip_address_worker
# run manager: ./kdd-cluster.py

def compute(centroids, row):    
    import operator
    from scipy.spatial.distance import euclidean        

    # measure distance    
    distance = []
    for c in centroids:
        d = euclidean(row, c)
        distance.append(d)

    # get maximum distance
    whatclass, distance = max(enumerate(distance), key=operator.itemgetter(1))    

    # get host name
    host = socket.gethostname()
    
    return whatclass, distance, host

if __name__ == '__main__':
    import dispy, random
    import csv
    import pickle

    # initiate cluster
    cluster = dispy.JobCluster(compute, nodes=['10.151.22.*'])
    jobs = []

    # read centroids
    f = open('centroids.csv', 'rb')
    centroids = pickle.loads(f.read())
    f.close()

    # read test data
    f = open('kddcup200new.csv', 'rb')
    rows = []
    reader = csv.reader(f)
    for row in reader:
        row = [float(r) for r in row]
        rows.append(row)        
    f.close()

    # distribute job to cluster member
    idx = 1
    for row in rows:
        job = cluster.submit(centroids, row)        
        job.id = idx
        idx = idx + 1
        jobs.append(job)
    
    # print result
    results = []
    for job in jobs:
        whatclass, distance, host = job()
        results.append((whatclass, distance))
        print '%s executed job %s at %s' % (host, job.id, job.start_time)
        
    cluster.stats()

    #for result in results:
    #    print result
