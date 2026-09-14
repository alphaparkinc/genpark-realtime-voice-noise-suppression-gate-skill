import json, sys
from client import RealtimeVoiceNoiseSuppressionGateClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "voice-noise-suppression", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "filter_acoustic_noise", "description": "Filters ambient acoustic background noise and computes SNR for voice agents."}]}}
    elif method == "tools/call":
        client = RealtimeVoiceNoiseSuppressionGateClient()
        res = client.filter_acoustic_noise()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = RealtimeVoiceNoiseSuppressionGateClient()
        print(json.dumps(client.filter_acoustic_noise(), indent=2))
