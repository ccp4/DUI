import 'dart:io';
import 'dart:convert';

void main(){
    // from pyhton socket example: ('localhost', 8089)
    WebSocket.connect('ws://localhost:8089/').then(
        (socket) {
            socket.send("Hi");
            /*
            socket.add('Hello, World 1');
            socket.add('Hello, World 2');
            */

            socket.send("Hi");

        }
    );
}
