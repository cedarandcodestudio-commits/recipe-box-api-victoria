2026-11-10

- Anonymous GET /recipes → 200 OK, returns all recipes including `"Secret family hot sauce"` with `"is_public": false`.
- Anonymous PATCH /recipes/1 → 200 OK, changes `title` to "Hacked Shakshuka"; no identity or permission checked.