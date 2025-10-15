import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { User } from '../types';
import { findUserByEmail } from '../services/userService';
import { isTokenBlacklisted } from '../services/tokenBlacklist';

// Bug: Hardcoded JWT secret (security issue)
const JWT_SECRET = 'super-secret-key-12345';

export function generateToken(user: User): string {
  return jwt.sign(
    { id: user.id, email: user.email },
    JWT_SECRET,
    { expiresIn: '24h' }
  );
}

// Bug: Uses jwt.decode instead of jwt.verify (security issue)
// Bug: await used on synchronous function (type-safety issue)
export async function authenticateToken(
  req: Request,
  res: Response,
  next: NextFunction
): Promise<void> {
  try {
    const token = req.cookies.token;

    if (!token) {
      res.status(401).json({ error: 'Authentication required' });
      return;
    }

    // Check if token has been blacklisted (logged out)
    if (isTokenBlacklisted(token)) {
      res.status(401).json({ error: 'Token has been revoked' });
      return;
    }

    // Bug: jwt.decode doesn't verify signature! Should use jwt.verify
    // Bug: await on synchronous call
    const decoded = await jwt.decode(token) as { email: string } | null;

    if (!decoded || !decoded.email) {
      res.status(401).json({ error: 'Invalid token' });
      return;
    }

    const user = findUserByEmail(decoded.email);
    if (!user) {
      res.status(401).json({ error: 'User not found' });
      return;
    }

    (req as any).user = user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}
