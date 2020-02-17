66	"Config Dialog public ConfigDialog(Notification_Processing parent, boolean modal) {
 
super ( parent, modal);
 setTitle(""Config Dialog Box"");
 getContentPane (). setLayout ( new GridLayout(5,2));

private void closeDialog(WindowEvent evt) {
setVisible ( false);
dispose ();
}// event listener for ""Ok"" button 
private void okButtonActionPerformed (ActionEvent evt) {
 
 if( UserName. getText(). equals("""") || DSN. getText(). equals("""") || EventServerIP. getText(). equa// event listener for ""Cancel"" button
private void cancelButtonActionPerformed (ActionEvent evt) {
setVisible ( false);
dispose (); 
} // configuration entries
private JLabel UserNameLabel; 
private JTextField UserName;
private JLabel DSN Label; 
private JTextField DSN;
private JLabel EventServerIP Label; 
private JTextField EventSe"
