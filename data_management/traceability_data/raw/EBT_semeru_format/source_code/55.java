55	"eventserver Threadstatic private int count = 0;
 private int taskNumber;
 protected Done done;
 ServerSocket theServer;

 private Connection conn;
 private Statement stmt;
 private ResultSet rs;

 private EventParser ep;
 private int id; EventServerThread(ServerSocket ss)
 {
 theServer = ss;
 count++;
 taskNumber = count;
 ep = new EventParser();
 } public void run()
 {

 while( true)
 {
 try
 {

Socket client = theServer. accept();
BufferedReader input = new BufferedReader( new InputStreamReader( client. getInputStream()));
PrintWriter output = new P public String getNextID()
 {

try
{
Class. forName("" sun. jdbc. odbc.jdbcodbcDriver"");
this. conn = DriverManager. getConnection("" jdbc: odbc:EBT"",""EBT"",""EBT"");
this. stmt = connpublic String searchDate()
 {

String dateString = new String();
Vector dateVector = new Vector();

try
{

 Class. forName("" sun. jdbc. odbc.jdbcodbcDriver"");
 Connection conn = DriverManager. getConnectio public String searchQueryID(String date)
 {
Vector queryVector = new Vector();

String searchQuery = new String();

try
{
 Class. forName("" sun. jdbc. odbc.JdbcOdbcDriver"");
 conn = DriverManager. getpublic String getConstraintFromDataBase(String queryID)
 {

String ConstString = new String();


try
{

 Class. forName("" sun. jdbc. odbc.JdbcOdbcDriver"");

 conn = DriverManager. getConnection("" j public String getDriverFromDataBase(String queryID)
 {

String driverString = new String();

try
{

 Class. forName("" sun. jdbc. odbc.JdbcOdbcDriver"");

 conn = DriverManager. getConnection("" jdbc "
