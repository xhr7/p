import { Router, Request, Response } from 'express';
import { createUser, findUserByEmail, validatePassword } from '../services/userService';
import { generateToken, authenticateToken } from '../middleware/auth';
import { RegisterRequest, LoginRequest } from '../types';
import { blacklistToken } from '../services/tokenBlacklist';

const router = Router();

// Bug: No input validation for email and password (security issue)
// Bug: No rate limiting (security issue)
router.post('/register', (req: Request, res: Response) => {
  const { email, password, isVip } = req.body as RegisterRequest;

  // Bug: Missing validation - no checks for email format, password strength, etc.
  if (!email || !password) {
    res.status(400).json({ error: 'Email and password required' });
    return;
  }

  const existingUser = findUserByEmail(email);
  if (existingUser) {
    res.status(400).json({ error: 'User already exists' });
    return;
  }

  const user = createUser(email, password, isVip);
  const token = generateToken(user);

  res.cookie('token', token, {
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000
  });

  res.status(201).json({
    message: 'User registered successfully',
    user: { id: user.id, email: user.email, isVip: user.isVip }
  });
});

// Bug: No rate limiting (security issue) - vulnerable to brute force
// Bug: No input validation
router.post('/login', (req: Request, res: Response) => {
  const { email, password } = req.body as LoginRequest;

  if (!email || !password) {
    res.status(400).json({ error: 'Email and password required' });
    return;
  }

  const user = findUserByEmail(email);
  if (!user) {
    res.status(401).json({ error: 'Invalid credentials' });
    return;
  }

  // Uses plain-text password comparison
  if (!validatePassword(user, password)) {
    res.status(401).json({ error: 'Invalid credentials' });
    return;
  }

  const token = generateToken(user);

  res.cookie('token', token, {
    httpOnly: true,
    maxAge: 24 * 60 * 60 * 1000
  });

  res.json({
    message: 'Login successful',
    user: { id: user.id, email: user.email, isVip: user.isVip }
  });
});

// Logout endpoint - requires authentication
router.post('/logout', authenticateToken, (req: Request, res: Response) => {
  const token = req.cookies.token;

  if (!token) {
    res.status(400).json({ error: 'No token provided' });
    return;
  }

  // Add token to blacklist
  blacklistToken(token);

  // Clear the cookie
  res.clearCookie('token');

  res.json({ message: 'Logout successful' });
});

export default router;
