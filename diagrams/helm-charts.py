from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing as Ingress, SVC as Service
from diagrams.k8s.podconfig import Secret
from diagrams.k8s.storage import Vol as Volume
from diagrams.onprem.client import User
from diagrams.aws.security import SecretsManager
from diagram_generator.utils import get_output_filename

with Diagram("Helm Charts and Kubernetes Components", direction="LR", filename=get_output_filename(__file__), outformat=["jpg", "png", "dot", "pdf"], show=False):
    # User interacting with the system
    user = User("User")

    # Kubernetes Cluster
    with Cluster("Kubernetes Cluster"):
        # Ingress Helm Chart (Route for accessing the service)
        with Cluster("Ingress Helm Chart"):
            route = Ingress("OpenShift Route")

        # Java Helm Chart (App with volumes and service)
        with Cluster("Java Helm Chart"):
            pod = Pod("Application Pod")
            volume = Volume("ConfigMaps/Secrets/Volumes")
            service = Service("Service")
            pod << volume  # Volume connected to the Pod

        # External Secrets Helm Chart (Secrets from AWS to K8s Pod)
        with Cluster("External Secrets Helm Chart"):
            secret_store = Secret("Secret Store")
            ext_secret = Secret("ExternalSecret")
            k8s_secret = Secret("K8s Secret")
            secret_store >> ext_secret >> k8s_secret >> pod  # Secrets flow to the pod

    # External connection from AWS Secrets Manager
    secrets_manager = SecretsManager("AWS Secrets Manager")

    # Diagram relationships
    user >> route  # User accesses the route
    route >> service  # Route forwards to the service
    pod >> service  # Pod connects to the service
    secrets_manager >> secret_store  # Secrets manager feeds into the secret store
