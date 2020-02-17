78	"Notification Event public String m_SubscriberName = """";
public String m_EventID = """";
public String m_Message type = """";
public String m_EventType = """";
public int m_NumberOfRequirements = 0;
public String m_EventTim // constructor
public Notification_Event()
{
 m_LeftSide = new ArrayList();
 m_RightSide = new ArrayList();
}// end of class Notification_Event public Object clone() throws CloneNotSupportedException
 {

// create new object with the same type
Notification_Event nEvt = (Notification_Event) super. clone();
 nEvt. m_LeftSide = new ArrayList();
 npublic void ParseEvent(String TextLine)
 {

String msg = TextLine;

if( msg. startsWith(""Re-execute"") )
{

 ModelDriver md = new ModelDriver( msg );
 md. init();

//ToDo:
// divert all the calls fo // Set the other members before calling this function

 public void ParseLeftAndRightLists(String LeftLine, String RightLine)
 {

m_LeftSide = new ArrayList();
 m_RightSide = new ArrayList();

if ( m_Eve //Comment Added by Amit Uchat
 //This method displays the contents of two array list to console
public void DisplayValues()
{
 System. out. println(""\ r\ nValues of the event:\ r\ n"");
 System. out. println("" "
