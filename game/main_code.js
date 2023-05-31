// const fairy = document.getElementById("fairy");

// document.addEventListener("keydown", function(event){
//     jump();
// });

// function jump () {
//     if (fairy.classList != "jump" ){
//         fairy.classList.add("jump")
//     }
//     setTimeout(function(){
//         fairy.classList.remove("jump")
//     },200)
// }


addEventListener('keydown', ({ keyCode }) => {
        switch (keyCode) {
            case 65:
                console.log('left')
                break
            case 83:
                console.log('down')
                break    
            case 68:
                console.log('right')
                break
            case 87:
                console.log('up')
                break
        }
    })
