const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width= window.innerWidth
canvas.height= window.innerHeight

const gravity = 0.5

class Player {
    constructor() {
        this.position = {
            x: 200,
            y: 200
        }
        this.velocity = {
            x:0,
            y:5
        }

        const image = new Image()
        image.src ='./image/img.png'

        this.image = image
        this.width = 100
        this.height = 100
  }
    draw(){
        c.drawImage(this.image, this.position.x, this.position.y)
    }

    update() {
        this.position.y += this.velocity.y
        this.draw()
        this.velocity.y += gravity
    }
    
    }


// addEventListener('keydown', ({ keyCode }) => {
//         switch (keyCode) {
//             case 65:
//                 console.log('left')
//                 break
//             case 83:
//                 console.log('down')
//                 break    
//             case 68:
//                 console.log('right')
//                 break
//             case 87:
//                 console.log('up')
//                 break
//         }
//     })

// class Platform{
//     this.position = {
//         x: 0, 
//         y: 0
//      }
//     this.width = 200
//     this.height = 20
// }
const player = new Player()
player.update()
// const platform = new Platform()

function animate() {
    requestAnimationFrame(animate)
    c.fillRect(0,0, canvas.width, canvas.height)
   player.update()
}
animate()