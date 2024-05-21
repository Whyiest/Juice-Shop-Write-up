# Juice-Shop Write-up: Exposed Metrics Challenge

## Challenge Overview

**Title:** Exposed Metrics\
**Category:** Sensitive Data Exposure\
**Difficulty:** ⭐ (1/6)

The challenge involves discovering an exposed metrics endpoint in a web application. 

## Tools Used

- Web browser
- Knowledge of Prometheus monitoring

## Methodology and Solution

To complete the Exposed Metrics challenge, follow these steps:

1. **Review Application Documentation**: We know that Juice Shop use Prometheus for his metrics. Examined the official documentation of Prometheus to understand its default configurations. It was found that Prometheus typically exposes metrics at the `/metrics` endpoint.

2. **Access the Endpoint**: Visited `http://127.0.0.1:3000/metrics` in the browser, anticipating to find the metrics endpoint as per the default configuration of Prometheus.

3. **Analyze Exposed Data**: Upon accessing the URL, metrics data was displayed. This included:
   - Startup times for various services.
   - CPU and memory usage statistics.
   - Detailed runtime and system health data.
   - Information about file uploads, including types and success/failure counts.

   <img src="../assets/difficulty1/exposed_metrics_1.png" alt="metrics" width="500px">

## Solution Explanation

By navigating to the Prometheus default metrics endpoint, valuable operational data was uncovered. This poses a significant security risk as sensitive system internals are exposed, potentially aiding malicious entities in crafting attacks.

## Remediation

### Immediate Actions
- **Restrict Access**: Implement access controls to limit the `/metrics` endpoint visibility only to authenticated users with administrative privileges.
  
### Long-term Strategies
- **Network Configuration**: Ensure that metrics endpoints are not accessible through the public internet. If needed, they should be accessible only via internal networks or through a VPN.
- **Enhance Authentication**: Utilize strong authentication methods to protect endpoints like these. Consider implementing additional security measures such as two-factor authentication for administrative access.
