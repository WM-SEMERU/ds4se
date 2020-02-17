88	"Event Model 
protected Vector EventShapes = new Vector();
protected Vector EventLines = new Vector();
protected EB Shape ebs, ebs2;
protected EventLine mline;
protected Color ShapeColor = new Color (190,190,190);
 public EventModel(EBT e)
{
ebt = e;
CurrentEvent = -1;
NotifyButton = new JButton(""Notify"");
setLayout( null);
NotifyButton. setBounds(305,265,80,25);
MinimumNoRects = 1;

add public void getIP Server( String serverIP)
 {

this. serverIP = serverIP;
 } public void ClearVectors()
{
EventShapes. removeAllElements();
EventLines. removeAllElements();
}public void drawModel()
{
repaint();
} public void drawModel(EBShape sh)
{
EventShapes. setElementAt( sh, ESCursor);
repaint();
} private void ClearData()
{
for ( int i = 0; i < EventShapes. size(); i++)
{
ebs = (EBShape)EventShapes. elementAt( i);
ebs.Updaterequirement Info("""","""","""");
 }
}public void Clicked ( int x, int y)
{
int Hit = 0;
for ( int i = 0; i < EventShapes. size(); i++)
{
 ebs = (EBShape)EventShapes. elementAt( i);

if (( x >= ebs.GetX() && ( x <= ebs public void CheckNotifyStatus()
 {
//Check if Minimum Standards have been met.
int j = 0;
for ( j = 0; j < MinimumNoRects; j++)
{
ebs2 = (EBShape)EventShapes. elementAt( j);

 if (((((protected void BuildEvent(){} protected void AddLine( int t, int l, int r, int b)
{
EventLines. addElement( new EventLine( t, l, r, b));
} protected void AddEventRect( int x, int y, int colorStatus)
{
if ( colorStatus == 1)
{
 EventShapes. addElement( new EBShape( x, y, new Color (100,100,100)));
 }
 else
 {
Even public String getrequirement Text(String r, String p, String m)
{
return new String(""requirementwill go here"");
 } public StringBuffer GenerateEvent()
{
return new StringBuffer("" "");
 }// end of GenerateEvent method protected void paintComponent(Graphics g)
{
super. paintComponent( g);
for ( int i = 0; i < EventShapes. size(); i++)
{
ebs = (EBShape)EventShapes. elementAt( i);
 g. setC"
