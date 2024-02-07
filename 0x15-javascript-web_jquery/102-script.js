$(document).ready(() => {
  let lang = $('#language_code').val();
  $('#btn_translate').click(() => {
    $.get(`https://stefanbohacek.com/hellosalut/?lang={lang}`, (data,textStatus) => {
      $('#hello').text(data.hello);
    });
  });
});
