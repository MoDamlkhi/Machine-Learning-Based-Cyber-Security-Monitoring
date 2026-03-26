# AI-Powered Cyber Security Monitoring System 🛡️

An advanced Network Intrusion Detection System (NIDS) built with Machine Learning and Streamlit. This system processes raw network traffic (PCAP) and identifies potential cyber threats in real-time.

## 🚀 System Architecture


The project follows a comprehensive pipeline:
1. **Traffic Capture**: Collecting raw packets using tools like Wireshark or Tcpdump.
2. **Feature Extraction**: Converting PCAP files into structured data (57 features) using **NFStreamer**.
3. **Preprocessing**: Scaling and encoding data for the ML model.
4. **Classification**: Detecting attacks (e.g., DoS, PortScan, DDoS) using a trained Random Forest model.
5. **Visualization**: Interactive web dashboard built with **Streamlit**.

## 📊 Dataset & Features
The model was trained on the **CICIDS2017** dataset, which is a benchmark for modern network attacks. 
- **Features extracted**: 57 flow-based features (Duration, Packet length, IAT, Flag counts, etc.).
- **Tools used**: NFStreamer (for high-performance flow analysis).

## 📈 Performance Results
| Metric | Score |
| :--- | :--- |
| **Accuracy** | 99.7% |
| **Precision** | 98.5% |
| **Recall** | 98.7% |
| **F1-Score** | 98.6% |

## 🛠️ Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python (Scikit-learn, Pandas, Numpy)
- **Traffic Analysis**: NFStreamer
- **Deployment**: Streamlit Cloud

## 💻 How to use
1. Upload your `.pcap` or `.csv` network traffic file.
2. The system will automatically extract features and analyze the traffic.
3. View the classification results and security alerts instantly.
4.
