92	"New Modelpublic NewModel(EBT em)
{
super( em);
 } // Construct Visual model for Merge Event
public void BuildEvent()
{
ClearVectors();
AddEventRect(60,80,1);
AddArrow(35,97,59,97);
CurrentEvent = 0;
} public StringBuffer GenerateEvent()
{
StringBuffer thisEvent = new StringBuffer();
thisEvent. append(""New|0|"");
thisEvent. append( new Date(). toString()+ ""|"");
ebs = (EBShape)EventShapes. elem"
