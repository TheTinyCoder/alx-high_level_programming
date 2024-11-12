$('document').ready(() => {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    $.each(data.results, (key, val) => {
      $('#list_movies').append(`<li>${val.title}</li>`);
    });
  });
});
