70	"Notification Processing // member variables for menu
 private JMenuBar menuBar;

 // subscriber list
 private JList SubscriberList;
 private DefaultListModel listModel;

 // popup menu

 private JPopupMenu popup;

 // database and eventserver information
 S public Notification_Processing()
 {

setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);

addWindowListener( new WindowAdapter()
{
 public void windowClosing(WindowEvent evt)
 {
try
public static void main(String args[])
 {
try
{
 Notification_Processing mainFrame = new Notification_Processing();
 mainFrame. setSize(600, 400);
 mainFrame. setLocation(100, 100);
 mainFrame. void exitApplication()
{
try
{
int reply = JOptionPane. showConfirmDialog( this,
""Do you really want to exit?"",
""No // action for ""Open log database""
 private void openMenuItemActionPerformed (ActionEvent evt)
 {
new ConfigDialog( this, true). show();

 if( m_DSN. equals("""") || m_EventServerIP. equals("""") || m_// action for ""Close log database""
 private void saveMenuItemActionPerformed (ActionEvent evt)
 {
try
{
 m_ conn. close();
 m_DSN="""";
 m_EventServerIP="""";
 m_EventServerPort="""";

 // action for "" exit""
 private void exitMenuItemActionPerformed (ActionEvent evt)
 {
exitApplication();
 } // action for ""Open Events"" in popup menu
 private void popupOpenActionPerformed (ActionEvent evt)
 {
openEventsMenuItemActionPerformed( evt);
 } // action for ""Open Events""
 private void openEventsMenuItemActionPerformed (ActionEvent evt)
 {
if (! listModel. isEmpty())
{
 int index = SubscriberList. getSelectedIndex();
 if ( index != -1)
 // action for "" double click on Subscriber List""
 private void doubleClickSubscriberList (MouseEvent evt)
 {
if (! listModel. isEmpty())
{
 int index = SubscriberList. getSelectedIndex();
 if ( index != -1 // action for ""About""
 private void aboutMenuItemActionPerformed (ActionEvent evt)
 {
new AboutDialog ( this, true). show();
 } void UpdateDisplayList()
 {
listModel. removeAllElements();

 String mSQL = ""SELECT distinct SubscriberName FROM EventDetails"";

try
{
 rs = stmt. executeQuery( mSQL);
 while ( rs. next())
 {
 "
