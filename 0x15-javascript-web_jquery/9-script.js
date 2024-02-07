$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data, textStatus) => {
    $('#hello').text(data.hello);
  });
});
