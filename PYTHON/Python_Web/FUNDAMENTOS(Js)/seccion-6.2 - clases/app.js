class Carro {

    constructor(marca1, tipo1, puertas) {

        this.marca = marca1;
        this.tipo = tipo1;
        this.puertas = puertas;

        this.creadoEn = 'hoy';
        this.encendido = false;
        this.gasolina = 100;

    }

    encenderCarro() {

        if (this.encendido) {
            console.error('El carro ya estaba encendido... se daño el motor');
        } else {
            this.encendido = true;
            console.log('El carro esta encendido');
        }

        return this;
    }

    realizarViaje(consumo) {

        if (!this.encendido) return console.log('Carro apagdo');

        if (consumo > this.gasolina) return console.log('No puede realizar el viaje: Gasolina ' + this.gasolina);

        this.gasolina = this.gasolina - consumo;
        return 'Le queda ' + this.gasolina;


    }

} // fin clase

let carro = new Carro('Mazda', 'Sedan', 2);


console.log(carro);