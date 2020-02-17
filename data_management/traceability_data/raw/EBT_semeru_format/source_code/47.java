47	"Impact Report private String server  IP = "" local host  "";
 private JPanel center  Panel = null  ;

 private JPanel driver  Panel = new JPanel  ();

 private JPanel driver  Inner  Panel = null  ;

 private JPanel impact  Panel = null  ;
 private JPanel impact  Inner  P public Impact  Report  ()
 {

  super  (""  Search Result GUI  "");

  container = get  Content  Pane  ();

  set  Size  (  800  , 250  );

  panel = new JPanel  ();

  panel  . set  Layout  ( null  );

  this  . server  IP =
   JOption  Pane
    . show  In public static void main  (  String [] args  )
 {

  Impact  Report im = new Impact  Report  ();



 } public Vector search  Date  ()
 {

  date  Vector = new Vector  ();
  date  Vector  . add  (""  Select Query Date  "");
  Socket server  ;
  String line = new String  ();


  try
  {

   server = new Socket  ( server  IP  ,  1701  );
   if ( server  . is  C public void search  Query  ID  (  String date  )
 {

  pair  Vector = new Vector  ();

  query  String  Combo  . remove  All  Items  ();

  query  String  Combo  . add  Item  (""  Select Query String  "");

  Socket server  ;
  String line = new String  (); Select Actions public void action  Performed  (  Action  Event e  )
  {

   if ( date  Combo == (  JCombo  Box  ) e  . get  Source  ())
   {
    date = (  String  ) date  Combo  . get  Selected  Item  ();
    search  Query  ID  ( date  );
   }
  } Button Actions  public void action  Performed  (  Action  Event e  ) {

   if ( submit  Button == e  . get  Source  ()) {

    for ( int i = 0  ; i < pair  Vector  . size  (); i  ++) {

     Pair pair = (  Pair  ) pair  Vector  . get  ( i  );

     if ( pair
      . get public void impact  Report  (  String id  )
 {

  // super  (""  Impact Report  "");

  container = get  Content  Pane  ();

  set  Size  (  1020  , 740  );

  this  . query  ID = id  ;

  System  . out  . println  (""  Impact Report Constructor ..... ID "" + public Vector get  Constraint  From  Data  Base  ()
 {

  Vector v = new Vector  ();

  Socket server  ;
  String line = new String  ();


  try
  {
   server = new Socket  ( server  IP  ,  1701  );

   if ( server  . is  Connected  () )
   {
    Buffered  public Vector get  Driver  From  Data  Base  ()
 {

  Vector v = new Vector  ();

     Socket server  ;
  String line = new String  ();


  try
  {
   server = new Socket  ( server  IP  ,  1701  );

   if ( server  . is  Connected  () )
   {
    Buffered"
