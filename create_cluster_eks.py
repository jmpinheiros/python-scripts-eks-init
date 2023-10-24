import os

class EKSClusterManager:
    def create_cluster(self):
        cluster_name = os.getenv('CLUSTER_NAME')
        region = os.getenv('AWS_REGION')
        nodegroup_name = os.getenv('NODEGROUP_NAME')
        node_type = os.getenv('NODE_TYPE')
        nodes = os.getenv('NODES')
        nodes_min = os.getenv('NODES_MIN')
        nodes_max = os.getenv('NODES_MAX')

        # Create EKS cluster
        os.system(f'eksctl create cluster --name {cluster_name} --region {region} --nodegroup-name {nodegroup_name} --node-type {node_type} --nodes {nodes} --nodes-min {nodes_min} --nodes-max {nodes_max} --managed')

class KubeconfigUpdater:
    def update_kubeconfig(self):
        cluster_name = os.getenv('CLUSTER_NAME')
        region = os.getenv('AWS_REGION')

        # Update kubeconfig to connect to the cluster
        os.system(f'aws eks update-kubeconfig --name {cluster_name} --region {region}')

class ServiceLoader:
    def load_balancer_service(self):
        # Apply the LoadBalancer service configuration
        os.system('kubectl apply -f ./nginx-svc.yaml')

class DeploymentStarter:
    def start_deployment(self):
        # Apply the deployment configuration
        os.system('kubectl apply -f ./nginx-deployment.yaml')

if __name__ == "__main__":
    eks_cluster_manager = EKSClusterManager()
    kubeconfig_updater = KubeconfigUpdater()
    service_loader = ServiceLoader()
    deployment_starter = DeploymentStarter()

    # Create EKS cluster
    eks_cluster_manager.create_cluster()

    # Update kubeconfig to connect to the cluster
    kubeconfig_updater.update_kubeconfig()

    # Start LoadBalancer service
    service_loader.load_balancer_service()

    # Start deployment
    deployment_starter.start_deployment()
