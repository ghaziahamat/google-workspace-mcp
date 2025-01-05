# Google Workspace MCP Servers

A collection of Model Context Protocol (MCP) servers that enable secure access to Google Workspace services through Large Language Models like Claude. This project includes three independent servers:

- **Gmail MCP Server**: Search emails, read content, and manage labels
- **Calendar MCP Server**: View events and check availability
- **Drive MCP Server**: Search and organize files and folders

## Prerequisites

- Windows 10 or later
- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/) (required for `npx`)
- [Claude Desktop](https://claude.ai/download)
- A Google Cloud project with OAuth 2.0 credentials

## Setup Instructions

### 1. Google Cloud Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs:
   - Gmail API
   - Google Calendar API
   - Google Drive API
4. Configure OAuth 2.0:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop application"
   - Download the credentials and rename to `client_secrets.json`

### 2. Project Setup

```powershell
# Create project directory
uv init google-workspace-mcp
cd google-workspace-mcp

# Create virtual environment and activate it
uv venv
.venv\Scripts\activate

# Install required packages
uv add mcp[cli] google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 3. Project Structure

Create the following directory structure:

```
google-workspace-mcp/
├── .venv/
├── client_secrets.json            # Your OAuth credentials
├── gmail_server/
│   ├── __init__.py
│   └── main.py
├── calendar_server/
│   ├── __init__.py
│   └── main.py
├── drive_server/
│   ├── __init__.py
│   └── main.py
└── shared/
    ├── __init__.py
    └── auth.py
```

### 4. Configure Claude Desktop

1. Open Claude Desktop
2. Click on the Claude menu and select "Settings..."
3. Click on "Developer" in the left sidebar
4. Click "Edit Config"
5. Replace the contents with the configuration provided in the `claude_config.json` file

**Important**: Replace `C:\path\to\google-workspace-mcp` with your actual project path.

## Available Features

### Gmail Server

Resources:
- `messages/{message_id}`: Get contents of specific emails
- `labels`: List all available Gmail labels

Tools:
- `search_emails`: Search emails using Gmail's query syntax
- `apply_label`: Apply or create labels for emails

Example queries:
- "Search my emails for messages about project deadlines"
- "Find emails from john@example.com from last week"
- "Add a 'Follow-up' label to my last email from Alice"

### Calendar Server

Resources:
- `events/{time_min}/{time_max}`: Get calendar events within a time range
- `calendars`: List all available calendars

Tools:
- `check_availability`: Check free/busy status for a given date

Example queries:
- "What meetings do I have tomorrow?"
- "Am I free next Tuesday afternoon?"
- "Show me all my events for this week"

### Drive Server

Resources:
- `files/{file_id}`: Get contents of specific files
- `folders/{folder_id}`: List contents of specific folders

Tools:
- `search_files`: Search files and folders
- `move_file`: Move files between folders

Example queries:
- "Find all PDF files related to project X"
- "What documents are in my Reports folder?"
- "Move my recent presentations to the Meeting Materials folder"

## Troubleshooting

### Authentication Issues

If you encounter authentication problems:
1. Check that `client_secrets.json` is in the correct location
2. Delete any existing `token_*.pickle` files to force re-authentication
3. Ensure all required Google Cloud APIs are enabled

### Server Connection Issues

If Claude can't connect to the servers:
1. Check Claude's logs at `%APPDATA%\Claude\logs\mcp*.log`
2. Verify paths in `claude_desktop_config.json` are correct
3. Ensure the virtual environment is activated
4. Restart Claude Desktop

### Common Error Messages

- "Failed to start server": Check that all paths in the configuration are correct
- "Authentication failed": Verify your OAuth credentials
- "API not enabled": Enable the required API in Google Cloud Console

## Logs and Debugging

Server logs can be found at:
- `%APPDATA%\Claude\logs\mcp-server-gmail.log`
- `%APPDATA%\Claude\logs\mcp-server-calendar.log`
- `%APPDATA%\Claude\logs\mcp-server-drive.log`

To view logs in real-time:
```powershell
Get-Content -Path "%APPDATA%\Claude\logs\mcp*.log" -Wait
```

## Security Notes

- All servers operate in read-only mode for their respective services
- OAuth tokens are stored locally in `token_*.pickle` files
- Each service maintains its own authentication token
- Permission requests are shown to the user during first authentication

## Contributing

We welcome contributions! Please see our contributing guidelines for more information.

## License

This project is licensed under the MIT License - see the LICENSE file for details.