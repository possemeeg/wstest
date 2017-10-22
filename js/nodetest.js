var Stomp = require('stompjs')
var sleep = require('sleep');
var console = require('console')
//var SockJS = require('sockjs-client')
//var sockjs = require('sockjs');

//var socket = new sockjs.constructor('/gs-guide-websocket')
//var socket = new SockJS('http://localhost:8080/gs-guide-websocket')
//var socket = new SockJS('/gs-guide-websocket')
var client = Stomp.overWS('stomp://192.168.1.21:61613');
//var client = Stomp.over(socket);

client.connect('hello', 'pawd', function(frame) {
      // called back after the client is connected and authenticated to the STOMP server
    console.log('connected: ' + frame)
    client.send('/queue/mailbox', {}, '{}')
    //client.subscribe('/queue/mailbox', function(greeting) {
    //    console.log('subscribed')
    //    console.log(greeting.body);
    //});
    sleep.sleep(10)
})

