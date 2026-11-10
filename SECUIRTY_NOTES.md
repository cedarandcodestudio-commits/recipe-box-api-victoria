2026-11-10

- Anonymous GET /recipes → 200 OK, returns all recipes including `"Secret family hot sauce"` with `"is_public": false`.
- Anonymous PATCH /recipes/1 → 200 OK, changes `title` to "Hacked Shakshuka"; no identity or permission checked.
- Anonymous DELETE /recipes/1 → 204 No Content; recipe is permanently removed.
- Follow-up anonymous GET /recipes/1 → 404 Not Found, {"error": "recipe not found"}; confirms delete succeeded for an unauthenticated caller.