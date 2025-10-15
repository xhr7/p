// User types - note isVip is optional but code assumes it's always defined
export interface User {
  id: string;
  email: string;
  password: string; // Will store plain-text (intentional security bug)
  isVip?: boolean; // Optional but code assumes it exists
}

export interface RegisterRequest {
  email: string;
  password: string;
  isVip?: boolean;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthenticatedRequest extends Express.Request {
  user?: User;
}
