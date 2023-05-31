const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')
canvas.width= window.innerHeight
document.body.appendChild(canvas);

class Player {
    constructor() {
        this.position ={
            x: 100,
            y: 100
        }
        // this.element = document.createElement("img");
        // this.element.src = url(image/img.png);
        // this.element.style.width = "78px";
        // this.element.style.height = "86px";
        // document.body.appendChild(this.element);
  }
        
    
    }
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

class Platform{
    this.position ={
        x: 0, 
        y: 0
            }
    this.width: 200;
    this.height: 20;
}
const player = new Player()
const platform = new Platform()