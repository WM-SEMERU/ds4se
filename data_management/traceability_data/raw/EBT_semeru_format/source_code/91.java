91	"Modify Model public ModifyModel(EBT em)
{
super( em);
 } // Construct Visual model for Merge Event
public void BuildEvent()
{
 ClearVectors();
AddEventRect(60,80,1);
CurrentEvent = 4;
} public StringBuffer GenerateEvent()
{
StringBuffer thisEvent = new StringBuffer();
thisEvent. append(""Modify|0|"");
thisEvent. append( new Date(). toString()+ ""|"");
 ebs = (EBShape)EventShapes protected void paintComponent(Graphics g)
{
g. drawString(""TESTING MODIFY"",5,5);
super. paintComponent( g);
 }"
