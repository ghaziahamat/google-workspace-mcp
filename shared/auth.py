from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

class GoogleAuth:
    def __init__(self, client_secrets_file: str, scopes: list[str], token_prefix: str):
        self.client_secrets_file = os.path.abspath(client_secrets_file)
        self.scopes = scopes
        self.token_path = os.path.join(
            os.path.dirname(self.client_secrets_file), 
            f'token_{token_prefix}.pickle'
        )
    
    def get_credentials(self) -> Credentials:
        """Handle OAuth flow and token management"""
        creds = None
        if os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                creds = pickle.load(token)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, self.scopes)
                creds = flow.run_local_server(port=0)
            
            with open(self.token_path, 'wb') as token:
                pickle.dump(creds, token)
        
        return creds