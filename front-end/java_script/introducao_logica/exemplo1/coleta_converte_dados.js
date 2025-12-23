function converter(){
const nome = document.getElementById('nome').value
const duracao = document.getElementById('duracao').value

const hora = Math.floor(duracao/60)
const minutos = duracao - hora * 60

document.getElementById('titulo').textContent = nome.toUpperCase()
document.getElementById('tempo').textContent = hora + 'hora(s)' + minutos + 'minuto(s)'
}
