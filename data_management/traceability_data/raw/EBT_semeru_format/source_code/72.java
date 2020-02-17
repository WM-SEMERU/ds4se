72	"Balance /**
 * Symbol represents what will be placed on the stack.
 */
private static class Symbol
{
public chartoken;
public int theLine;

public Symbol( char tok, int line )
{
token = /**
 * Constructor.
 * @param inStream the stream containing a program.
 */
public Balance( Reader inStream )
{
errors = 0;
tok = new Tokenizer( inStream );
}/**
 * Print an error message for unbalanced symbols.
 * @return number of errors detected.
 */
public int checkBalance( )
{
char ch;
Symbol match = null;
Stack pendingTokens = new Stack( );

 private Tokenizer tok;
private int errors; /**
 * Print an error message if clSym does not match opSym.
 * Update errors.
 */
private void checkMatch( Symbol opSym, Symbol clSym )
{
if( opSym. token == '(' && clSym. token != ')' ||
 /**
 * main routine for balanced symbol checker.
 * Slightly different from text.
 * If no command line parameters, standard input is used.
 * Otherwise, files in command line are used.
 */
public static void main( St"
