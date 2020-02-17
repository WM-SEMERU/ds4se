60	"Thread Pool /**
* The threads in the pool.
*/
protected Thread threads[] = null;
/**
* The backlog of assignments, which are waiting
* for the thread pool.
*/
Collection assignments = new ArrayList(3);
/**
* A Done object that is /**
 * The constructor.
 *
 * @param sizeHow many threads in the thread pool.
 */
public ThreadPool( int size)
{

threads = new WorkerThread[ size];

for ( int i=0; i< threads. length; i++)
{
thr /**
* Add a task to the thread pool. Any class
* which implements the Runnable interface
* may be assigned. When this task runs, its
* run method will be called.
*
* @param r An object that implements the Runnable interface
*/
 pub /**
* Get a new work assignment.
*
* @return A new assignment
*/
 public synchronized Runnable getAssignment()
 {
try {
 while ( ! assignments. iterator(). hasNext() )
wait();

 Runnable r = (Runnable) assignments./**
* Called to block the current thread until
* the thread pool has no more work.
*/
 public void complete()
 {
done. waitBegin();
done. waitDone();
 } protected void finalize()
 {
done. reset();
for ( int i=0; i< threads. length; i++) {
 threads[ i]. interrupt();
 done. workerBegin();
 threads[ i]. destroy();
}
done. waitDone();
 }
}"
