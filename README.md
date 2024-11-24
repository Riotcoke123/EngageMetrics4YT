<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
    <img src="https://github.com/user-attachments/assets/99f3051c-76e7-48d5-b921-6a3846358ece" alt="RealView Audit Tool Overview" style="width:17%;max-width:50px;">
    <h1>YouTube Stream Insight</h1>
    <p>Welcome to the <strong>YouTube Stream Insight</strong> project! This tool analyzes live stream metrics from YouTube to provide insights into viewer engagement, real vs. bot viewers, and overall stream health. The <strong>Version 0.2 Update</strong> introduced new features, refined algorithms, and improved performance. The <strong>Version 0.2a Update</strong> focuses on further enhancements, including bug fixes and minor optimizations.</p>
    <h2>Features</h2>
    <ul>
        <li>Fetch live stream details, including view count, engagement score, and channel username.</li>
        <li>Dynamic thresholds to estimate real viewers and bot activity based on engagement levels.</li>
        <li>Save processed data to a structured <code>JSON</code> file for detailed reporting and analysis.</li>
        <li>Enhanced error handling to manage incomplete or missing data gracefully.</li>
        <li>Comprehensive real-time logging to track API interactions and debug issues effectively.</li>
        <li>Support for fetching and analyzing data from YouTube live streams using the YouTube API v3.</li>
        <li>Optimized data handling and processing for smoother performance in production environments.</li>
    </ul>
    <h2>Installation</h2>
    <pre><code>pip install google-api-python-client</code></pre>
    <p>Ensure Python is installed on your system. Use <code>pip</code> to install the necessary dependencies.</p>
    <h2>Usage</h2>
    <ol>
        <li>Update the <code>api_key</code> variable in the script with your YouTube API key.</li>
        <li>Replace the <code>video_id</code> with the ID of the live stream you wish to analyze.</li>
        <li>Run the script using Python:</li>
        <pre><code>python script_name.py</code></pre>
        <li>The output will be saved as a <code>data.json</code> file in the specified path. This file contains:</li>
        <ul>
            <li>Username (channel name)</li>
            <li>Total viewers</li>
            <li>Engagement score</li>
            <li>Real viewers</li>
            <li>Bot viewers</li>
        </ul>
    </ol>
    <h2>Changelog (Version 0.2 - 0.2a Update)</h2>
    <p>The following updates and improvements have been made in Version 0.2:</p>
    <ul>
        <li><strong>Improved Viewer Estimation:</strong> Real viewer estimation is now more accurate, using dynamic thresholds tailored to engagement scores. The logic adjusts depending on the engagement score (e.g., high engagement results in more real viewers).</li>
        <li><strong>Error Handling Enhancements:</strong> Added robust try-except blocks to manage API failures, missing fields, and invalid responses more effectively, ensuring that the application runs smoothly even when data is incomplete.</li>
        <li><strong>JSON Output Formatting:</strong> Output JSON files are now more readable, with structured indentation and clear labeling of key metrics, making it easier to parse and analyze the data.</li>
        <li><strong>Logging Improvements:</strong> Detailed logs for each step of the process, including API requests, responses, and any processing errors, are written to a log file for easier debugging and tracking.</li>
        <li><strong>Code Refactoring:</strong> The code has been modularized into well-defined functions, improving maintainability and performance. Key functionalities like YouTube API initialization, live stream data fetching, viewer estimation, and saving data are now encapsulated in separate functions.</li>
    </ul>
    <p>The following updates have been made in Version 0.2a:</p>
    <ul>
        <li><strong>Bug Fixes:</strong> Addressed issues with incorrect viewer count when the API returns incomplete data. The script now ensures the accurate reporting of viewers even when certain fields are missing or null.</li>
        <li><strong>Optimization:</strong> Improved the speed of processing by streamlining the estimation algorithms and reducing unnecessary API calls, resulting in a faster and more responsive user experience.</li>
        <li><strong>New Data Validation:</strong> Added additional checks to validate that the fetched data is consistent before processing, ensuring that only complete and accurate data is used for analysis.</li>
        <li><strong>Additional Logging:</strong> Expanded logging functionality to provide more detailed insights into each function's execution, making it easier to track issues and performance bottlenecks.</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the <strong>GNU General Public License v3.0</strong>. You are free to use, modify, and distribute this project under the same license.</p>
    <h2>Contributions</h2>
    <p>We welcome contributions! If you have suggestions, bug reports, or feature requests, feel free to fork the repository and submit a pull request. Let’s make this tool better together!</p>
</body>
</html>

