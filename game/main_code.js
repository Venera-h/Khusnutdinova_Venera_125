const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

canvas.width= window.innerWidth
canvas.height= window.innerHeight

const gravity = 0.2

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
        c.drawImage(this.image, this.position.x, this.position.y, this.width, this.height)
    }

    update() {
        this.draw()
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y

        if (this.position.y + this.height + 
            this.velocity.y <= canvas.height)
            this.velocity.y += gravity
         else this.velocity.y = 0

    }
    
    }


  addEventListener('keydown', ({ keyCode }) => {
         switch (keyCode) {
              case 37:
                  console.log('left')
                  keys.left.pressed = true
                //   player.velocity.x -= 5
                  break
              case 40:
                  console.log('down')
                  player.velocity.y += 7
                  break    
              case 39:
                  console.log('right')
                //   player.velocity.x += 5
                  keys.right.pressed = true
                  break
              case 38:
                  console.log('up')
                  player.velocity.y -= 7
                  break
         }
        //  console.log(keys.right.pressed)
        }) 
        addEventListener('keyup', ({ keyCode }) => {
            switch (keyCode) {
                 case 37:
                     console.log('left')
                     keys.left.pressed = false
                   //   player.velocity.x -= 5
                     break
                 case 40:
                     console.log('down')
                     player.velocity.y += 20
                     break    
                 case 39:
                     console.log('right')
                   //   player.velocity.x += 5
                     keys.right.pressed = false
                     break
                 case 38:
                     console.log('up')
                     player.velocity.y -= 20
                     break
            }
           }) 
    
    //   addEventListener('keydown', (event) =>{
    //      console.log(event)
    //   })

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
const keys = {
right: {
    pressed: false
},
left: {
    pressed: false
}
}
// const platform = new Platform()

function animate() {
    requestAnimationFrame(animate)
   c.fillRect(0,0, canvas.width, canvas.height)
   c.clearRect(0,0, canvas.width, canvas.height)
   player.update()

    if (keys.right.pressed) 
        player.velocity.x =5
    else if (keys.left.pressed)
        player.velocity.x =-5
    else player.velocity.x = 0 
   
}
animate()