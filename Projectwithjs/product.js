var badge=document.getElementById("badge")
var badgeInside=2
badge.innerHTML=badgeInside
var money2 = document.getElementById("money2")
var money2Inner =37   
money2.innerText=money2Inner


function thumb() {

    let x = document.getElementById("thumb")

    if (x.style.color == "blue") {
        x.style.color = "gray"
    }
    else {
        x.style.color = "blue"
    }


}



function heart() {
    let x = document.getElementById("heart")
    if (x.style.color == "red") {
        x.style.color = "grey"
        alert("Bəyənməkdən imtina etdiniz!")
    }

    else {
        x.style.color = "red"
        alert("Kitabı bəyəndiniz!")
    }
}

function removeElement1() {
    var remove= document.getElementById("parent1")
    remove.style.display="none"
    badgeInside =badgeInside-1
    badge.innerText=badgeInside
    money2Inner =money2Inner-16
    money2.innerText=money2Inner
    
    
    
}

function removeElement2() {
    var remove= document.getElementById("parent2")
    remove.style.display="none"
    badgeInside =badgeInside-1
    badge.innerText=badgeInside
    money2Inner =money2Inner-21
    money2.innerText=money2Inner
    
    
}

function removeElement3() {
    var remove= document.getElementById("parent3")
    
    var y = document.getElementById("book")
    y.classList.remove("d-none")
    y.classList.toggle("d-flex")
    var x = document.getElementById("sebet")
    x.style.backgroundColor = "LightSeaGreen"
    x.style.borderColor = "LightSeaGreen "
    x.style.boxShadow = "LightSeaGreen "
    x.innerText = "Səbətə əlavə et"
    badgeInside =badgeInside-1
    badge.innerText=badgeInside
    money2Inner =money2Inner-12 
    money2.innerText=money2Inner
    
  
}


function sebet() {
    let x = document.getElementById("sebet")
    if (x.style.backgroundColor != "grey") {
        x.style.backgroundColor = "grey"
        x.style.borderColor = "grey"
        x.style.boxShadow = "grey"
        x.innerText = "Səbətdən çıxart"
        let y = document.getElementById("book")
        y.classList.remove("d-none")
        y.classList.toggle("d-flex")
        money2Inner =money2Inner+12
        money2.innerText=money2Inner
        
    
        badgeInside =badgeInside+1
        badge.innerText=badgeInside

    }
    else{
    x.style.backgroundColor = "LightSeaGreen"
    x.style.borderColor = "LightSeaGreen "
    x.style.boxShadow = "LightSeaGreen "
    x.innerText = "Səbətə əlavə et"
    let y = document.getElementById("book")
    y.classList.toggle("d-none")
    y.classList.remove("d-flex")
    
   
    
    
    let modal=document.getElementById("modal1")
    modal.innerText="Məhsul səbətdən çıxarıldı"
    badgeInside =badgeInside-1
    badge.innerText=badgeInside
    }


}
// if(document.getElementById("parent1").style.display=="none"){
    
//     money2Inner -=16
//     money2.innerText=money2Inner
//     window.money2Inner=money2Inner
// }

// else{
//     money2Inner +=16
//     money2.innerText=money2Inner
//     window.money2Inner=money2Inner


// }

// if(document.getElementById("parent2").style.display=="none"){
    
//     money2Inner -=21
//     money2.innerText=money2Inner
//     window.money2Inner=money2.money2Inner
// }
// else{
//     money2Inner +=21
//     money2.innerText=money2Inner
//     window.money2Inner=money2.money2Inner

// }
// if(document.getElementById("book").style.display=="none"){
    
//     money2Inner = money2Inner-12
//     money2.innerText=money2Inner
//     window.money2Inner=money2.money2Inner
// }
// else{
//     money2Inner = money2Inner+12

//     money2.innerText=money2Inner
//     window.money2Inner=money2.money2Inner


// }
