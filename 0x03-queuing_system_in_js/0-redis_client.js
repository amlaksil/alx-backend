import { createClient } from 'redis';

const client = createClient()
	.on('connect', () => console.log('Redis client connected to the server'))
	.on('error', (error) => console.error(`Redis client not connected to the server: ${error}`));
