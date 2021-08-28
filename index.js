

// npm install package.json 


// this runs the code:
// node index.js

const fetch = require("node-fetch");


// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
    console.log('Ready!');

});



async function callModel(text) {

  console.log('Calling model...');

    try
    {
        const settings = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',},
            body: JSON.stringify({'text': text})
        }; 
        // const fetchResponse = await fetch('/submit_text', settings);
        const fetchResponse = await fetch('http://localhost:8111/submit_text', settings);

        const response = await fetchResponse.json();

        console.log(response);
        // console.log(response['hey']);
        return response['hey'];

        // script = response['script']

        // var F = new Function (script);
        // F();

    }
    catch (e)
    {
        console.log('error2', e);
        return e;
    }
}






client.on('message', async message => {

    if (message.author.bot) return;


    if (message.content.startsWith(`To Torn:`)) {

        console.log(message.content);

        words = await callModel(message.content);

        if (words.length > 0) {
            message.channel.send(words);
        }

    }
    

    // // if (message.content.startsWith(`bot:`)) {
    // if (message.content === '!ping') {
    //     // send back "Pong." to the channel the message was sent in
    //     message.channel.send('!ping');
    // }
});

// login to Discord with your app's token
client.login('ODI2MTU5NTkyNjE4MDY1OTMw.YGIbFA.JJEAYBuW9VcOVtp1dpmpIeS4_z0');












