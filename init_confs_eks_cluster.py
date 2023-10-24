import os

class AWSConfigurator:
    def update_aws_cli(self):
        # Update the AWS CLI
        os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
        os.system('unzip awscliv2.zip')

    def install_aws_cli(self):
        # Install the AWS CLI update
        os.system('sudo ./aws/install --bin-dir /usr/bin --install-dir /usr/bin/aws-cli-update')

    def configure_aws_account(self):
        # Configure the AWS account
        os.system('aws configure')
        # Enter your AWS account credentials when prompted

class KubectlInstaller:
    def install_kubectl(self):
        # Install kubectl
        os.system('curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.2/2023-10-17/bin/linux/amd64/kubectl')

    def authorize_kubectl(self):
        # Grant execute permission to kubectl
        os.system('chmod +x ./kubectl')

    def copy_kubectl_binary(self):
        # Copy the kubectl binary to $HOME/bin
        os.system('mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH')

    def validate_kubectl_installation(self):
        # Validate the kubectl installation
        os.system('kubectl version --client')

class EksctlInstaller:
    def install_eksctl(self):
        # Install eksctl
        os.system('curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp')

    def move_eksctl_binary(self):
        # Move eksctl to /usr/bin
        os.system('sudo mv /tmp/eksctl /usr/bin')

    def validate_eksctl_installation(self):
        # Validate the eksctl installation
        os.system('eksctl version')

class GitRepositoryCloner:
    def clone_git_repository(self):
        # Check if GIT_REPO_URL environment variable is defined
        git_repo_url = os.getenv('GIT_REPO_URL')
        if git_repo_url is None:
            print("The GIT_REPO_URL environment variable is not defined. Set it to the Git repository URL.")
            return

        os.system('sudo yum install -y git')
        os.system(f'git clone {git_repo_url}')

if __name__ == "__main__":
    aws_configurator = AWSConfigurator()
    kubectl_installer = KubectlInstaller()
    eksctl_installer = EksctlInstaller()
    git_repo_cloner = GitRepositoryCloner()

    # AWS Configuration
    aws_configurator.update_aws_cli()
    aws_configurator.install_aws_cli()
    aws_configurator.configure_aws_account()

    # Install kubectl
    kubectl_installer.install_kubectl()
    kubectl_installer.authorize_kubectl()
    kubectl_installer.copy_kubectl_binary()
    kubectl_installer.validate_kubectl_installation()

    # Install eksctl
    eksctl_installer.install_eksctl()
    eksctl_installer.move_eksctl_binary()
    eksctl_installer.validate_eksctl_installation()

    # Clone the Git repository
    git_repo_cloner.clone_git_repository()
