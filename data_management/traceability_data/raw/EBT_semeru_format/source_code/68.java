68	"Events Processor // event list
 private JList eventList;
 private DefaultListModel listModel;
 private ArrayList events;

 // popup menu
 private JPopupMenu popup;

 // Subscriber name
 String m_SubscriberName;

 // list of requirements to be d public EventsProcessor(Notification_Processing parent, boolean modal, String SubsName)
 {

 setTitle(""EventsProcessor"");

addWindowListener( new WindowAdapter()
{
 public void windowClosing(WindowEve void exitApplication() {
m_ parent.UpdateDisplayList();
 this. setVisible( false);
 this. dispose();
} // action for "" double click on Event List""
 private void doubleClickEventList (MouseEvent evt)
 {

int index = eventList. getSelectedIndex();
if ( index != -1)
{
 try
 {
Notification // action for ""Open First Record"" in popup menu
 private void popupOpenActionPerformed (ActionEvent evt)
 {
if (! listModel. isEmpty())
{
 int index =0;
 try
 {
Notification_Event nEvt1 = (Notificati / action for ""View Current Record"" in popup menu
 private void popupViewActionPerformed (ActionEvent evt)
 {
int index = eventList. getSelectedIndex();
if ( index != -1)
{
 try
 {
N void DeleteEvent(String SubscriberName, String EventID)
 {

try
{

 int i, j=-1;
 for ( i=0; i< events. size(); i++)
 {
Notification_Event nEvt = (Notification_Event) events. get( i);
i void DeleteRelatedEvents()
 {

while ( m_Deleterequirement List. size()!=0)
{

 Requirement requirement= (Requirement)( m_Deleterequirement List. get(0));

 m_Deleterequirement List. remove(0);
void AddSubscription(String SubscriberName, Requirement requirement )
 {

String SubscriberDependency = ""Requirements"";

String Message = ""ADD_SUBSCRIPTION""+""|"";
Message += m_UserName + ""|"";
Message += Subscribervoid DeleteSubscription(String SubscriberName, Requirement requirement )
 {
String Message = ""REMOVE_SUBSCRIPTION""+""|"";
Message += SubscriberName + ""|"";
Message += requirement . m_RequirementID + "","";
Message += req void UpdateDisplayList()
 {

listModel. removeAllElements();

for ( int j=0; j< events. size(); j++)
{

 Notification_Event nEvt = (Notification_Event) events. get( j);

 String displayStri // Passes a CHECK_SUBSCRIPTION message to the eventserver and waits for a response
private boolean Check_Subscription(String ip,
 int PortNo,
 String SubscriberName,
 String Requirement // Takes an event string returned from the eventserver and
// extracts True or False response
private boolean Analyze_CheckSubscription(String str)
{
StringTokenizer tokens = new StringTokenizer( str,""|"");
String Messag"
