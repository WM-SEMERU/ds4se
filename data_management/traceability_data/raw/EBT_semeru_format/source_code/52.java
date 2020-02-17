52	"Pair private String queryID;
 private String queryString; public Pair(String queryID, String queryString) {

this. queryID = queryID;
this. queryString = queryString;

 } public String getQueryID() {
return this. queryID;
 } public String getQueryString() {
return this. queryString;
 } public void setQueryID(String queryID) {
this. queryID = queryID ;
 } public void setQueryString(String queryString) {
this. queryString = queryString;
 } public String toString(){


return ""Query ID: ""
+ this. queryID
+ ""\ n""
+""Query String : ""
+ this. queryString
+ ""\ n"";


 }"
