76	"Evaluatorprivate static final int EOL = 0;
private static final int VALUE = 1;
private static final int OPAREN= 2;
private static final int CPAREN= 3;
private static final int EXP = 4;
private static final int MULT= private static class Precedence
{

public int inputSymbol; // refers to the precedence level of operator
public int topOfStack; // stores the operator in the form of integer

public Precedence( int inSymbol, int // PrecTable matches order of Token enumeration
private static Precedence [ ] precTable = new Precedence[ ]
{

new Precedence( 0, -1 ),// EOL
new Precedence( 0,0 ),// VALUE
new Precedence( 100private static class Token
{

public Token( ) { this( EOL ); }

public Token( int t ) { this( t, 0 ); }

public Token( int t, double v ) {

 System. out. println("" INSIDE Token.Token()"");
 private static class EvalTokenizer {

public EvalTokenizer( StringTokenizer is ) {
 System. out. println(""INSIDE EvalTokenizer"");
 str = is;
} /**
 * Find the next token, skipping blanks, and return it.
 * For VALUE token, place the processed value in currentValue.
 * Print error message if input is unrecognized.
 */
public Token getToken /**
 * Construct an evaluator object.
 * @param s the string containing the expression.
 */
public Evaluator( String s ) {

opStack = new Stack( );
postfixStack = new Stack( );
str = new StringTokeni // The only publicly visible routine
/**
 * Public routine that performs the evaluation.
 * Examine thepostfix machine to see if a single result is
 * left and if so, return it; otherwise print error.
 * @return the result. private Stack opStack; // Operator stack for conversion
private Stack postfixStack;// Stack for postfix machine that stores the numbers could be values or result
private StringTokenizer str; // StringTokenizer stream, conte /**
 * Internal method that hides type-casting.
 * Changed the method to support double
 */
private double postFixTopAndPop( ) {
 System. out. println(""INSIDE postFixTopAndPop method"");
 System /**
 * Another internal method that hides type-casting.
 */
private int opStackTop( ) {
return ( (Integer) ( opStack. peek( ) ) ). intValue( );
} /**
 * After a token is read, use operator precedence parsing
 * algorithm to process it; missing opening parentheses
 * are detected here.
 */
private void processToken( Token lastToken ) {

System. out. printl /*
 * topAndPop the postfix machine stack; return the result.
 * If the stack is empty, print an error message.
 */
private double getTop( ) { // change to support double
 System. out. println(""INSIDE GET TOP/**
 * Internal routine to compute x^ n.
 */
private static double pow( double x, double n ) {
 System. out. println(""INSIDE pow"");

if( x == 0 ) {
 if( n == 0 ){
System. out. /**
 * Process an operator by taking two items off the postfix
 * stack, applying the operator, and pushing the result.
 * Print error if missing closing parenthesis or division by 0.
 */
private void binaryOp( int topOp/**
 * Simple main to exercise Evaluator class.
 */
public static void main( String [ ] args ) {



String str;
BufferedReader in = new BufferedReader( new InputStreamReader( System. in ) );

try {
 "
