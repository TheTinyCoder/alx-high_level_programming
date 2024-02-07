$(document).ready(() => {
  let lang = $('#language_code').val();
  function showHello () {
    $.get(`https://stefanbohacek.com/hellosalut/?lang={lang}`, (data,textStatus) => {
      $('#hello').text(data.hello);
    });
  };
  $('#btn_translate').click(() => {
    showHello();
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
});
