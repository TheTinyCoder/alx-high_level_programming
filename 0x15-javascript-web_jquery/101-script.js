document.getElementById('add_item').addEventListener('click', () => {
  const item = document.createElement('li');
  item.innerHTML = 'Item';
  document.getElementsByClassName('my_list').appendChild(item);
});

document.getElementById('remove_item').addEventListener('click', () => {
  const list = document.getElementsByClassName('my_list');
  list.removeChild(list.lastElementChild);
});

document.getElementById('clear_list').addEventListener('click', () => {
  const list = document.getElementsByClassName('my_list');
  list.replaceChildren();
});
