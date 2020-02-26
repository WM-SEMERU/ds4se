83	"Variable String id = """"; // requirement id ex WB10
 String type= """"; // type of requirement ex Driver or Constraints
 String name= """"; // requirement name which is same as variable name in graph
 double value= 0.0; // value of variable
 double speculat //General Constructor to initialize all the members
 Variable(String id, String type, String name, double value, double speculateValue, String logic, String project_ path)
 {
this. id = id;
this. type = type;
this.//Constructor to Add driver related members
 Variable(String id, String type, String name, double value, double speculateValue)
 {
this. id = id;
this. type = type;
this. name = name;
this. value = value;
this //Constructor to Add constraints related members
 Variable(String id, String type, String name, double value, String logic){
this. id = id;
this. type = type;
this. name = name;
this. value = value;
this. logicpublic String toString()
 {
String temp;
temp = ""ID = "" + id + "", Type = "" + type + "", Name = "" + name +"", value = "" + value +
 "", SpeculateValue = "" + speculateValue + "", Logic = "" + logic + "", Project_Path = "" + project_ path /**
* Returns the id.
* @return int
*/
 public String getId()
 {
return id;
 } /**
* Returns the logic.
* @return String
*/
 public String getLogic()
 {
return logic;
 } /**
* Returns the name.
* @return String
*/
 public String getName()
 {
return name;
 } /**
* Returns the value.
* @return double
*/
 public double getValue() {
return value;
 } /**
* Sets the id.
* @param id The id to set
*/
 public void setId(String id) {
this. id = id;
 } /**
* Sets the logic.
* @param logic The logic to set
*/
 public void setLogic(String logic) {
this. logic = logic;
 } /**
* Sets the name.
* @param name The name to set
*/
 public void setName(String name) {
this. name = name;
 } /**
* Sets the value.
* @param value The value to set
*/
 public void setValue( double value) {
this. value = value;
 } /**
* Returns the speculateValue.
* @return double
*/
 public double getSpeculateValue() {
return speculateValue;
 } /**
* Sets the speculateValue.
* @param speculateValue The speculateValue to set
*/
 public void setSpeculateValue( double speculateValue) {
this. speculateValue = speculateValue;
 } /**
* Returns the type.
* @return String
*/
 public String getType() {
return type;
 } /**
* Sets the type.
* @param type The type to set
*/
 public void setType(String type) {
this. type = type;
 } /**
* Returns the project_ path.
* @return String
*/
 public String getProject_ path() {
return project_ path;
 } /**
* Sets the project_ path.
* @param project_ path The project_ path to set
*/
 public void setProject_ path(String project_ path) {
this. project_ path = project_ path;
 }"
