const kue = require('kue');

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

const push_notification_code_2 = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
	// Start tracking progress
	job.progress(0, 100);

	if (blacklistedNumbers.includes(phoneNumber)) {
		// Phone number is blacklisted
		const errorMessage = `Phone number ${phoneNumber} is blacklisted`;

		//console.error(`Notification job #${job.id} failed:`, errorMessage);
		done(new Error(errorMessage));
	} else {
		job.progress(50);
		console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

		// Simulating the completion of the job
		setTimeout(() => {
			job.progress(100);
			done();
		}, 2000);
	}
}

// Process jobs from the queue
const job = push_notification_code_2.process('sms', 2, (job, done) => {
	// Extract phoneNumber and message from job data
	const { phoneNumber, message } = job.data;
	
	sendNotification(phoneNumber, message, job, done);
});
