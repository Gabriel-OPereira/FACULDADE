let dadosMarcas = [];

async function consultaMarca() {
  const url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas';
  
  try {
    const resposta = await fetch(url);
    dadosMarcas = await resposta.json();
    exibiMarca(dadosMarcas);
  } catch (erro) {
    console.error('Erro ao consultar API:', erro);
  }
}

function exibiMarca(dados) {
  const corpoMarcas = document.getElementById('corpo-marcas');
  corpoMarcas.innerHTML = '';

  dados.forEach(marca => {
    const linha = document.createElement('tr');
    linha.innerHTML = `
      <td style = "padding-left: 30px;">${marca.codigo}</td>
      <td style = "padding-left: 80px;">${marca.nome}</td>
      <td><button onclick="exibirCarros('${marca.codigo}')">Ver Carros</button></td>
    `;
    corpoMarcas.appendChild(linha);
  });
}

async function exibirCarros(Marca) {
  const url = `https://parallelum.com.br/fipe/api/v1/carros/marcas/${Marca}/modelos`;
  try {
    const resposta = await fetch(url);
    const data = await resposta.json();
    const corpoCarros = document.getElementById('corpo-carros');
    corpoCarros.innerHTML = '';

    data.modelos.forEach(carro => {
      const linha = document.createElement('tr');
      linha.innerHTML = `
        <td>${carro.nome}</td>
      `;
      corpoCarros.appendChild(linha);
    });

    const tabelaCarros = document.getElementById('tabela-carros');
    tabelaCarros.style.display = 'table';
  } catch (erro) {
    console.error('Erro ao consultar API:', erro);
  }
}

function pesquisarMarca() {
  const entrada = document.getElementById('marca-entrada').value.toLowerCase();
  const marcasFiltradas = dadosMarcas.filter(marca => marca.nome.toLowerCase().includes(entrada));
  exibiMarca(marcasFiltradas);
}

window.onload = consultaMarca;
