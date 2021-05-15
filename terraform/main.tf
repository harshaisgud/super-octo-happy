provider "helm" {
  kubernetes {
    config_path = var.config_path
  }
}


resource "helm_release" "nginx_ingress" {
  name       = "camelcase"
  chart      = "./camelchart"
  namespace  = var.namespace
  values     = ["${file("./camelchart/values.yaml")}"]
}