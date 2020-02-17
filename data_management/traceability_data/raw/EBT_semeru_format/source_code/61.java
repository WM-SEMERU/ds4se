61	"Worker Thread /**
* True if this thread is currently processing.
 */
public boolean busy;
/**
 * The thread pool that this object belongs to.
 */
public ThreadPool owner; /**
 * The constructor.
 *
 * @param o the thread pool
 */
WorkerThread(ThreadPool o)
{
owner = o;
} /**
 * Scan for and execute tasks.
 */
public void run()
{
Runnable target = null;

do
{
target = owner. getAssignment();
if ( target!=null)
{
 target. run();
 owner. done. worker"
