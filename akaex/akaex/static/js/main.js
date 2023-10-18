
var schools = []

function init_fill(selector) {
  var elems = document.querySelectorAll(selector)
  var height = 0
  for (var i = 0; i < elems.length; i++) {
    let curr = elems[i]
    let rect = curr.getBoundingClientRect()
    let styles = window.getComputedStyle(curr)
    let padding_bottom = parseFloat(styles.paddingBottom)
    let margin_bottom = parseFloat(styles.paddingBottom)
    let margin_top = parseFloat(styles.marginTop)
    if (rect.top != 0) {
      height = window.innerHeight - rect.top - margin_bottom - padding_bottom - window.innerHeight*0.025
    }
    curr.style.height = height.toString().concat('px')
  }
}

function load_school_list() {
  // Hacer una solicitud Axios a la URL /list
  axios.get('/list')
  .then(response => {
    // Obtener los datos de la respuesta
    const data = JSON.parse(response.data);
    schools = data
    // Iterar sobre los datos
    $.each(data, function(index, item) {
        // Crear un elemento <li>
        var option = $('<option>', {
            class: 'blue lighten-5 black-text',
            value: item.id,
        });

        // Crear un elemento <a>
        var row = $('<div>', {
            href: '#!',
            class: 'row',
        });

        var name = $('<div>', {
          class: 'col s12 m12 l12',
          text: item.name,
        })
        // var municipality = $('<div>', {
        //   class: 'col s6 m6 l6',
        //   text: item.municipality,
        // })
        row.append(name)
        // row.append(municipality)
        // Añadir el elemento <a> al elemento <li>
        option.append(row);

          // Añadir el elemento <li> al menú desplegable
          $('#school-select').append(option);
      });
      var elems = document.getElementById("school-select");
      var instances = M.FormSelect.init(elems, options);
  })
  .catch(error => {
    // Manejar el error
    console.error(error);
  });
}

function onExportButtonClick() {
  var selector = document.getElementById('school-select')
  window.location.href = '/export?id='.concat(selector.value)
}

function onImportInputChange(ev) {
  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
  var fileInput = document.getElementById('import-input');
  var formData = new FormData();
  formData.append('file', fileInput.files[0]);
  axios({
    method: 'post',
    url: '/import/',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data',
    }
  }).then(response => {

  }).catch(error => {
    console.error(error)
  })
}

options = {}

document.addEventListener('DOMContentLoaded', function() {
    load_school_list();

    var navs = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(navs, options);
  
    var tabs = document.querySelector('.tabs');
    var instance = M.Tabs.init(tabs, options);

    var exportButton = document.getElementById('export-button')
    exportButton.addEventListener('click', onExportButtonClick)

    var importButton = document.getElementById('import-input')
    importButton.addEventListener('change', onImportInputChange)

    init_fill('.workarea')
    window.onresize = function(){
      init_fill('.workarea')
    }
});