fetch("/productos")
  .then(res => res.json())
  .then(data => {
    let contenedor = document.getElementById("productos");

    data.forEach(p => {
      contenedor.innerHTML += `
        <div class="producto">
          <img src="${p.imagen}" alt="${p.nombre}">
          <h3>${p.nombre}</h3>
          <p>S/. ${p.precio}</p>
        </div>
      `;
    });
  });