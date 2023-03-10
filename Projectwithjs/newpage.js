let number_of_page = window.prompt("Kitabın səhifə sayı:")


let days =window.prompt("Neçə günə bitirməlisiniz?")
if (isNaN(number_of_page )==true|| isNaN(days)==true){
    alert("Hesablamada problem baş verdi")
    
}
else if(number_of_page==0){
    alert("Hesablamada problem baş verdi")
    
    
}
else{
    alert("hər gün ən az " + number_of_page / days + " səhifə oxumalısınız!")
}


console.log("Səhifə sayı: " + number_of_page)
console.log("Gün sayı: " + days)
console.log("Nəticə: " + number_of_page / days)
