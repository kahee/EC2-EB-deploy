#!/user/bin/env bash

#2. eb-deploy시, .secrets를 실행하고 배포 한후, .secrets을 지워줌
git add -f .secrets && eb deploy --staged --profile=eb; git reset HEAD .secrets
