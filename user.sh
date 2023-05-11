#!/bin/bash
users=$(cat /home/dtapia/dryrun/disabled_users.json | jq -r '.[].uid[]')
for user in "${users[@]}"
do
echo "Running command for user: $user"
ipa user-del --preserve --dry-run $user
echo "User $user was deleted"
done
echo "All users have been deleted"