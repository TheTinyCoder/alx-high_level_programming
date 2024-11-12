$('document').ready(() => {
  $('#btn_translate').on('click', () => {
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${$('#language_code').val()}`;
    $.getJSON(url, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
