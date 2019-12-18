window.onload = () =>{
    var jsonobj = [
        {
            "name":"Rohit",
            "country":"Gitland",
            "title":"Hackerman",
            "year":"3000"
        },
        {
            "name":"Reshma",
            "country":"USA-LA",
            "title":"Haunted",
            "year":"2050"
        },
        {
            "name":"Nikhil Zombie",
            "country":"The dark",
            "title":"Deadland",
            "year":"2021"
        },
        {
            "name":"Shreekumar",
            "country":"South Africa",
            "title":"Surviving in Africa",
            "year":"2019"
        }
    ]
    
    jsonobj.forEach(function dothis(item,index){
        if(index<=1){
        var abc = document.createElement('div')
        for(i=0;i<2;i++){
            var def = document.createElement('th')
            def.innerHTML = item.name
            var cont = document.createElement('h6')
            cont.innerHTML = item.country
            var year1 = document.createElement('h6')
            year1.innerHTML = item.year
            var titl = document.createElement('h6')
            titl.innerHTML = item.title
        }
            def.appendChild(cont)
            def.appendChild(year1)
            def.appendChild(titl)
            abc.appendChild(def)
            document.getElementById('auth').appendChild(abc)
    }
        else{
            var abc = document.createElement('p')
        for(i=0;i<2;i++){
            var def = document.createElement('p')
            def.innerHTML = item.name
            var cont = document.createElement('h6')
            cont.innerHTML = item.country
            var year1 = document.createElement('h6')
            year1.innerHTML = item.year
            var titl = document.createElement('h6')
            titl.innerHTML = item.title
        }
            def.appendChild(cont)
            def.appendChild(year1)
            def.appendChild(titl)
            abc.appendChild(def)
            document.getElementById('auth1').appendChild(abc)
        }
    })
}