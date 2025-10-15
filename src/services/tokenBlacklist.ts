// Simple in-memory token blacklist for logout functionality
const blacklistedTokens: Set<string> = new Set();

export function blacklistToken(token: string): void {
  blacklistedTokens.add(token);
}

export function isTokenBlacklisted(token: string): boolean {
  return blacklistedTokens.has(token);
}

// Optional: Clear expired tokens periodically to prevent memory leak
// In production, you'd use Redis or a database with TTL
export function clearBlacklist(): void {
  blacklistedTokens.clear();
}

export function getBlacklistSize(): number {
  return blacklistedTokens.size;
}
