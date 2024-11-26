document.addEventListener("DOMContentLoaded", () => {

  document.getElementById("setVolumeForm").onsubmit = function (e) {
    e.preventDefault();


    const volume = document.getElementById("volume").value;


    fetch("", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
      body: JSON.stringify({ action: "set_volume", volume: volume }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Ошибка сервера");
        }
        return response.json();
      })
      .then((data) => {
        alert(data.message);
        console.log(data.message);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
        alert("Произошла ошибка при установке объема контейнера.");
      });
  };


  document.getElementById("addMessageForm").onsubmit = function (e) {
    e.preventDefault();


    const text = document.getElementById("text").value;


    fetch("", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
      body: JSON.stringify({ action: "add_message", text: text }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Ошибка сервера");
        }
        return response.json();
      })
      .then((data) => {
        alert(data.message);
        console.log(data.message);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
        alert("Произошла ошибка при добавлении сообщения.");
      });
  };


  document.getElementById("searchMessageForm").onsubmit = function (e) {
    e.preventDefault();


    const text = document.getElementById("search_text").value;

    fetch("", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
      body: JSON.stringify({ action: "search_message", text: text }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Ошибка сервера");
        }
        return response.json();
      })
      .then((data) => {
        alert(data.message);
        console.log(data.message);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
        alert("Произошла ошибка при поиске сообщения.");
      });
  };
});