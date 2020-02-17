50	"Driver Description private String projectName = null;
 private String modulePath = null;
 private String requirementID = null;

 private String description = null; // Description of the requirement.
 private String changedArrtibute = null;
 private Strinpublic DriverDescription(
String projectName,
String modulePath,
String requirementID,
String description,
String changedAttribute,
String fromAttribute,
String toAttribute)
 {

this. projectName = projecpublic String getChangedAttribute()
 {
return changedAttribute;
 }public String getDescription()
 {
return description;
 }public String getFromAttribute()
 {
return fromAttribute;
 } public String getModulePath()
 {
return modulePath;
 }public String getProjectName()
 {
return projectName;
 } public String getRequirementID()
 {
return requirementID;
 } public String getToAttribute()
 {
return toAttribute;
 } public void setChangedAttribute(String changedAttribute)
 {
this. changedAttribute = changedAttribute;
 } public void setDescription(String description)
 {
this. description = description;
 } public void setFromAttribute(String fromAttribute)
 {
this. fromAttribute = fromAttribute;
 } public void setModulePath(String modulePath)
 {
this. modulePath = modulePath;
 } public void setProjectName(String projectName)
 {
this. projectName = projectName;
 } public void setRequirementID(String requirementID)
 {
this. requirementID = requirementID;
 } public void setToAttribute(String toAttribute)
 {
this. toAttribute = toAttribute;
 } public String createKey()
 {
String key =
 this. projectName + this. modulePath + ""\\"" + this. requirementID;

return key. toLowerCase();

 } public boolean equals(Object o)
 {
if (!( o instance of DriverDescription))
 return false;

DriverDescription dd = (DriverDescription) o;

if ( dd. projectName. equalsIgnoreCase( this. projectName)
 && ddpublic String toString()
 {

String str =
 ""\ nProject Name = ""
+ this. projectName
+ ""\ n""
+ ""Module Path = ""
+ this. modulePath
+ ""\ n""
+ ""Requirement ID = ""
+ this. requirementID
+ ""\ n""
public int hashCode()
 {

int hashCode = 0;

if ( hashCode == 0)
{
 int result = 17;
 result = 37 * result + this. projectName. hashCode();
 result = 37 * result + this. modulePath. hashCode();
 result = 37 "
