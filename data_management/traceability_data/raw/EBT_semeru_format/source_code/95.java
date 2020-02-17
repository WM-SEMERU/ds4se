95	"Text Model private int CurrentEvent;
private EBT ebt;
private JLabel lblrequirement No, lblProject, lblModulePath;
private JTextField txtrequirement No, txtProject, txtModulePath;
private boolean HideMsg;
p public TextModel(EBT e)
{
 // System. out. println(""Trying to create text box"");
ebt = e;
CurrentEvent = -1;
// setForeground( new Color ( 255,255,255) );
 lblrequirement No = new JLabel(""requirement public void showText(EBShape sh)
{
 // Hide message in bottom box.
 HideMsg = true;
 repaint();
lblProject. setVisible( true);
lblrequirement No. setVisible( true);
lblModulePath. set public void HideText()
{
lblProject. setVisible( false);
lblrequirement No. setVisible( false);
lblModulePath. setVisible( false);
txtProject. setVisible( false);
txtrequirement No. setVisi public void ShowInfo( int CE)
{
CurrentEvent = CE;
HideMsg = false;
HideText();
 repaint();
} public void drawModel()
{
repaint();
} protected void paintComponent(Graphics g)
{
 super. paintComponent( g);

if (HideMsg == true)
{
 g. drawString("" "",20,25);
 g. drawString("" "",20,40);
 g. drawString("" "",20,55 "
