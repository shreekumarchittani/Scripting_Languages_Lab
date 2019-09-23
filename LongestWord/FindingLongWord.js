function FindMax(){
	var Mystring = document.getElementById("str").value;
	var arr = Mystring.split(" ");
	var i;
	var maxlen;
	maxlen=-1;
	var maxString;
	for(i=0;i<arr.length;i++){
		if(arr[i].length>maxlen){
		 	maxlen = arr[i].length;
		 	maxString = arr[i];	
		 }
		 }
	document.getElementById("res").innerHTML = maxString;
}
