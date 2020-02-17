71	"Requirementpublic String m_RequirementID ="""";
public String m_Project ="""";
public String m_ModulePath="""";
public String m_Content = """";
public String m_RegFlag = ""N""; public Requirement()
{

} public Object clone() throws CloneNotSupportedException
 {

Requirement requirement= (Requirement) super. clone();
return requirement ;
 } public void ReadValues(String RequirementID, String Project, String ModulePath, String Content, String RegFlag)
 {
this. m_RequirementID = RequirementID;
this. m_Project = Project;
this. m_ModulePath public void ParseRequirement(String TextLine)
 {

 StringTokenizer LineSt;
LineSt = new StringTokenizer(TextLine, "","");
m_RequirementID=LineSt. nextToken();
m_Project=LineSt. "
