import express, { Request, Response } from 'express';
import cookieParser from 'cookie-parser';
import authRoutes from './routes/auth';
import { authenticateToken } from './middleware/auth';
import { getFinalPrice } from './utils/discount';

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cookieParser());

// Auth routes
app.use('/api', authRoutes);

// Home page - requires authentication
app.get('/', authenticateToken, (req: Request, res: Response) => {
  const user = (req as any).user;

  // Bug: Assumes isVip is always defined, but it's optional in types
  const welcomeMessage = user.isVip
    ? `Welcome VIP user ${user.email}!`
    : `Welcome ${user.email}!`;

  res.json({
    message: welcomeMessage,
    user: {
      id: user.id,
      email: user.email,
      isVip: user.isVip
    }
  });
});

// Price endpoint using billing utility
app.get('/api/price', (req: Request, res: Response) => {
  const basePrice = parseFloat(req.query.price as string) || 100;
  const discount = parseFloat(req.query.discount as string) || 0;
  const isVip = req.query.vip === 'true';

  // This can produce negative prices if discount > 100
  const finalPrice = getFinalPrice(basePrice, discount, isVip);

  res.json({
    basePrice,
    discount,
    isVip,
    finalPrice
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

export default app;
