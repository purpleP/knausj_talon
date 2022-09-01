<<<<<<< HEAD
tag: terminal
and tag: user.openshift
-
openshift [control]: "oc "

openshift create:         "oc create "
openshift expose:         "oc expose "
openshift run:            "oc run "
openshift set:            "oc set "
openshift run container:  "oc run-container "

openshift explain:        "oc explain "
openshift get:            "oc get "
openshift edit:           "oc edit "
openshift delete:         "oc delete "

openshift rollout:        "oc rollout "
openshift rolling update: "oc rolling-update "
openshift scale:          "oc scale "
openshift auto scale:     "oc autoscale "

openshift certificate:    "oc certificate "
openshift top:            "oc top "
openshift drain:          "oc drain "
openshift taint:          "oc taint "
openshift (cord | cordon): "oc cordon "
openshift (uncord | uncordon): "oc uncordon "
openshift cluster (info | information): "oc cluster-info "

openshift describe:     "oc describe "
openshift logs:         "oc logs "
openshift attach:       "oc attach "
openshift exec:         "oc exec "
openshift port forward: "oc port-forward "
openshift proxy:        "oc proxy "
openshift copy:         "oc cp "
openshift auth:         "oc auth "
openshift project:      "oc project "

openshift diff:         "oc diff "
openshift apply:        "oc apply "
openshift patch:        "oc patch "
openshift replace:      "oc replace "
openshift wait:         "oc wait "
openshift convert:      "oc convert "
openshift customize:    "oc kustomize "

openshift label:        "oc label "
openshift annotate:     "oc annotate "
openshift completion:   "oc completion "

openshift (interface | API):   "oc api "
openshift interface resources: "oc api-resources "
openshift interface versions:  "oc api-versions "
openshift config:       "oc config "
openshift help:         "oc help "
openshift plugin:       "oc plugin "
openshift version:      "oc version "

openshift {user.openshift_action} [{user.openshift_object}]:
    insert("oc {openshift_action} ")
    insert(openshift_object or "")

openshift detach:
    key("ctrl-p")
    key("ctrl-q")
openshift shell:
    insert("oc exec -it  -- /bin/bash")
    key("left:13")
||||||| parent of 57fae2b5 (openshift support)
=======
tag: terminal
and tag: user.openshift
-
openshift [control]: "oc "

openshift create:         "oc create "
openshift expose:         "oc expose "
openshift run:            "oc run "
openshift set:            "oc set "
openshift run container:  "oc run-container "

openshift explain:        "oc explain "
openshift get:            "oc get "
openshift edit:           "oc edit "
openshift delete:         "oc delete "

openshift rollout:        "oc rollout "
openshift rolling update: "oc rolling-update "
openshift scale:          "oc scale "
openshift auto scale:     "oc autoscale "

openshift certificate:    "oc certificate "
openshift top:            "oc top "
openshift drain:          "oc drain "
openshift taint:          "oc taint "
openshift (cord | cordon): "oc cordon "
openshift (uncord | uncordon): "oc uncordon "
openshift cluster (info | information): "oc cluster-info "

openshift describe:     "oc describe "
openshift logs:         "oc logs "
openshift attach:       "oc attach "
openshift exec:         "oc exec "
openshift port forward: "oc port-forward "
openshift proxy:        "oc proxy "
openshift copy:         "oc cp "
openshift auth:         "oc auth "

openshift diff:         "oc diff "
openshift apply:        "oc apply "
openshift patch:        "oc patch "
openshift replace:      "oc replace "
openshift wait:         "oc wait "
openshift convert:      "oc convert "
openshift customize:    "oc kustomize "

openshift label:        "oc label "
openshift annotate:     "oc annotate "
openshift completion:   "oc completion "

openshift (interface | API):   "oc api "
openshift interface resources: "oc api-resources "
openshift interface versions:  "oc api-versions "
openshift config:       "oc config "
openshift help:         "oc help "
openshift plugin:       "oc plugin "
openshift version:      "oc version "

openshift {user.openshift_action} [{user.openshift_object}]:
    insert("oc {openshift_action} ")
    insert(openshift_object or "")

openshift detach:
    key("ctrl-p")
    key("ctrl-q")
openshift shell:
    insert("oc exec -it  -- /bin/bash")
    key("left:13")
>>>>>>> 57fae2b5 (openshift support)
