<h2>Read 2 Amazon SQS Queues in Parallel</h2>
<ul>
<li>Open btwoqs.py and addmsg.py in Visual Studio code.
<li>Run btwoqs.py to poll every second for new messages in all your queues.
<li>In addmsg.py, change 'count' and 'queues' as per your need and run it to add messages in a batch with a time stamp on each, which will allow you to easily distinguish messages.
</ul>
<hr>
<i>Note: Ensure you have AWS configured correctly so that boto3 can access your queues!!</i>
