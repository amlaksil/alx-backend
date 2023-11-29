const kue = require('kue');

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('sms', {
	phoneNumber: typeof 'string',
	message: typeof 'string',
	}).save((err) => {
		if (err) {
			console.error('Notification job failed', err);
		} else {
			console.log('Notification job created:', job.id);
		}
	});

job.on('completed', () => console.log('Notification job completed'));
