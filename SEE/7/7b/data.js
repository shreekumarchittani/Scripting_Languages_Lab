window.onload=function()	{

    Models=[
            {
                "name":"Model1",
                "model":"model1",
                "price":"6,25,000",
                "year":"2017"
            },

            {
                "name":"Model2",
                "model":"model2",
                "price":"4,00,000",
                "year":"2018"
            },

            {
                "name":"Model3",
                "model":"model3",
                "price":"7,50,000",
                "year":"2015"
            }
        ];


    Models.forEach(function(item,index)	{

        elem=document.createElement("th");
        elem.id=item.model;
        elem.innerHTML=item.name;
        document.getElementById("menu").appendChild(elem);

    })
    Models.forEach(mouseEventHandler);
	
		function mouseEventHandler(item,index)	{
	
			elem=document.getElementById(item.model);
			elem.onmouseover=function ()	{
			
				details=item;
				document.getElementById("data-elements").removeAttribute("hidden");
				document.getElementById("name").innerHTML=details.name;
				document.getElementById("picture").innerHTML='<img src="/luma/home/'+details.model+'1.jpeg">';
				document.getElementById("price").innerHTML="Rs."+details.price;
				document.getElementById("year").innerHTML=details.year;
			}
		}
};
