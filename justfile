
compose:
  docker compose pull
  docker compose up -d --build

    
compose-podman :
  podman compose pull
  podman compose up -d --build

publish:
  rm -rf dist
  uv build
  uvx twine upload dist/*
  rm -rf dist

restart-func cri="docker":
    {{cri}} compose restart hello-fn

step-1 id="1":
  #echo "{}" | http POST :10000/api/class/example.hello/*/invokes/new
  echo '{}' | jq --argjson id {{id}} '{"id":$id}' | oprc-cli i -g http://localhost:10002 example.hello 0 new -p -

step-1-verify id="1":
  oprc-cli o g example.hello 0 {{id}} -z tcp/127.0.0.1:7447

step-2 id="1":
  echo "{}" | oprc-cli i -g http://localhost:10002 example.hello 0 greet -o {{id}} -p -

bench-echo:
  echo "{}" | bench-g-invoke -g http://localhost:10002 example.hello echo 1 -c 16 -d 10s -p -

bench-random:
  echo "{}" | bench-g-invoke -g http://localhost:10002 example.record random 1 -c 16 -d 10s --stateful -p -
  
k3d-create:
  K3D_FIX_DNS=1 k3d cluster create -p "10080:80@loadbalancer"  --servers-memory 8G

maturin-dev options="":
  cd oprc-py; maturin develop {{options}}

oprc-dev options="":
  @just maturin-dev {{options}}
  @just oprc-py/gen-stub