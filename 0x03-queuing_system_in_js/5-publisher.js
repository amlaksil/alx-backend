import { createClient } from 'redis'

// Create a Redis client and handle errors
const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error}`));

function publishMessage(message, time) {
	// Publish a message to the channel after a delay
	setTimeout(() => {
		console.log(`About to send ${message}`);
		client.publish('holberton school channel', message);}, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
