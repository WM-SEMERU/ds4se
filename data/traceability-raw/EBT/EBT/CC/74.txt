74	"database QueryConnection conn=null;
 ResultSet rs=null;
 Statement stmt=null;
 String mSQL="""";

 Vector structVector = new Vector(); // for holding the dummy variable objects used in executeStructure()
 Variable v;// create this object and /**
 * Construct a connection object.
 * @param Returns an object of type Connection
 */
 public Connection getConnection()
 {
System. out. println("" in get Connection"");
Connection connect=null;
try
{
 Class. fo /**
* Returns GraphId as int
* @param graphName performance modelHandler calls this method with graphName
* as parameter, performance modelHandler parse the EventServer message and get the
* graphName
*/
 public int get /**
* Copy data from one set of columns to other in table Variable
* @param graphId is the id of graph for which you want to save the
* current state of variables
*/
 public void saveCurrentModel( int graphId)
 {

conn = this. getConnect/**
* Injects new value into Variable table, using Data stored in
* Vector of Variable object
* @param graphId is the id of graph
* @param Vector var is the Vector that stores the Object of type Variable
*/
 public void injectVa /**
* this method will pick up the structure id from SPE Structure
* If DependentStructureId is 0 then select StructureID
* and invoke the executeStructure method on Selected
* StructureId
* Who Invokes this method: performance model // this method is about executing the structure
 // based on StructureId find all the data related to given StructureId
 // and using the equation in string format call the method equationParser.
 //I am passing Vector that has all the data abou public void solveStructure( int StructureId, Vector vr)
 {
System. out. println(""Inside solveStructure()&&&&&&&&&&&&&&&&&&&&&&&"");

Connection conn1 = this. getConnection();
System. out. println("" in solveStru public void solveStructureEquation()
 {
System. out. println(""Inside solveStructureEquation()%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"");

//Based on that result find out the equation and replace the name by its value
System public void getTrackVariableName()
 {
System. out. println(""Inside getTrackVariableName()$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"");
//This will get the variable name from SPE Graph and find the same name in variable
// and inse public void setCalculatedValues()
 {
System. out. println(""Inside setCalculatedValues()>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"");
// and at matching location put the calculated values
System. out. println("" enter calcValue // this method creates the token for each variable name in the string
 // and store that variable into vector
 // it also creates the vector called varValues
 // varValues has values of each variable stored in varName
 //So equation has variable n public Vector getImpactReport()
 {
//This SPE Graph works on the assumption that each model tracks
// the effect of changes on one variable
Vector report = new Vector();
report. add( trackVariableName);
report. add(Stri"
