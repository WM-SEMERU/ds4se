90	"Merge Model public MergeModel(EBT em)
 {
super( em);
 MinimumNoRects = 3;
 } // Construct Visual model for Merge Event
public void BuildEvent()
{
 ClearVectors();
AddEventRect(90,220,1);
 AddEventRect(20,20,1);
AddEventRect(20,70,1);
AddEvent public StringBuffer GenerateEvent()
{
StringBuffer thisEvent = new StringBuffer();
StringBuffer temp = new StringBuffer();
int MergeCount = -1;
thisEvent. append(""Merge|"");

for ( int i = 0; i < EventSha"
