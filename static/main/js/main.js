// for(let i = 1 ; i < 101 ; i++){
//     const h = document.querySelector('.h1')
//     console.log(`${i}. hello`)
   
// }
const modal = document.querySelector('.nv-modal')
const menu = document.querySelector('.menu')
const x = document.querySelector('.ix')


menu.addEventListener('click' , ()=>{
    modal.style.display = 'block'
})
x.addEventListener('click' , ()=>{
    modal.style.display = 'none'
})
