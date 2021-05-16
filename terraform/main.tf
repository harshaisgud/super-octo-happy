provider "helm" {
  kubernetes {
    config_path = var.config_path
  }
}


resource "helm_release" "camelcase" {
  name       = "camelcase"
  chart      = "./camelchart"
  namespace  = var.namespace
  values     = [file("./camelchart/values.yaml")]
  create_namespace = true

  set {
    name = "image.tag"
    value = var.tag
  }

  set {
    name = "versionz.image.tag"
    value = var.tag
  }
}