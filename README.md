<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Lazada_Price_Drop_Alerts_0"></a>Lazada Price Drop Alerts</h1>
<p class="has-line-data" data-line-start="1" data-line-end="3"><a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="made-with-python"></a> <a href="https://github.com/ngeks/lazada-price-drop-alerts/blob/main/LICENSE"><img src="https://badgen.net/github/license/Naereen/Strapdown.js" alt="GitHub license"></a> <a href="https://saythanks.io/to/ngeksdev"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks!"></a><br>
<a href="https://www.buymeacoffee.com/ngeks"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="&amp;quot;Buy Me A Coffee&amp;quot;"></a></p>
<p class="has-line-data" data-line-start="4" data-line-end="5">A python script that can help you keep track of your Lazada product wish list prices. It sends you an email alert whenever there is a price drop.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="How_to_run_the_script_6"></a>How to run the script?</h2>
<h3 class="code-line" data-line-start=7 data-line-end=8 ><a id="Requirements_7"></a>Requirements</h3>
<ul>
<li class="has-line-data" data-line-start="8" data-line-end="9">You must have <code>python</code> installed on your computer.</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">You must have <code>pip</code> installed on your computer.</li>
<li class="has-line-data" data-line-start="10" data-line-end="12">An email account to send out email alerts.</li>
</ul>
<h3 class="code-line" data-line-start=12 data-line-end=13 ><a id="Instructions_12"></a>Instructions</h3>
<ol>
<li class="has-line-data" data-line-start="13" data-line-end="18">
<p class="has-line-data" data-line-start="13" data-line-end="14">First, clone the repository.</p>
<pre><code class="has-line-data" data-line-start="15" data-line-end="17">https://github.com/ngeks/lazada-price-drop-alerts.git
</code></pre>
</li>
<li class="has-line-data" data-line-start="18" data-line-end="22">
<p class="has-line-data" data-line-start="18" data-line-end="19">Then, navigate inside the folder.</p>
<pre><code class="has-line-data" data-line-start="20" data-line-end="22">cd lazada-price-drop-alerts
</code></pre>
</li>
<li class="has-line-data" data-line-start="22" data-line-end="26">
<p class="has-line-data" data-line-start="22" data-line-end="23">Install required packages.</p>
<pre><code class="has-line-data" data-line-start="24" data-line-end="26">pip install -r requirements.txt
</code></pre>
</li>
<li class="has-line-data" data-line-start="26" data-line-end="48">
<p class="has-line-data" data-line-start="26" data-line-end="27">Set environment variables.</p>
<pre><code class="has-line-data" data-line-start="28" data-line-end="35">export DATA_FILE=&quot;CSV_FILE_LOCATION&quot;
export SMTP_ADDRESS=&quot;SMTP_SERVER_ADDRESS&quot;
export SMTP_PORT=0000
export FROM_EMAIL=&quot;SENDER_EMAIL_ADDRESS&quot;
export FROM_EMAIL_PW =&quot;SENDER_EMAIL_ADDRESS_PW&quot;
export TO_EMAIL=&quot;RECIPIENT_EMAIL_ADDRESS&quot;
</code></pre>
<p class="has-line-data" data-line-start="35" data-line-end="36">Example:</p>
<pre><code class="has-line-data" data-line-start="37" data-line-end="44">export DATA_FILE=&quot;products.csv&quot;
export SMTP_ADDRESS=&quot;smtp.gmail.com&quot;
export SMTP_PORT=587
export FROM_EMAIL=&quot;alertsender@gmail.com&quot;
export FROM_EMAIL_PW =&quot;thesenderemailpw.&quot;
export TO_EMAIL=&quot;alertrecipient@gmail.com&quot;
</code></pre>
<p class="has-line-data" data-line-start="45" data-line-end="47"><em>Optional: If you are using gmail make sure to turn on your less secure apps access.</em><br>
<em>Manage your Google account -&gt; Security -&gt; Turn on <strong>Less secure app access</strong></em></p>
</li>
<li class="has-line-data" data-line-start="48" data-line-end="57">
<p class="has-line-data" data-line-start="48" data-line-end="49">Run <code>main.py</code> to manage product data.</p>
<pre><code class="has-line-data" data-line-start="50" data-line-end="52">pyton main.py
</code></pre>
<pre><code class="has-line-data" data-line-start="53" data-line-end="57">- View products
- Add product
- Remove product
</code></pre>
</li>
<li class="has-line-data" data-line-start="57" data-line-end="62">
<p class="has-line-data" data-line-start="57" data-line-end="58">Run <code>alerts.py</code> to check for price drop and send email alert.</p>
<pre><code class="has-line-data" data-line-start="59" data-line-end="61">python alerts.py
</code></pre>
</li>
</ol>
<h2 class="code-line" data-line-start=62 data-line-end=63 ><a id="License_62"></a>License</h2>
<p class="has-line-data" data-line-start="63" data-line-end="64">Distributed under <a href="https://github.com/ngeks/lazada-price-drop-alerts/blob/main/LICENSE">MIT License</a>.</p>
<h2 class="code-line" data-line-start=65 data-line-end=66 ><a id="Links_65"></a>Links</h2>
<p class="has-line-data" data-line-start="66" data-line-end="69">Repository: <a href="https://github.com/ngeks/lazada-price-drop-alerts">https://github.com/ngeks/lazada-price-drop-alerts</a><br>
Twitter: <a href="https://twitter.com/ngeksdev">@ngeksdev</a><br>
Email: <a href="mailto:ngeksdev@gmail.com">ngeksdev@gmail.com</a></p>