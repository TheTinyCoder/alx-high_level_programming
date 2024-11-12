const ready = runDocument => document.readyState !== 'loading'
  ? runDocument()
  : document.addEventListener('DOMContentLoaded', runDocument);
ready(() => {
  document.querySelector('header').style.color = '#FF0000';
});
