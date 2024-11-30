const input = document.getElementById('inputNumero');

input.addEventListener('input', function () {
  // Remove caracteres não numéricos
  this.value = this.value.replace(/\D/g, '');

  // Limita a 14 caracteres
  if (this.value.length > 14) {
    this.value = this.value.slice(0, 14);
  }
});