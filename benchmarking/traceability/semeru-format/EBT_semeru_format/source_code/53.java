53	"Performance Modelprivate String name = null;
 private Vector driverVector = null;
 private Vector constraintVector = null;

 private long queryID = 0;

 public static int count = 0; public PerformanceModel(String name, long queryID)
 {
this. name = name;
this. queryID = queryID;

this. driverVector = new Vector();
this. constraintVector = new Vector();
 } public Vector getConstraints()
 {
return constraintVector;
 } public Vector getDrivers()
 {
return driverVector;
 } public String getName()
 {
return name;
 } public void setName(String name)
 {
this. name = name;
 } public void addDriver(DriverDescription driver)
 {

if ( driverVector. contains( driver))
{
}
else
 this. driverVector. add( driver);

 } public void removeDriver(DriverDescription driver)
 {
this. driverVector. remove( driver);
 } public boolean containsDriver(DriverDescription driver)
 {
return this. driverVector. contains( driver);
 } public void addConstraint(ConstraintsDescription constraint)
 {
this. constraintVector. add( constraint);
 } public boolean containsConstraint(ConstraintsDescription constraint)
 {
return this. constraintVector. contains( constraint);
 } public void removeConstraint(ConstraintsDescription constraint)
 {
this. constraintVector. remove( constraint);
 } public DriverDescription getDriver(DriverDescription driver)
 {
DriverDescription dd = null;

for ( int i = 0; i < this. driverVector. size(); i++)
{
 dd = (DriverDescription) this. driverVector. get( i) public ConstraintsDescription getConstraint(ConstraintsDescription constraint)
 {
ConstraintsDescription cd = null;

for ( int i = 0; i < this. constraintVector. size(); i++)
{
 cd = (ConstraintsDescription) thispublic long getQueryID()
 {
return this. queryID;
 } public void setQueryID( long id)
 {
this. queryID = id;
 } public String toString()
 {
return ""performance modelName = ""
 + this. name
 + ""\ n""
 + ""Query ID = ""
 + this. queryID
 + ""\ n""
 + ""Drivers = ""
 + this. driverVector
 + ""\ n""
 + ""Constraints = ""
 + this."
