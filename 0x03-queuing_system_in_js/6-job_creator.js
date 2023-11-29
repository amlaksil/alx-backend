const kue = require('kue');

// Create a queue with kue
const push_notification_code = kue.createQueue();

// Create a job with job data
const job = push_notification_code.create('sms', {
	phoneNumber: '4153518780',
	message: 'This is the code to verify your account'
	}).save((err) => {
		if (err) {
			console.error('Notification job failed', err);
		} else {
			console.log('Notification job created:', job.id);
		}
	});

job.on('completed', () => console.log('Notification job completed'));
