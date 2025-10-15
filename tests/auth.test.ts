import { createUser, findUserByEmail, validatePassword } from '../src/services/userService';
import { generateToken } from '../src/middleware/auth';

describe('Authentication', () => {
  beforeEach(() => {
    // Clear users array before each test
    const users = require('../src/services/userService');
    users.getAllUsers().length = 0;
  });

  describe('User Service', () => {
    test('should create a new user', () => {
      const user = createUser('test@example.com', 'password123', false);
      expect(user.email).toBe('test@example.com');
      expect(user.password).toBe('password123'); // Plain-text stored
    });

    test('should find user by email', () => {
      createUser('test@example.com', 'password123', false);
      const user = findUserByEmail('test@example.com');
      expect(user).toBeDefined();
      expect(user?.email).toBe('test@example.com');
    });

    // Bug: This test will FAIL - uses correct password when testing rejection
    test('should reject wrong password', () => {
      const user = createUser('test@example.com', 'password123', false);
      // Bug: Using CORRECT password in a test that should test WRONG password
      const isValid = validatePassword(user, 'password123');
      expect(isValid).toBe(false); // Will fail because password matches
    });

    test('should validate correct password', () => {
      const user = createUser('test@example.com', 'password123', false);
      const isValid = validatePassword(user, 'password123');
      expect(isValid).toBe(true);
    });
  });

  describe('JWT Token', () => {
    test('should generate a valid token', () => {
      const user = createUser('test@example.com', 'password123', false);
      const token = generateToken(user);
      expect(token).toBeDefined();
      expect(typeof token).toBe('string');
    });
  });
});
