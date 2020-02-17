75	"Driver String id;
 double valueFrom;
 double valueTo;
 String name; Driver(String id, double valueFrom, double valueTo, String name)
 {
this. id = id;
this. valueFrom = valueFrom;
this. valueTo = valueTo;
this. name = name;
 } public String toString()
 {
String temp;
temp = ""ID = "" + id + "", valueFrom = "" + valueFrom + "", valueTo = "" + valueTo + "", Name = "" + name;
return temp;
 } /**
* Returns the id.
* @return int
*/
 public String getId()
 {
return id;
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
 public double getValueFrom()
 {
return valueFrom;
 } public double getValueTo()
 {
return valueTo;
 } /**
* Sets the id.
* @param id The id to set
*/
 public void setId(String id)
 {
this. id = id;
 } **
* Sets the name.
* @param name The name to set
*/
 public void setName(String name)
 {
this. name = name;
 } **
* Sets the value.
* @param value The value to set
*/
 public void setValueFrom( double value)
 {
this. valueFrom = valueFrom;
 } public void setValueTo( double value)
 {
this. valueTo = valueTo;
 }"
