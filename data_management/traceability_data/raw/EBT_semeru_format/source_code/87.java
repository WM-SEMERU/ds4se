87	"EBTprivate JSplitPane splitPane;
private JSplitPane splitPane2;
private Frame FrameParent;
private JPanel MenuPanel;
private TextModel WorkArea;
private EventModel VisualPanel;
private MergeModel M public EBT(Frame f)
{

FrameParent = f;
CurrentEvent = -1;

this. serverIP =
 JOptionPane
. showInputDialog(""Please Enter the IP Address of eventserver"")
. trim();

 // Set up JList Selection wid public void getrequirement Text(EBShape sh)
{
WorkArea. showText( sh);
 } public boolean mouseDown( java. awt.Evente, int x, int y)
 {
 return true;
 }public boolean mouseUp( java. awt.Evente, int x, int y)
{
return true;
 } public void mouseClicked( java. awt. event.MouseEvente)
{
VisualPanel.Clicked( e. getX(), e. getY());
} public void mouseExited( java. awt. event.MouseEvente){} public void mousePressed( java. awt. event.MouseEvente){} public void mouseReleased( java. awt. event.MouseEvente){}public void mouseEntered( java. awt. event.MouseEvente){} public void paint(Graphics g) {} public void update(Graphics g) {} public JSplitPane getSplitPane()
{
return splitPane;
} public void valueChanged(ListSelectionEvent e)
{
if ( e. getValueIsAdjusting())
return;
} private class ValueReporter implements ListSelectionListener
{

public void valueChanged(ListSelectionEvent event)
{
 if (! event. getValueIsAdjusting())
 {
switch(EventList. getSelectedIndex())
public void RedrawAll(EBShape sh)
{
VisualPanel. drawModel( sh);
VisualPanel.CheckNotifyStatus();
} public static void main(String s[])
{
JFrame mainframe = new JFrame(""Trigger an Event Notification"");

mainframe. addWindowListener( new WindowAdapter()
{
public void windowClosing(Wind"
