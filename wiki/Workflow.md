# 🔭 Workflow

## Branches

- `main` is the default branch and always holds the latest pushed build.
- Feature work can happen on a side branch, but every push is also reflected
  on `main`.

## Before every push

1. **Check the script parses:**
   ```bash
   node -e "const h=require('fs').readFileSync('index.html','utf8');new Function(h.split('<script>')[1].split('</script>')[0])"
   ```
2. **Bump the badge:** `python3 tools/bump_space.py "what changed"`
3. **Update the wiki** if a feature or workflow changed.
4. Commit, push, and sync `main`.

## Running locally

Open `index.html` directly, or `python3 -m http.server 8000` and visit
<http://localhost:8000>.
