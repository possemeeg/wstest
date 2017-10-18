var Stomp = require('stompjs')
var sleep = require('sleep');
var console = require('console')
var SockJS = require('sockjs-client')
//var sockjs = require('sockjs');

//var socket = new sockjs.constructor('/gs-guide-websocket')
var socket = new SockJS('http://localhost:8080/gs-guide-websocket')
//var socket = new SockJS('/gs-guide-websocket')
//var client = Stomp.overWS('ws://localhost:8080/gs-guide-websocket/055/o0vba17k/websocket');
var client = Stomp.over(socket);

client.connect('hello', 'pawd', function(frame) {
      // called back after the client is connected and authenticated to the STOMP server
    console.log('connected: ' + frame)
    client.subscribe('/topic/greetings', function(greeting) {
        console.log('subscribed')
        console.log(greeting.body);
    });
    sleep.sleep(10)
})

