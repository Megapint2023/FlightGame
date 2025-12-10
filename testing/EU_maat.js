'use strict';

fetch("http://127.0.0.1:5000/countries")
  .then(res => res.json())
  .then(countries => {
    const panel2 = document.getElementById("panel_2");
    const list = document.createElement("ul");

    countries.forEach(name => {
      const li = document.createElement("li");
      li.textContent = name;
      list.appendChild(li);
    });

    panel2.appendChild(list);
  })
  .catch(err => console.error("ERR fetching countries:", err));