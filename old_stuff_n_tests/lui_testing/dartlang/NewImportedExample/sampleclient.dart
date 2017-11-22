import 'dart:html';

void main() {
  TextInputElement input = querySelector('#input');
  ParagraphElement output = querySelector('#output');

  String server = 'ws://localhost:8080/';
  WebSocket ws = new WebSocket(server);
  ws.onOpen.listen((Event e) {
    outputMessage(output, 'Connected to server');
  });

  ws.onMessage.listen((MessageEvent e){
    outputMessage(output, e.data);
  });

  ws.onClose.listen((Event e) {
    outputMessage(output, 'Connection to server lost...');
  });

  input.onChange.listen((Event e){
    ws.send(input.value.trim());
    input.value = "";
  });
}

void outputMessage(Element e, String message){
  print(message);
  e.appendText(message);
  e.appendHtml('<br/>');

  //Make sure we 'autoscroll' the new messages
  e.scrollTop = e.scrollHeight;
}