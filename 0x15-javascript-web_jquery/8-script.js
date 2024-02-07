$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    data.results.forEach(film => {
      const item = $('<li></li>').text(film.title);
      $('#list_movies').append(item);
    });
  });
});
