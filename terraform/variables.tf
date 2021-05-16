variable "config_path" {
    type = string
    description = "Path to Kubeconfig"
    default = "~/.kube/config"
}

variable "namespace" {
    type = string
    description = "Namespace to install release"
    default = "default"
}

variable "tag" {
    type = string
    description = "Deployment Tag"
}