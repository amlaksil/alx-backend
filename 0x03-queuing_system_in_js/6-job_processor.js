const kue = require('kue');

const push_notification_code = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
// Queue process that listens to new jobs on push_notification_code
const job = push_notification_code.process('sms', (job, done) => {
	// Extract phoneNumber and message from job data
	const { phoneNumber, message } = job.data;

	sendNotification(phoneNumber, message);

	// Mark the job as completed
	done();
});
