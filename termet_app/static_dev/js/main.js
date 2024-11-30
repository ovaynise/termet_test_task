document.getElementById('setVolumeForm').onsubmit = function (e) {
  e.preventDefault();
  const volume = document.getElementById('volume').value;

  fetch('', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value },
    body: JSON.stringify({ action: 'set_volume', volume: volume }),
  })
    .then((response) => response.json())
    .then((data) => alert(data.message))
    .catch((error) => alert('Ошибка: ' + error));
};