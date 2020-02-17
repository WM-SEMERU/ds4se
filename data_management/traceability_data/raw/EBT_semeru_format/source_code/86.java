86	"EB Shape private int x, y;
 private String requirement No;
 private String ProjectName, ModulePath;
private Color c; public EBShape( int xpos, int ypos, Color col)
 {
x = xpos;
y = ypos;
c = col;
requirement No = """";
ProjectName = """";
ModulePath = """";
 } public void Updaterequirement Info(String rno, String pname, String mname)
 {
requirement No = rno. trim();
ProjectName = pname. trim();
ModulePath = mname. trim();
 } public boolean match( int mx, int my)
 {
return true;

 } public int GetX()
 {
return x;
 } public int GetY()
 {
return y;
 } public Color GetC()
{
return c;
 } public String GetReqno()
 {
return requirement No;
 } public String GetProject()
 {
return ProjectName;
 } public String GetModule()
 {
return ModulePath;
 }"
