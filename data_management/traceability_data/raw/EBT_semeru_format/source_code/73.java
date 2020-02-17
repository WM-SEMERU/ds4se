73	"Constraints String id;
 String name;
 double value;
 String logic; Constraints(String id, String name, double value, String logic){
this. id = id;
this. name = name;
this. value = value;
this. logic = logic;
 } public String toString(){
 String temp;
 temp = ""ID = "" + id + "", Name = "" + name +"", value = "" + value + "", Logic = "" + logic;
 return temp;
 } /**
* Returns the id.
* @return int
*/
 public String getId() {
return id;
 } /**
* Returns the logic.
* @return String
*/
 public String getLogic() {
return logic;
 } /**
* Returns the name.
* @return String
*/
 public String getName() {
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
 } **
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
 }"
