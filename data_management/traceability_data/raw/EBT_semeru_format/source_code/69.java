69	"Notification Event public String m_SubscriberName = """";
public String m_EventID = """";
public String m_Message type = """";
public String m_EventType = """";
public int m_NumberOfRequirements = 0;
public String m_EventTim public Notification_Event()
{
 m_LeftSide = new ArrayList();
 m_RightSide = new ArrayList();
} public Object clone() throws CloneNotSupportedException
 {

Notification_Event nEvt = (Notification_Event) super. clone();
 nEvt. m_LeftSide = new ArrayList();
 nEvt. m_RightSide = new ArrayLis public void ParseEvent(String TextLine)
 {

 StringTokenizer LineSt; // Tokenizer for the line

int i=0;

LineSt = new StringTokenizer(TextLine, ""|"");

m_SubscriberName = LineSt. nextToken// Set the other members before calling this function

 public void ParseLeftAndRightLists(String LeftLine, String RightLine)
 {

m_LeftSide = new ArrayList();
 m_RightSide = new ArrayList();

if ( m_Eve public void DisplayValues()
{
 System. out. println(""\ r\ nValues of the event:\ r\ n"");
 System. out. println("" m_SubscriberName: ""+ m_SubscriberName);
 System. out. println("" m_EventI"
