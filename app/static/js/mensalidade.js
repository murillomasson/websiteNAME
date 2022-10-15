function mensalidade()
{
  var mensalidade;
  var n = parseFloat(document.getElementById('n').value);

  if (n < 32){
  mensalidade = n * 0.8
  }
  else{
  mensalidade = 32
  }
  alert("R$" + mensalidade + "");
}