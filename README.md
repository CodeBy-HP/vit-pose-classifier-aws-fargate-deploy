<div align="center">

# 🎯  Human Pose Classification API

*Fine-tuned Vision Transformer with AWS Fargate serverless deployment, Application Load Balancing, and automated CI/CD pipeline*

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Fargate%20%7C%20ECS%20%7C%20ECR%20%7C%20ALB-FF9900.svg)](https://aws.amazon.com/)
[![Serverless](https://img.shields.io/badge/Serverless-Fargate-FD5750.svg)](https://aws.amazon.com/fargate/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Transformers-EE4C2C.svg)](https://pytorch.org/)

</div>

---

## 🎯 Overview

Production-grade human pose classification API featuring **fine-tuned Vision Transformer (ViT) model**, **AWS Fargate serverless compute**, **Application Load Balancer**, and **automated CI/CD deployment** with zero-infrastructure management and automatic scaling capabilities.

---

## 🌈 Application UI

<div align="center">
<img width="493" height="858" alt="Screenshot 2025-12-23 232355" src="https://github.com/user-attachments/assets/1a9bcc84-0e43-4327-a866-ea3211715dd5" />
</div>

---

## 🌈 Video Demo

<p align="center">
  <a href="https://youtube.com/" target="_blank">
    <img 
      src="https://img.youtube.com/vi/UcwIQ7bP31Y/maxresdefault.jpg"
      alt="Watch Demo"
      width="700"
    />
  </a>
</p>

<p align="center"><b>▶️ Click to watch architecture & serverless deployment demo</b></p>

---

## 🌈 Architecture Diagrams

<div align="center">

<img width="817" height="1056" alt="Screenshot 2025-12-25 184002" src="https://github.com/user-attachments/assets/8698a773-84dc-4f3e-a91a-1757a9e7cf94" />
<img width="880" height="515" alt="Screenshot 2025-12-25 184702" src="https://github.com/user-attachments/assets/f012f5a2-5f85-45a8-aa89-556bb827e694" />

</div>

---

## CI/CD Pipeline

<div align="center">
<img width="566" height="756" alt="Screenshot 2025-12-25 184028" src="https://github.com/user-attachments/assets/68945957-4715-4ab7-8799-231ffbe8fcb7" />
</div>

---

## ✨ Key Features

### 🧠 **VISION TRANSFORMER MODEL**
- State-of-the-art ViT architecture (google/vit-base-patch16-224-in21k)
- Fine-tuned on human action recognition dataset
- Self-attention mechanism for superior pose understanding
- Transfer learning from ImageNet-21k (14M images)

### ☁️ **AWS FARGATE SERVERLESS**
- Zero server management - fully managed containers
- Pay-per-use pricing (vCPU-seconds + GB-seconds)
- No infrastructure provisioning or maintenance
- Automatic OS patching and security updates

### ⚖️ **APPLICATION LOAD BALANCER**
- Intelligent traffic distribution across Fargate tasks
- Health-check based routing to healthy containers
- Multi-AZ deployment for high availability
- Single DNS endpoint for all requests

### 🚀 **AUTO-SCALING & HIGH AVAILABILITY**
- ECS Service auto-scaling based on CPU/Memory metrics
- Multi-Availability Zone deployment for fault tolerance
- Rolling deployments with zero downtime
- Automatic task replacement on failures

---

## 🛠️ Tech Stack

- **Machine Learning:** PyTorch, Transformers, Vision Transformer (ViT)
- **Backend:** FastAPI, Uvicorn
- **Infrastructure:** Docker, AWS ECS, AWS Fargate
- **Load Balancing:** AWS Application Load Balancer (ALB)
- **Container Registry:** Amazon ECR
- **DevOps & CI/CD:** GitHub Actions, AWS ECS Auto-deployment
- **Monitoring:** CloudWatch Logs & Metrics

---

## 📁 Project Structure

```
human-pose-classification/
├── fastapi_app/
│   ├── app.py                    # FastAPI application with prediction endpoints
│   ├── requirements.txt          # Python dependencies
│   ├── ml-models/
│   │   └── vit-human-pose-classification/
│   │       ├── config.json       # Model configuration
│   │       ├── model.safetensors # Fine-tuned ViT weights
│   │       └── preprocessor_config.json
│   ├── scripts/
│   │   ├── data_model.py        # Pydantic response models
│   │   ├── huggingface_load.py  # Model loader from Hugging Face
│   │   └── s3.py                # S3 model downloader (optional)
│   └── templates/
│       └── index.html           # Web interface for image upload
├── ImageClassification.ipynb    # Model training notebook
├── Dockerfile                   # FastAPI container (Port 8000)
└── README.md
```

---

## 🎓 What I Learned

- Vision Transformer architecture and self-attention mechanisms
- Transfer learning with pre-trained ViT models
- Fine-tuning transformers for image classification
- AWS Fargate serverless container deployment
- ECS cluster and service orchestration
- Application Load Balancer configuration and target groups
- Security groups and VPC networking in AWS
- CloudWatch monitoring and logging
- CI/CD pipeline automation with GitHub Actions
- Serverless architecture benefits (cost, scalability, zero management)
- Docker optimization for ML workloads
- Production-ready ML API design with FastAPI

---

## 🔮 Future Enhancements

- **A/B Testing:** Deploy multiple model versions with traffic splitting
- **Batch Inference:** Support batch prediction endpoints
- **Prometheus Metrics:** Custom metrics export for advanced monitoring
- **SageMaker Integration:** Continuous model retraining pipeline

---


## 🌟 Why Serverless?

### Traditional EC2 Approach vs. Fargate Serverless

| Aspect | EC2 | AWS Fargate |
|--------|-----|-------------|
| **Server Management** | Manual provisioning, patching, scaling | Zero management - fully automated |
| **Scaling** | Configure auto-scaling groups manually | ECS handles automatically |
| **Cost Model** | Pay 24/7 for running instances | Pay only for compute time used |
| **Deployment** | Manage EC2 + Docker separately | Container-native, seamless |
| **High Availability** | Configure across AZs manually | Built-in multi-AZ deployment |
| **Estimated Cost** | $50-100/month (always running) | $20-40/month (low-moderate load) |

---

## 👤 Author

**Harsh Patel**  
📧 code.by.hp@gmail.com  
🔗 [GitHub](https://github.com/CodeBy-HP) • [LinkedIn](https://www.linkedin.com/in/harsh-patel-389593292/)

---

<div align="center">

**⭐ If you find this project helpful, please star it!**

</div>
