const $button = document.querySelector('.burger')
const $nav = document.querySelector('#sideBare')

$button.addEventListener('click', e => {
    e.preventDefault()

    $nav.classList.toggle('show')
    $button.classList.toggle('burgerLeft')
})



const $homeLink = document.querySelector('#homeLink')
const $aboutLink = document.querySelector('#aboutLink')
const $valuesLink = document.querySelector('#valuesLink')
const $roadmapLink = document.querySelector('#roadmapLink')
const $techLink = document.querySelector('#techLink')
const $servicesLink = document.querySelector('#servicesLink')
const $positionsLink = document.querySelector('#positionsLink')
const $contactLink = document.querySelector('#contactLink')



window.addEventListener('scroll' , e => {
    if(window.scrollY > 0 && window.scrollY < 800){
        $homeLink.classList.add('activated')
    }else{
        $homeLink.classList.remove('activated')
    }

    if(window.scrollY > 800 && window.scrollY < 1300){
        $aboutLink.classList.add('activated')
    }else{
        $aboutLink.classList.remove('activated')
    }


    if(window.scrollY > 1300 && window.scrollY < 2000){
        $valuesLink.classList.add('activated')
    }else{
        $valuesLink.classList.remove('activated')
    }

    if(window.scrollY > 2200 && window.scrollY < 3000){
        $roadmapLink.classList.add('activated')
    }else{
        $roadmapLink.classList.remove('activated')
    }

    if(window.scrollY > 3100 && window.scrollY < 4000){
        $techLink.classList.add('activated')
    }else{
        $techLink.classList.remove('activated')
    }

    if(window.scrollY > 4100 && window.scrollY < 5300){
        $servicesLink.classList.add('activated')
    }else{
        $servicesLink.classList.remove('activated')
    }

    if(window.scrollY > 5400 && window.scrollY < 6000){
        $positionsLink.classList.add('activated')
    }else{
        $positionsLink.classList.remove('activated')
    }

    if(window.scrollY > 6050 && window.scrollY < 7200){
        $contactLink.classList.add('activated')
    }else{
        $contactLink.classList.remove('activated')
    }
})