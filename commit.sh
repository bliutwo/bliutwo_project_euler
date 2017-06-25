#!/bin/bash

echo ''
echo 'Pulling...'
echo ''
git pull
echo ''
echo 'Adding all files to commit...'
echo ''
git add -A
echo ''
echo 'Starting commit, editor opening...'
echo ''
git commit
echo ''
echo 'Pushing...'
echo ''
git push
