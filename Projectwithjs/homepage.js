var books = [
    {
        url: '../images/Inkognito.png',
        title: 'İnkognite 1',
        author: 'David-Eagleman',
        link: "https://www.qanun.az/incognito-beyinin-gizli-heyati-%E2%80%93-david-eagleman-251  "
    },
    {
        url: '../images/lusi.jpg',
        title: 'Lusifer effekti',
        author: 'Filip Zimbordo',
        link: "https://alinino.az/product/lusifer-effekti  "
    },
    {
        url: '../images/das evler.jpg',
        title: 'Daş evlər',
        author: 'Seyran Səxavət',
        link: "https://alinino.az/product/das-evler  "
    }
]
const randomBooks = []
const oldBooks = []
function increaseValue() {
    var index = Math.floor(Math.random() * books.length);
    if (oldBooks.includes(index) == true) {
        increaseValue()
    }
    else {
        randomBooks.push(`<div class='card  col-4 d-flex m-auto' style='width: 17rem;'>
        <img src="${books[index]['url']}" class="card-img-top">
        <div class="card-body">
            <h6 class="card-title">${books[index]["title"]} 1</h6>
            <p class="card-text">${books[index]["author"]}</p>
            <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
            </div> 
            </div>`)
        $("#randomBooks").html(randomBooks)
        $('#number').val(randomBooks.length)
        oldBooks.push(index)


    }
}
function decreaseValue() {
    randomBooks.pop()
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
    oldBooks.pop()
}
function calculate() {
    $("#calcul").css({ "background-color": "red", "border-color": "red", "box-shadow": "none" })
    if ($("#process").is(':hidden')) {
        $("#process").show()
        $("#calcul").html("Bitir")
    }
    else {
        $("#process").hide()
        $("#calcul").css({ "background-color": "#ffc107", "border-color": "#ffc107", "box-shadow": "#ffc107" })
        $("#calcul").html("Başla")
    }
    $("#process").removeClass("d-none")
}
function calculation() {
    var sum = parseInt($("#valu1").val()) / parseInt($("#valu2").val())
    $("#mark").html("Hər gün ən az " + sum + " səhifə oxumalısınız.")
}
function hamsi() {
    oldBooks.length = 0
    var eded = 0
    randomBooks.forEach(element => {
        randomBooks.length = 0
        $('#number').val(randomBooks.length)
        $("#randomBooks").html(randomBooks)
    });
    if (oldBooks.includes(eded) == true) {
        increaseValue()
    }
    else {
        books.forEach(element => {
            randomBooks.push(`<div class='card  col-4 d-flex m-auto' style='width: 17rem;'>
        <img src="${books[eded]['url']}" class="card-img-top">
        <div class="card-body">
            <h6 class="card-title">${books[eded]["title"]} 1</h6>
            <p class="card-text">${books[eded]["author"]}</p>
            <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
            </div> 
            </div>`)
            oldBooks.push(eded)
            eded++
            $('#number').val(randomBooks.length)
            $("#randomBooks").html(randomBooks)
            console.log(oldBooks)
        });
    }
}
function psixologiya() {
    oldBooks.push(0)
    oldBooks.push(1)
    oldBooks.push(2)
    randomBooks.length = 0
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
    randomBooks.push(`<div class='card  col-4 d-flex m-auto' style='width: 17rem;'>
        <img src="${books[0]['url']}" class="card-img-top">
        <div class="card-body">
            <h6 class="card-title">${books[0]["title"]} 1</h6>
            <p class="card-text">${books[0]["author"]}</p>
            <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
            </div> 
            </div>`)
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
}
function roman() {
    oldBooks.push(0)
    oldBooks.push(1)
    oldBooks.push(2)
    randomBooks.length = 0
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
    randomBooks.push(`<div class='card  col-4 d-flex m-auto' style='width: 17rem;'>
         <img src="${books[1]['url']}" class="card-img-top">
         <div class="card-body">
             <h6 class="card-title">${books[1]["title"]} 1</h6>
             <p class="card-text">${books[1]["author"]}</p>
             <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
             </div> 
             </div>`)
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
}
function elmi() {
    oldBooks.push(0)
    oldBooks.push(1)
    oldBooks.push(2)
    randomBooks.length = 0
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
    randomBooks.push(`<div class='card  col-4 d-flex m-auto' style='width: 17rem;'>
        <img src="${books[2]['url']}" class="card-img-top">
        <div class="card-body">
            <h6 class="card-title">${books[2]["title"]} 1</h6>
            <p class="card-text">${books[2]["author"]}</p>
            <a href="#" class="btn text-light" style="background-color: #2FA3B8;">Ətraflı</a>
            </div> 
            </div>`)
    $('#number').val(randomBooks.length)
    $("#randomBooks").html(randomBooks)
}