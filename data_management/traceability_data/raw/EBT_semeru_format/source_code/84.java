84	"White Board Execution Graph //Driver data members
 double avgShapeSize_Original;
 double avgShapeSize_Speculate;

 // constraints data members
 double avgTextSize;
 double writeTime;
 double noShapes;
 double noTextItems;
 double bandWidth public WhiteBoardExecutionGraph(Vector driver, Vector constraints){
this. driver = driver;
this. constraints = constraints;
 }// end of constructor public String toString(){
 String result;

 result = "" avgShapeSize_Original = "" + avgShapeSize_Original +
"",\ navgShapeSize_Speculate = "" + avgShapeSize_Speculate +
"",\ navgTextSize = "" + avgTextSizepublic void injectDrivers(){
System. out. println(""\ t\ tINSIDE INJECT DRIVERs METHOD"");
//To Do: Run for loop for more then one drivers
//To Do: have a case insensitive check for driver name and then populate the data member public void injectConstraints(){
System. out. println(""\ t\ tINSIDE INJECT CONSTRAINTs METHOD"");

//To Do: have a case insensitive check for constraints name and then populate the data member
//System. out. println( const public double timeToBroadcastShapeBefore(){
System. out. println(""\ t\ t\ tINSIDE timeToBroadcastShapeBefore METHOD"");

double targetResponse time_ temp = 0.00;

 for( int i=0; i< noShapes; i++ public double timeToBroadcastShapeAfter(){
System. out. println(""\ t\ t\ tINSIDE timeToBroadcastShapeAfter METHOD"");

double targetResponse time_ temp = 0.00;

 for( int i=0; i< noShapes; i++){ public double timeToBroadcastText(){
System. out. println(""\ t\ t\ tINSIDE timeToBroadcastText METHOD"");

double targetResponse time_ temp = 0.00;

 for( int i=0; i< noTextItems; i++){

 target public double writeTime(){
System. out. println(""\ t\ t\ tINSIDE writeTime METHOD"");

System. out. println(""\ t\ t\ t\ tTotal time to write = "" + writeTime);

System. out. println(""\ t\ t\ tLEAVING w public double targetResponseTimeBefore(){
System. out. println(""\ t\ tINSIDE targetResponseTimeBefore METHOD\ n"");

targetResponse time = timeToBroadcastShapeBefore() +
timeToBroadcastText()public double targetResponseTimeAfter(){
System. out. println(""\ t\ tINSIDE targetResponseTimeAfter METHOD\ n"");

targetResponse time = timeToBroadcastShapeAfter() +
timeToBroadcastText() + w"
