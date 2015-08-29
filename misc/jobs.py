class Job:
  def __init__(self, name, runtime, frequency):
    self.name = name
    self.runtime = runtime
    self.frequency = frequency

def runJobs(jobs, maxJobs): 
  Q = []        # scheduled jobs (job, deadline)
  running = {} # running jobs: {finishTick: [jobs]}
  inflight = 0  # num currently job

  for job in jobs:
    Q.append((job, job.frequency))

  i = 0
  while i < 100:
    # Handled finished jobs.
    for j in running.get(i, set()):
      inflight -= 1
      print "TIME: %d: FINISH: %s" % (i, j.name)

    # Run more jobs.
    Q.sort(key = lambda (j, deadline): deadline)
    while inflight < maxJobs:
      (job, _) = Q.pop(0)
      print "TIME: %d: START: %s" % (i, job.name)
      inflight += 1

      # schedule next run
      Q.append((job, i + job.frequency))

      # store finish time
      finishTime = i + job.runtime
      runningJobs = running.get(finishTime, set())
      runningJobs.add(job)
      running[finishTime] = runningJobs

    i += 1

jobs = [
  Job('JobA', 2, 3),
  Job('JobB', 3, 6),
  Job('JobC', 1, 2)
]

runJobs(jobs, maxJobs=2)
