56	"Event Parser private Connection conn;
 private ResultSet rs;
 private Statement stmt; //EventParser Constructor
 // initializes the Database connection
 public EventParser()
 {
try
{
 Class. forName("" sun. jdbc. odbc.JdbcOdbcDriver"");
 this. conn = DriverManager. getConnection("" jdbc: odbc: public void updateEvent(String str, String ID)
 {

String mProject;
String mEvent;
String mType;
String mNum;
String mrequirement ;
String mModule;
String mSQL;
String mDate;
String mReqtext;
//Check if a subscription exists
 public boolean CheckSubscription(String str)
 {

StringTokenizer tokens = new StringTokenizer( str, ""|"");
String Message type = tokens. nextToken();
String SubscriberName = tokens. next //Insert a subscription into the ""Subscription"" table
 public void AddSubscription(String str, int ID)
 {

// Parse the message string and get the fields

StringTokenizer tokens = new StringTokenizer( str, ""|"");
String Messag //DeleteSubscription from the ""Subscription"" table
 public void DeleteSubscription(String str, int ID)
 {
// Parse the message string and get the fields
StringTokenizer tokens = new StringTokenizer( str, ""|"");
String Messag //Speculate method will receive a string from the Speculative GUI
 // tool and parse it using CallBack class to identify the
 // performance models
 public void speculate(String str)
 {
System. out. println(""Speculate"");
CallBack public void impactReport(String str)
 {
CallBack cb = new CallBack();
cb. parseImpactReport( str);
 }// end impactReport()"
