const input = document.getElementById("user-input");
const chatContainer = document.getElementById("chat");
const sendButton = document.getElementById("send");

eel.expose(send_bot_response);

function send_bot_response(text) {
  add_message(text, "bot-message");
}

function send_user_message(text) {
  add_message(text, "user-message");
}

function add_message(text, class_name) {
  let message = document.createElement("p");
  message.innerHTML = text;
  message.classList.add(class_name);
  message.classList.add("message");
  chatContainer.appendChild(message);
}

sendButton.onclick = () => {
  if (input.value !== "") {
    send_user_message(input.value);
    eel.query_bot(input.value);
    input.value = "";
  }
};
