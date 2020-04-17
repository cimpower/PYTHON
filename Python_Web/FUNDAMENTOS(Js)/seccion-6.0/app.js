function describirPersona(p) {


    console.log(`${ p.nombre } tiene una edad de ${ p.edad } y mide ${ p.estatura }`);

}



let persona = {
    nombre: 'Melissa',
    edad: 27,
    estatura: 1.50
}

describirPersona(persona);