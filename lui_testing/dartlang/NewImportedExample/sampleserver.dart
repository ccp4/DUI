import 'dart:io';
import 'dart:convert';

void main() {
  HttpServer.bind(InternetAddress.ANY_IP_V4, 8080).then((HttpServer server) {
    print("HttpServer listening...");
    server.serverHeader = "DartEcho (1.0) by James Slocum";
    server.listen((HttpRequest request) {
      if (WebSocketTransformer.isUpgradeRequest(request)){
        WebSocketTransformer.upgrade(request).then(handleWebSocket);
      }
      else {
        print("Regular ${request.method} request for: ${request.uri.path}");
        serveRequest(request);
      }
    });
  });
}

void handleWebSocket(WebSocket socket){
  print('Client connected!');
  socket.listen((String s) {
    print('Client sent: $s');
    socket.add('echo: $s');
  },
  onDone: () {
    print('Client disconnected');
  });
}

void serveRequest(HttpRequest request){
  request.response.statusCode = HttpStatus.FORBIDDEN;
  request.response.reasonPhrase = "WebSocket connections only";
  request.response.close();
}