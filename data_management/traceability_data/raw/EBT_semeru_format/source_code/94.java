94	"Refine Modelpublic RefineModel(EBT em)
{
super( em);
 } // Construct Visual model for Merge Event
public void BuildEvent()
{
 ClearVectors();
AddEventRect(60,80,1);
CurrentEvent = 3;
} public StringBuffer GenerateEvent()
{
StringBuffer thisEvent = new StringBuffer();
thisEvent. append(""Refine|0|"");
thisEvent. append( new Date(). toString()+""|"");
ebs = (EBShape)EventShapes. el"
