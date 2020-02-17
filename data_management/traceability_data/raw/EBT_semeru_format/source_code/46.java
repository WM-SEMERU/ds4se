private JPanel center  Panel = null  ;

 private JLabel des  Label = null  ;
 private JLabel change  Label = null  ;
 private JLabel from  Label = null  ;
 private JLabel to  Label = null  ;
 private JText  Area des  Text = null  ;
 private JText  Field c Speculate Gui public Speculate  Gui  ()
 {

  super  ("  Speculate GUI  ");

  container = get  Content  Pane  ();

  set  Size  (  800  , 600  );

  this  . event  Server  IP =
   JOption  Pane
    . show  Input  Dialog  ("  Please Enter the IP Address of eventserver  Submit Listener public void action  Performed  (  Action  Event e  ) {

   if ( e  . get  Source  () == submit  Button  ) {

    send  Query  TO Server  ();

   }

   if ( e  . get  Source  () == fetch  Button  ) {


    System  . out  . println  ("  Fetch Button Pressed void send  Query  TO Server  ()
 {

  String ip = this  . event  Server  IP  ;
  int Port  No = 1701  ;

  Socket socket  ;
  try {

   socket = new Socket  ( ip  , Port  No  );

   Output  Stream os = socket  . get  Output  Stream  ();
   Output  Stream  public void pull  Value  From  DOORS  ()
 {

  String server  IP = new String  ( doors server  IP  ); //"  140  .  192  .  37  .  150  ";

  String  [] attribute = { "  Value  ", "  Attribute  " };

  String project  Name = this  . proj  Name  Text  . get public static void main  (  String  [] args  )
 {
  new Speculate  Gui  ();
 }