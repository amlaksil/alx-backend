import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient()
	.on('connect', () => console.log('Redis client connected to the server'))
	.on('error', (error) => console.error(`Redis client not connected to the server: ${error}`));

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
	try {
		const reply = await setAsync(schoolName, value);
		console.log('Reply:', reply);
	} catch (error) {
		console.error(error);
	}
}

async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (error) {
		console.log(error);
	}
}

async function main() {
	await displaySchoolValue('Holberton');
	await setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
}

// Invoke the main function
main()
