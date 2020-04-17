let numeros = [1, 6, 8, 20, 2, 7, 0, 3, 5];
let mayor = -999999;

for (let i = 0; i <= numeros.length; i++) {

    if (numeros[i] >= mayor) {
        mayor = numeros[i];
    }

}


console.log('El número mayor es: ' + mayor);