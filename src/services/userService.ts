import { User } from '../types';

// In-memory database
const users: User[] = [];

// Bug: Stores plain-text password (security issue)
export function createUser(email: string, password: string, isVip: boolean = false): User {
  const user: User = {
    id: Date.now().toString(),
    email,
    password, // Storing plain-text password (intentional bug)
    isVip
  };

  users.push(user);
  return user;
}

export function findUserByEmail(email: string): User | undefined {
  return users.find(u => u.email === email);
}

// Bug: Plain-text password comparison with === (security issue)
export function validatePassword(user: User, password: string): boolean {
  return user.password === password; // Direct comparison (intentional bug)
}

export function getAllUsers(): User[] {
  return users;
}
