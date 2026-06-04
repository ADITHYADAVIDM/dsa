#!/bin/bash
cd "$(dirname "$0")"
CURRENT_DATE=$(date +%Y-%m-%d)

echo "🔄 Staging all new DSA solutions..."
git add .

echo "📝 Enter the problem name solved today (or press ENTER for default message):"
read -r PROBLEM_NAME

if [ -z "$PROBLEM_NAME" ]; then
    COMMIT_MSG="docs(dsa): daily roadmap sync ($CURRENT_DATE)"
else
    COMMIT_MSG="feat(dsa): solve $PROBLEM_NAME ($CURRENT_DATE)"
fi

echo "💾 Committing changes: \"$COMMIT_MSG\""
git commit -m "$COMMIT_MSG"

echo "🚀 Pushing updates to GitHub remote repository..."
git push -u origin master
echo "🎯 Daily DSA update successfully deployed!"
