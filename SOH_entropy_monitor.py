import numpy as np
import uuid
from datetime import datetime

class SOHMetabolicMonitor:
    """
    SOH v2.0 - Self-Organizing Homeostasis
    Implements Shannon Entropy to detect 'Metabolic Stress' in AI Inference.
    """
    def __init__(self, threshold=0.8):
        self.threshold = threshold  # Homeostatic Range Limit

    def calculate_entropy(self, probabilities):
        """
        Calculates Shannon Entropy: H(P) = -sum(Pi * log(Pi))
        """
        # Ensure probabilities sum to 1
        probs = np.array(probabilities)
        # Avoid log(0)
        entropy = -np.sum(probs * np.log2(probs + 1e-9))
        return entropy

    def generate_forensic_metadata(self, entropy):
        """
        Generates Typed gRPC-compliant Metadata for auditing.
        """
        status = "NORMAL" if entropy < self.threshold else "METABOLIC_STRESS"
        
        metadata = {
            "trace_id": str(uuid.uuid4()),
            "timestamp_ns": int(datetime.utcnow().timestamp() * 1e9),
            "entropy_score": round(entropy, 4),
            "homeostatic_status": status,
            "action": "GRACEFUL_DEGRADATION" if status == "METABOLIC_STRESS" else "CONTINUE"
        }
        return metadata

# --- TEST CASE ---
if __name__ == "__main__":
    monitor = SOHMetabolicMonitor(threshold=0.7)

    # Simulation 1: Confident Prediction (Low Entropy)
    confident_output = [0.95, 0.02, 0.03]
    h1 = monitor.calculate_entropy(confident_output)
    
    # Simulation 2: Confused Prediction (High Entropy / Hallucination Risk)
    confused_output = [0.4, 0.3, 0.3]
    h2 = monitor.calculate_entropy(confused_output)

    print(f"SOH v2.0 Audit Log:\n{'-'*30}")
    print(f"Audit 1: {monitor.generate_forensic_metadata(h1)}")
    print(f"Audit 2: {monitor.generate_forensic_metadata(h2)}")
