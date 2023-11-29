import { createClient } from 'redis'

// Create a Redis client and handle errors
const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error}`));

// Subscribe to a channel
client.subscribe('holberton school channel');

// Handle messages received on the subscribed channel
client.on('message', (channel, message) => {
	if (message === 'KILL_SERVER') {
		client.unsubscribe(channel);
		client.quit();
	}
	console.log(message);
});
