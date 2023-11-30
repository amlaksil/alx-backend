const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Create a queue with kue
const push_notification_code_2 = kue.createQueue();

jobs.forEach((jobData) => {
	// Create a job and save it to the queue
	const job = push_notification_code_2.create('sms', jobData)
	.save((err) => {
		if (err) {
			console.error('Notification job failed', err);
		} else {
			console.log('Notification job created:', job.id);
		}
	});
	job.on('failed', (err) => console.error(`Notification job #${job.id} failed: ${err}`));
	job.on('progress', (progress) => console.log(`Notification job #${job.id} ${progress}% complete`));
	job.on('completed', () => console.log(`Notification job #${job.id} completed`));
});
