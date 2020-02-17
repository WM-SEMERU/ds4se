67	"Event Detail Dialog private GridBagLayout grid bag;
private GridBagConstraints c;

// objects in top panel
private JPanel topPanel;
private JLabel modelLabel;
private JLabel typeLabel;
private JTextField modelField;
p public EventDetailDialog(EventsProcessor parent, boolean modal,Notification_Event nEvt, boolean mode)
{

super ( parent, modal);
 setTitle(""Event Details"");
 getContentPane (). setLayout (private void closeDialog(WindowEvent evt)
{
setVisible ( false);
dispose ();
} // event listener for ""Ok/Update"" button
private void okButtonActionPerformed (ActionEvent evt)
{

 if ( displayMode == true)
 {

// m_ parent.DeleteEvent( m_Evt. m_SubscriberName, m_ // event listener for ""Cancel"" button
private void cancelButtonActionPerformed (ActionEvent evt)
{
setVisible ( false);
dispose ();
} private void LeftListClicked(MouseEvent e){

 if (!LeftList. isSelectionEmpty()) {

 int index = LeftList. getSelectedIndex();
 Requirement requirement= (Requirement) m_Evt. m_LeftSideprivate void RightListClicked(MouseEvent e){

 if (!RightList. isSelectionEmpty()) {

 int index = RightList. getSelectedIndex();
 Requirement requirement= (Requirement) m_Evt. m_RightS"
