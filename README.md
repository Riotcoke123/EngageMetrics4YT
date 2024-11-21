<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
        <img src="https://github.com/user-attachments/assets/99f3051c-76e7-48d5-b921-6a3846358ece" alt="RealView Audit Tool Overview" style="width:17%;max-width:50px;">

<h1>YouTube Stream Insight</h1>
<p>Welcome to the <strong>YouTube Stream Insight</strong> project! This tool analyzes live stream metrics from YouTube to provide insights into viewer engagement, real vs. bot viewers, and overall stream health. The <strong>Beta Test 0.2</strong> release includes improvements to viewer estimation algorithms and stream data fetching, along with enhanced error handling and logging features. We are actively working on refining these features based on user feedback.</p>

<h2>Features</h2>
<ul>
    <li>Fetch live stream details, including view count and engagement score.</li>
    <li>Estimate real and bot viewers based on engagement score, with dynamic thresholds for various levels of engagement.</li>
    <li>Improved viewer estimation logic that distinguishes between real viewers and bot activity.</li>
    <li>Save data to a JSON file for further analysis or reporting.</li>
    <li>Real-time logging for better tracking and debugging of API interactions.</li>
</ul>

<h2>Installation</h2>
<pre><code>pip install google-api-python-client</code></pre>
<p>Ensure you have Python installed and use pip to install the required package.</p>

<h2>Usage</h2>
<ol>
    <li>Replace the <code>video_id</code> in the main function with the ID of the live stream you want to analyze.</li>
    <li>Update the <code>api_key</code> variable with your YouTube API key.</li>
    <li>Run the script to fetch live stream details and estimate real vs. bot viewers.</li>
    <li>The results will be saved as a <code>data.json</code> file on your local system, containing the stream’s username, total viewers, engagement score, bot viewers, and real viewers.</li>
</ol>

<h2>Code Updates in Beta Test 0.2</h2>
<p>The following improvements have been made in the Beta Test 0.2 release:</p>
<ul>
    <li>The engagement score is now generated directly when fetching live stream details, streamlining the workflow.</li>
    <li>Real viewers are estimated first, based on engagement score thresholds, followed by bot viewers as the difference.</li>
    <li>Improved logic for calculating real and bot viewers with more accurate estimates based on dynamic engagement thresholds.</li>
    <li>Added error handling in key functions, ensuring smoother execution even when some data is unavailable.</li>
    <li>Updated logging for better insight into API requests and response data.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the <strong>GNU General Public License v3.0</strong>.</p>

<h2>Contributions</h2>
<p>Contributions are welcome! Feel free to fork the repository and submit pull requests. We appreciate any help in making this tool better, including suggestions for improving the real vs. bot viewer detection algorithms.</p>

</body>
</html>
