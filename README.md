# Buggy Express App - Code Review Testing

This is a minimal TypeScript + Express application **intentionally containing seeded bugs** for testing code review tools and processes.

## ⚠️ WARNING

This repository contains intentional security vulnerabilities, logic bugs, and code quality issues. **DO NOT** use this code in production or as a template for real applications.

## Features
بببب
- User registration and login (`/api/register`, `/api/login`)
- JWT-based authentication with cookies
- Protected home page at `/` (requires valid JWT)
- Price calculation API with discount logic (`/api/price`)
- In-memory user storage (no external database required)

## Getting Started

### Prerequisites

- Node.js >= 18
- npm

### Installation

```bash
npm install
```

### Available Scripts

#### Development

```bash
npm run dev
```

Starts the development server with hot reload on `http://localhost:3000`

#### Build

```bash
npm run build
```

Compiles TypeScript to JavaScript in the `dist/` directory

#### Test

```bash
npm test
```

Runs Jest test suite. **Note:** 3 tests are intentionally failing to demonstrate test-related bugs (8 pass, 3 fail).

## API Endpoints

### POST /api/register

Register a new user.

```json
{
  "email": "user@example.com",
  "password": "password123",
  "isVip": false
}
```

### POST /api/login

Login with existing credentials.

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

### GET /

Protected home page. Requires valid JWT cookie from login.

### GET /api/price

Calculate price with discounts.

Query parameters:
- `price` - Base price (default: 100)
- `discount` - Discount percentage (default: 0)
- `vip` - Whether to apply VIP discount (true/false)

Example: `http://localhost:3000/api/price?price=100&discount=10&vip=true`

## Known Intentional Bugs

This codebase contains **intentionally seeded bugs** for testing code review tools. DO NOT fix these unless you're testing the fix process.

### 🔴 Security Issues (Critical)

| Issue | Location | Description |
|-------|----------|-------------|
| Hardcoded secret | `src/middleware/auth.ts:8` | JWT secret is hardcoded as `'super-secret-key-12345'` |
| No signature verification | `src/middleware/auth.ts:31` | Uses `jwt.decode()` instead of `jwt.verify()` - doesn't validate token signature |
| Plain-text passwords | `src/services/userService.ts:11` | Passwords stored without hashing |
| Plain-text comparison | `src/services/userService.ts:24` | Password comparison using `===` instead of secure comparison |
| No input validation | `src/routes/auth.ts:11-46` | Missing email format and password strength validation |
| No rate limiting | `src/routes/auth.ts:46` | Login endpoint vulnerable to brute force attacks |

### 🟠 Business Logic Bugs (High)

| Issue | Location | Description |
|-------|----------|-------------|
| Negative prices | `src/utils/discount.ts:4-7` | `calculateDiscount()` returns negative prices when discount > 100% |
| Inconsistent rounding | `src/utils/discount.ts:11,17` | Uses `Math.floor()` in one function, `Math.ceil()` in another |

### 🟡 Code Quality Issues (Medium)

| Issue | Location | Description |
|-------|----------|-------------|
| Optional type misuse | `src/types.ts:6`, `src/index.ts:25` | `isVip?` is optional but code assumes it's always defined |
| Incorrect async/await | `src/middleware/auth.ts:31` | `await` used on synchronous `jwt.decode()` call |

### 🔵 Test Issues

| Issue | Location | Description |
|-------|----------|-------------|
| Negative price test | `tests/discount.test.ts:16` | Expects non-negative but gets -50 (correctly catches the bug) |
| Wrong expectation | `tests/discount.test.ts:38` | Expects 100 but gets 92 (bad test expectation) |
| Wrong password test | `tests/auth.test.ts:30` | Uses correct password in "should reject wrong password" test |

All bugs are documented in code comments.

## Project Structure

```
├── src/
│   ├── index.ts              # Express app setup
│   ├── types.ts              # TypeScript type definitions
│   ├── middleware/
│   │   └── auth.ts           # JWT authentication middleware
│   ├── routes/
│   │   └── auth.ts           # Registration and login routes
│   ├── services/
│   │   └── userService.ts    # User management (in-memory)
│   └── utils/
│       └── discount.ts       # Billing and discount calculations
├── tests/
│   ├── auth.test.ts          # Authentication tests
│   └── discount.test.ts      # Discount calculation tests
├── package.json
├── tsconfig.json
└── jest.config.js
```

## License

MIT (for testing purposes only)