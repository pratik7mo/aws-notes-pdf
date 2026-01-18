# aws_content.py

aws_pages = [
    # Page 1: Introduction
    {
        "title": "1. Introduction to Cloud & AWS",
        "subtitle": "Basics",
        "sections": [
            {
                "header": "1. What is Cloud Computing?",
                "body": "Cloud computing is using computing resources like servers and storage over the internet instead of owning hardware—like using <b>Uber</b> instead of buying a car.<br/>You pay only for what you use, avoid maintenance, and can scale resources anytime."
            },
            {
                "header": "2. What is AWS?",
                "body": "AWS (Amazon Web Services) is a cloud platform that provides on-demand services like servers, storage, databases, and networking over the internet.<br/><br/><b>Analogy:</b> It lets users rent computing resources and pay only for what they use—like staying in a <b>Hotel</b> instead of buying a house (no ownership, no maintenance, pay only for the stay)."
            },
            {
                "header": "3. Advantages of AWS",
                "items": [
                    "<b>Pay-as-you-go:</b> No upfront hardware cost.",
                    "<b>Fast resource provisioning:</b> Get started in minutes.",
                    "<b>Easy scalability:</b> Scale up/down anytime.",
                    "<b>High availability and security.</b>"
                ]
            }
        ]
    },
    # Page 2: Compute (EC2 & Lambda)
    {
        "title": "2. Compute Services",
        "subtitle": "EC2 & Lambda",
        "sections": [
            {
                "header": "4. What is EC2?",
                "body": "EC2 (Amazon EC2) is an AWS service that provides virtual servers called instances in the cloud. It allows users to choose required CPU, memory, storage, and OS, and pay only for what they use."
            },
            {
                "header": "EC2 Practical Use (Real-Time)",
                "items": [
                    "Used to host backend applications like Java Spring Boot or Node.js.",
                    "Developer connects using SSH.",
                    "Application code is deployed and started.",
                    "Security Groups control allowed ports.",
                    "Can be scaled manually or using Auto Scaling."
                ],
                "interview": {
                    "question": "One-Line Summary",
                    "answer": "EC2 is used to deploy, run, and manage backend applications on virtual servers in AWS."
                }
            },
            {
                "header": "13. What is AWS Lambda?",
                "body": "Lambda (AWS Lambda) is a serverless service that runs code without managing servers. You upload code, AWS executes it on demand, and you pay only for execution time."
            }
        ]
    },
     # Page 3: Storage & Database
    {
        "title": "3. Storage & Databases",
        "subtitle": "S3 & RDS",
        "sections": [
             {
                "header": "5. What is S3?",
                "body": "S3 (Amazon S3) is an AWS service used to store and retrieve data like files, images, and videos over the internet. It provides highly durable, scalable storage with pay-as-you-go pricing."
            },
            {
                "header": "6. What is RDS?",
                "body": "RDS (Amazon RDS) is an AWS service that provides managed relational databases in the cloud. It handles backups, patching, and scaling automatically, so users can focus on the application instead of database management."
            }
        ]
    },
     # Page 4: Networking & Security
    {
        "title": "4. Networking & Security",
        "subtitle": "VPC, SecGroup, IAM",
        "sections": [
            {
                "header": "7. What is IAM?",
                "body": "IAM (AWS IAM) is an AWS service used to manage users, roles, and permissions. It controls who can access what in AWS securely without sharing passwords."
            },
            {
                "header": "8. What is VPC?",
                "body": "VPC (Amazon VPC) stands for Virtual Private Cloud. It allows you to create a private, isolated network in AWS where you control IP ranges, subnets, routing, and security for your resources."
            },
             {
                "header": "9. What is a Security Group?",
                "body": "A Security Group in AWS acts as a virtual firewall that controls inbound and outbound traffic for resources like EC2. It allows or denies traffic based on rules such as IP, port, and protocol."
            }
        ]
    },
    # Page 5: Scaling & Infrastructure
    {
        "title": "5. Scaling & Infrastructure",
        "subtitle": "ELB, ASG, AZ",
        "sections": [
             {
                "header": "10. What is a Load Balancer?",
                "body": "A Load Balancer (AWS Elastic Load Balancing) distributes incoming traffic across multiple servers. It improves application availability, scalability, and fault tolerance by preventing server overload."
            },
             {
                "header": "11. What is Auto Scaling?",
                "body": "Auto Scaling automatically increases or decreases the number of EC2 instances based on traffic demand. It helps maintain performance while optimizing cost by running only the required resources."
            },
            {
                "header": "15. What is an Availability Zone (AZ)?",
                "body": "An Availability Zone is an isolated data center within an AWS region. Using multiple AZs helps achieve high availability and fault tolerance."
            }
        ]
    },
    # Page 6: Monitoring & Messaging
    {
        "title": "6. Monitoring & Messaging",
        "subtitle": "CloudWatch, SNS, SQS",
        "sections": [
             {
                "header": "12. What is CloudWatch?",
                "body": "CloudWatch (Amazon CloudWatch) is an AWS monitoring service used to track metrics, logs, and alarms for AWS resources. It helps monitor performance, detect issues, and trigger alerts."
            },
            {
                "header": "14. Difference between SQS and SNS",
                "items": [
                    "<b>Amazon SQS:</b> Message queue (point-to-point): messages are stored and processed by one consumer.",
                    "<b>Amazon SNS:</b> Message topic (publish-subscribe): messages are sent to multiple subscribers at once."
                ]
            }
        ]
    }
]
