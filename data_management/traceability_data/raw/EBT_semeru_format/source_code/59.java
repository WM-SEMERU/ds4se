59	"Done /**
* The number of Worker object
* threads that are currently working
* on something.
*/
 private int _ activeThreads = 0;

 /**
* This boolean keeps track of if
* the very first thread has started
* or not. This prevents this objec /**
* This method can be called to block
* the current thread until the ThreadPool
* is done.
*/

 synchronized public void waitDone()
 {
try {
 while ( _ activeThreads>0 ) {
wait();
 }
} catch ( InterruptedException/**
* Called to wait for the first thread to
* start. Once this method returns the
* process has begun.
*/

 synchronized public void waitBegin()
 {
try {
 while ( !_ started ) {
wait();
 }
} catch ( InterruptedException e/**
* Called by a Worker object
* to indicate that it has begun
* working on a workload.
*/
 synchronized public void workerBegin()
 {
_ activeThreads++;
_ started = true;
notify();
 } /**
* Called by a Worker object to
* indicate that it has completed a
* workload.
*/
 synchronized public void workerEnd()
 {
_ activeThreads--;
notify();
 } /**
* Called to reset this object to
* its initial state.
*/
 synchronized public void reset()
 {
_ activeThreads = 0;
 }"
