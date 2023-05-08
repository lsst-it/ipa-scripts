#!/bin/bash
users=$(cat /home/dtapia/dryrun/disabled_users.json | jq '.[].uid[]')
for users in "${users[@]}"
do
    echo "Running command for user: $user"
    ipa user-del --preserve --dry-run $users
    echo "User $user was deleted"
done

