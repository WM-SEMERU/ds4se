63	"Doors Thread static private int count = 0;
 private int taskNumber;
 protected Done done;
 ServerSocket theServer;

 private Connection conn;
 private Statement stmt;
 private ResultSet rs; DOORsThread(ServerSocket ss)
 {
 theServer = ss;
 count++;
 taskNumber = count;
 } public void run()
 {

 while( true)
 {
 try
 {

Socket client = theServer. accept();
BufferedReader input = new BufferedReader( new InputStreamReader( client. getInputStream()));
PrintWriter output = new P"
