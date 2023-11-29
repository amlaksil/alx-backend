import { createClient } from 'redis'

const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error}`));

client.hset('HolbertonSchools', 'Portland', 50, (error, result) => {
	if (error) {
		console.error(error);
	} else {
		console.log('Reply:', result);
	}
});

client.hset('HolbertonSchools', 'Seattle', 80, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Reply:', result);
  }
});

client.hset('HolbertonSchools', 'New York', 20, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Reply:', result);
  }
});

client.hset('HolbertonSchools', 'Bogota', 20, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Reply:', result);
  }
});

client.hset('HolbertonSchools', 'Cali', 40, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Reply:', result);
  }
});

client.hset('HolbertonSchools', 'Paris', 2, (error, result) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Reply:', result);
  }
});

client.hgetall('HolbertonSchools', (error, result) => {
	if (error) {
		console.error(error);
	} else {
		console.log(result);
	}
});
