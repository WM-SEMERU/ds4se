48	"Constraint Inner Panel  private String server  IP = "" local host  "";
 private JLabel performance  Model  Label = null  ;
 private JLabel project  Name  Label = null  ;
 private JLabel module  Path  Label = null  ;
 private JLabel requirement  Id  Label = null  ;
 private JLabel public Constraint  Inner  Panel  (
  String performance  Model  Name  ,
  String project  Name  ,
  String module  Path  ,
  String requirement  Id  ,
  String description  ,
  String logic  ,
  String units  ,
  String value  ,
  String impacted  Value    private void set goal  Label  Values  (
  String attribute  ,
  String logic  ,
  String value  ,
  String units  )
 {
  goal  Label  . set  Text  (
   ""  Goal : "" + attribute + ""  "" + logic + ""  "" + value + "" "" + units  );

 }  public Vector get  Values  From  Data  Base  ()
 {

  Vector v = new Vector  ();

  Socket server  ;
  String line = new String  ();


  try
  {
   server = new Socket  ( server  IP  ,  1701  );

   if ( server  . is  Connected  () )
   {
    Buffered  R  private void set impacted  Label  Value  (
  String attribute  ,
  String value  ,
  String impacted  Value  ,
  String units  ,
  String logic  )
 {

  if ( impacted  Value !  = null  )
  {

   double value  1 = Double  . parse  Double  ( value  );
   d  public JPanel get  Panel  ()
 {
  return panel  ;
 }"
