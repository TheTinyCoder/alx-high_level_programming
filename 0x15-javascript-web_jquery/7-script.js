$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, textStatus) => {
    $('#character').text(data.name);
  });
});
