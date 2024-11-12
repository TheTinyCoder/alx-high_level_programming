$('document').ready(() => {
  function trigger () {
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`;
    $.getJSON(url, (data) => {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').on('click', trigger);
  $('#language-code').on('keypress', (event) => { if (event.which === 13) trigger(); });
});
