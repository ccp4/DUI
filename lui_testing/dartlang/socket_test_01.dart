//import 'dart:html';
import 'dart:io';
import 'dart:convert';
void main() {
  //TextInputElement input = querySelector('#input');
  //ParagraphElement output = querySelector('#output');

  String server = 'ws://localhost:8089/';
  WebSocket ws = new WebSocket(server);

  ws.send("Hi");


  ws.onOpen.listen((Event e) {
    print('Connected to server');
  });

  ws.onMessage.listen((MessageEvent e){
    print(e.data);
  });

  ws.onClose.listen((Event e) {
    print('Connection to server lost...');
  });

  /*
  input.onChange.listen((Event e){
    ws.send(input.value.trim());
    input.value = "";
  });
  */

}