
06/08/2025

# Antenna

## 🎯 Goals

Antenna provides the essential building blocks for **developer-first robotics workflows**—without imposing a UI or closed ecosystem.

### ✅ 1. Real-Time Control & Telemetry  
- Enable device apps (iPadOS, web, desktop) to send actuator commands and receive motor/servo/sensor data in real time via HTTP and WebSocket.  
- Target sub-100 ms latency on local networks for fluid manual control and debugging.

### ✅ 2. Seamless Recording for ML Pipelines  
- Support `/start-recording`, `/stop-recording`, and live event logging as **JSONL or Parquet**.  
- Capture rich input/output event streams compatible with Rerun, Hugging Face Datasets, or your own tools.

### ✅ 3. Modular & Extensible Architecture  
- Remain **robot-agnostic**, supporting SO‑101, demo arms, DIY rigs via simple adapter plugins.  
- Ship with **no UI by default**, giving developers freedom to integrate iPad, web, or desktop clients.

### ✅ 4. Open Data & Interoperability  
- Include an endpoint to **publish recorded episodes to Hugging Face** with minimal configuration.  
- Use standard, tool-friendly data formats to encourage integration into dashboards, ML workflows, or analytics setups.


# Running

`uvicorn main:app --reload`

