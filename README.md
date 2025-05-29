ProxyPunk

🔍 ProxyPunk is a cheeky proxy that not only listens but also automatically parses, extracts, and prepares requests for attack tools like nuclei, x8, and more.

It’s designed for researchers, bug bounty hunters, and hackers who want to capture endpoints on the fly and immediately test them.
Features

✅ Captures HTTP/HTTPS traffic using mitmproxy
✅ Outputs structured requests (headers, body)
✅ Extracts URLs, cookies, and other juicy details
✅ Automatically kicks off attack tools (planned!)
✅ Simple YAML configuration
✅ Easy to extend
Installation

1️⃣ Clone the repo:

git clone https://github.com/yourname/ProxyPunk.git
cd ProxyPunk

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Make sure you have mitmdump installed:

sudo apt install mitmproxy

Configuration

Edit config.yaml:

listen_host: 127.0.0.1
listen_port: 1332

✅ Tip: We recommend running on localhost for safe testing.
Usage

Start the proxy:

python run_mitm.py

It will:

    Launch mitmdump with your settings

    Run the script dump_requests.py from the current directory

    Print formatted requests to the console

Planned Features

✨ Automatically extract URLs and cookies
✨ Run attack tools like nuclei or x8 on captured endpoints
✨ Save interesting findings to output files
✨ Add filtering and scope management
Example

Here’s how a captured request looks in the console:

================================================================================
Request: POST https://target.com/api/login
--------------------------------------------------------------------------------
Host: target.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0
Content-Type: application/json
...

{
    "username": "admin",
    "password": "password123"
}
======================================================
