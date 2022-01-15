
# Storage and list objects in Cloud Provider
## list-s3-blobs
+ **terraform:**   Contains *.tf* files in order to create a s3 bucket. If you need a remote backend, uncomment and configure backend.tf
+ **list-s3-blobs:** Small program made in python to list objects from s3 bucket. Exposes /list endpoint in the port 5000. The bucket can be configured with *AWS_BUCKET* environment variable.
    + **docker:** Contains the source code and Dockerfile to build the container
    + **k8s:** Contains the yamls needed in order to deploy the program in a kubernetes cluster. If th program needs an *external* URL can be included an *Ingress* or *VirtualService* if Istio is deployed on k8s.

The authentication is done via AWS *AK*/*SK* and Kubernetes Secret. This secret can be stored in a repository safely with tools like [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets)

If Kubernetes Cluster is deployed in AWS there is also the possibility of using IRSA
*IAM Rolse for Service Account* [AWS Doc](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html). No credentials or secrets are needed with this approach and could be a cleaner way.

