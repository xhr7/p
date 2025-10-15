import { calculateDiscount, calculateVipPrice, getFinalPrice } from '../src/utils/discount';

describe('Discount Utilities', () => {
  describe('calculateDiscount', () => {
    test('should calculate 10% discount correctly', () => {
      expect(calculateDiscount(100, 10)).toBe(90);
    });

    test('should calculate 50% discount correctly', () => {
      expect(calculateDiscount(200, 50)).toBe(100);
    });

    // Bug: This test will FAIL because discount > 100 returns negative price
    test('should never return negative prices', () => {
      const result = calculateDiscount(100, 150);
      expect(result).toBeGreaterThanOrEqual(0); // Will fail: gets -50
    });
  });

  describe('calculateVipPrice', () => {
    test('should apply 15% VIP discount', () => {
      const result = calculateVipPrice(100);
      expect(result).toBe(85); // Math.floor(100 - 15) = 85
    });
  });

  describe('getFinalPrice', () => {
    test('should calculate final price with tax for non-VIP', () => {
      const result = getFinalPrice(100, 10, false);
      // 100 - 10% = 90, + 8% tax = 90 + Math.ceil(7.2) = 90 + 8 = 98
      expect(result).toBe(98);
    });

    // Bug: This test will FAIL - uses wrong password expectation
    test('should calculate final price with VIP discount', () => {
      const result = getFinalPrice(100, 0, true);
      // 100, VIP: Math.floor(100 - 15) = 85, + tax: 85 + Math.ceil(6.8) = 85 + 7 = 92
      expect(result).toBe(100); // Wrong expectation - will fail
    });
  });
});