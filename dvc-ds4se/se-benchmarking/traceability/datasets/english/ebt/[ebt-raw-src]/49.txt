49	"Constraints Description private String project  Name = null  ;
 private String module  Path = null  ;
 private String requirement  ID = null  ;

 private String value = null  ;
 private String logic = null  ;
 private String units = null  ;
 private String description = null  ;
 public Constraints  Description  (
  String project  Name  ,
  String module  Path  ,
  String requirement  ID  )
 {

  this  . project  Name = project  Name  ;
  this  . module  Path = module  Path  ;
  this  . requirement  ID = requirement  ID  ;

 }  public String get  Description  () {
  return this  . description  ;
 }  public String get  Logic  () {
  return this  . logic  ;
 }  public String get  Module  Path  () {
  return this  . module  Path  ;
 }  public String get  Project  Name  () {
  return this  . project  Name  ;
 }  public String get  Requirement  ID  () {
  return this  . requirement  ID  ;
 }  public String get  Units  () {
  return this  . units  ;
 }  public String get  Value  () {
  return this  . value  ;
 }  public void set  Description  (  String description  ) {
  this  . description = description  ;
 }  public void set  Logic  (  String logic  ) {
  this  . logic = logic  ;
 }  public void set  Module  Path  (  String module  Path  ) {
  this  . module  Path = module  Path  ;
 }  public void set  Project  Name  (  String project  Name  ) {
  this  . project  Name = project  Name  ;
 }  public void set  Requirement  ID  (  String requirement  ID  ) {
  this  . requirement  ID = requirement  ID  ;
 }  public void set  Units  (  String units  ) {
  this  . units = units  ;
 }  public void set  Value  (  String units  ) {
  this  . value = units  ;
 }  public String get  Impacted  Constraint  () {
  return this  . impacted  Constraint  ;
 }  public void set  Impacted  Constraint  (  String impacted  Constraint  ) {
  this  . impacted  Constraint = impacted  Constraint  ;
 }  public String get  Attribute  () {
  return this  . attribute  ;
 }  public void set  Attribute  (  String attribute  ) {
  this  . attribute = attribute  ;
 }  public String get  Performance  Model  Name  () {
  return this  . performance  Model  Name  ;
 }  public void set  Performance  Model  Name  (  String performance  Model  Name  ) {
  this  . performance  Model  Name = performance  Model  Name  ;
 } public String to  String  () {

  String str =
   ""\ n  Project Name = ""
    + this  . project  Name
    + ""\ n  ""
    + ""  Module Path = ""
    + this  . module  Path
    + ""\ n  ""
    + ""  Requirement ID = ""
    + this  . requirement  ID
    + ""\ n  ""
   public boolean equals  (  Object o  ) {

  if (!( o instance of Constraints  Description  ))
   return false  ;

  Constraints  Description cd = (  Constraints  Description  ) o  ;

  if ( cd  . project  Name  . equals  Ignore  Case  ( this  . project  Na  public int hash  Code  () {

  int hash  Code = 0  ;

  if ( hash  Code == 0  ) {
   int result = 17  ;
   result = 37 * result + this  . project  Name  . hash  Code  ();
   result = 37 * result + this  . module  Path  . hash  Code  ();
   result = 37 * "
