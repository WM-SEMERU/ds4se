57	"Event Notifier // Variables to process the requirement
 private String requirement No;//Requirement No.
 private String ProjName; //Project name
 private String ModPath;//Modular path
 private String requirement Text;/ public EventNotifier(String rno, String proj, String mod, String rtext,String eID, String em, String eventType)
 {
requirement No = rno;//Requirement number
ProjName = proj;// project name
ModPath = mo // finds the subscribers for this requirement
 public void IdentifySubscribers()
 {
String mSQL;
// Create an SQL statement that will limit the selection as much as possible
// If a subscription is to a specific requirement - check for requi //Reads the result from IdentifySubscribers method selection
 // and adds each result into ActualSubscribers Vector.
 void ProcessResultSet()
 {

String sName, sReqno, sModule, sKey1, sKey2;
try
{
 System. o // Send messages to all subscribers listed in ActualSubscriber Vector
// Possible that a sort routine can be added later so that all notification to
// the same subscribermanager can be batched.This is not implemented yet.

 public void Dispatch public String getErrorMessage()
 {
 return errMsg;

 } public boolean Contains(String ContextString, String SearchString)
 {
int cLen = ContextString. length();
int sLen = SearchString. length();
if (SearchString. length() == 0)
 return false;

for ( int i = 0"
