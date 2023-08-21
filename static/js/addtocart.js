const product = [
    {
        id: 0,
        Image: 'Ap-panther-WC.png',
        title : 'Audemars Piguet Black Panther ',
        price: 7000,

    },
    {
        id: 1,
        Image: 'AP3-Wc.png',
        title : 'Audemars Piguet White Gold  ',
        price: 25000,

    },
    {
        id: 2,
        Image: 'jacob-watch-img.png',
        title : 'Jacob&co Dragon Edition ',
        price: 80000,

    },
    {
        id: 3,
        Image: 'Patek1-WC.avif',
        title : 'Patek Phillipe Nauritius 1 ',
        price: 17000,

    },
    {
        id: 4,
        Image: 'Patek2-WC.png',
        title : 'Patek Phillipe Asprey ',
        price: 35000,

    },
    {
        id: 5,
        Image: 'RM1-WC.jpg',
        title : 'Richard Mille RM 50-01 ',
        price: 30000,

    },
]

const categories =[...new set(product.map((item)=>
    {return item}))]
    let i=0;
    document.getElementById('root').innerHTML= categories.map((item)=>{
        var{image ,title , price }=item;
        return(
            `<div class='box'>
            <div class='img-box'>
            <img class='images' src=${image}></img>
            </div>

            <div class='bottom'>
            <p>${title}</p>
            <h2>$ ${price}.00</h2>`+
            "button onclick='addtocart("+(i++)+")'>Add to cart</button"+
            `</div>
            </div>`

            
        )
        
    }).join('')

    var cart=[];

    function addtocart(a){
        cart.push({...categories[a] });
        displaycart();

    }


    function deleteElement(a){
      cart.splice(a, 1)
      displaycart();


    }
     function displaycart(a){
        let j = 0; total=0;
        document.getElementById("count").innerHTML=cart.length;
        if(cart.length==0){
            document.getElementById('cartItem').innerHTML="Your cart is empty";
            document.getElementById("total").innerHTML = "$"+0+".00";

        }
        else{
            document.getElementById("cartItem").innerHTML = cart.map((item)=>
            {
                var {image , title ,price }=items;
                total=total+price ;
                document.getElementById("total").innerHTML = "$"+total+".00";
                return(
                    `<div class= 'cart-item'>
                    <div clas='row-img '>
                    <img class='rowing' src=${image}>
                    </div>
                    <p style='font-size: 12px;'>${title}</p> 
                    <h2 style='font-size: 15px ;>$ ${price}.00</h2>`+
                    "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div"
                );

            })
        }
     }
    