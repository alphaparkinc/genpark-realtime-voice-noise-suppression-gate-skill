import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import RealtimeVoiceNoiseSuppressionGateClient

def main():
    client = RealtimeVoiceNoiseSuppressionGateClient()
    res = client.filter_acoustic_noise()
    print("=== Realtime Voice Noise Suppression Gate Output ===")
    print(f"RMS Energy: {res['frame_rms_energy']} | Level: {res['frame_level_db']} dB")
    print(f"SNR Ratio: {res['signal_to_noise_ratio_db']} dB | Floor: {res['noise_floor_db']} dB")
    print(f"Gate Verdict: {res['spectral_gate_verdict']} (Attenuation: {res['attenuation_applied_db']} dB)")

if __name__ == '__main__':
    main()
