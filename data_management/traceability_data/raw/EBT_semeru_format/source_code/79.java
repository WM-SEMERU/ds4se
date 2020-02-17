79	"performance model Handler String strES; // string received from eventserver
 String impactReport;// string to be send to eventServer

 String commandStr; // represent the command ex. execute, re - execute etc
 String eventId;// refers to the eventId
 String performance model Handler(String msg)
 {
this. strES = msg;
 } public void messageParser()
 {
System. out. println(""INSIDE PARSER"");

mainSto = new StringTokenizer( strES,""|""); // current ex will have 10 tokens in mainSto


tempStr1 = mainSto. nextToken();
//Re-execut public String generateReport()
{
 System. out. println(""INSIDE generateReport"");

 mainSto = new StringTokenizer( strES,""|""); // current ex will have 10 tokens in mainSto
 /*
""ImpactReport|1015818161020| int grId; public int getId(){
 // get GraphId
 System. out. println(""database start"");
 int grId = database. getGraphId( modelName);
 return grId;
 } public void saveModel( int id)
 {
// save current model
database. saveCurrentModel( id);
 } public void insertData( int id){
// inject data into model
database. injectVariables( id, variable);
 } public void execute( int id){
// inject data into model
database. executeModel( id, variable);
 }"
