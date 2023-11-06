## Onboard a new application to the Openshift cluster

**Objectives:**

- Create a new deployment to run the image you created in Docker Hub a few weeks ago with the python application
- Create a new service to expose the deployment
- Use the command `oc port-forward` to access to the service from your local computer
- Create a route to expose the service to the world and test it by opening the URL from your browser

## Build an image from the Openshift cluster

**Objectives:**

- Create a new BuildConfig to build the container image from the cluster
    - Make use of the code in `source/python-app` from the repository https://github.com/musghost/belastingdienst
    - The output of the image should be an ImageStream
- Trigger the build using the oc command

## Automatically deploy the new created image

**Objectives:**

- Create a new DeploymentConfig that makes use of the ImageStream
- Scale up the DeploymentConfig with 3 replicas using the oc command
- Assign proper resources to the DeploymentConfig:
  - CPU 550m
  - Memory 512Mi
- Trigger a new BuildConfig and check if the automatically deploys the new version