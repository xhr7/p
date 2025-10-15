// Billing utility with intentional bugs

// Bug: Can return negative prices if discountPercent > 100
export function calculateDiscount(price: number, discountPercent: number): number {
  const discount = price * (discountPercent / 100);
  return price - discount;
}

// Bug: Inconsistent rounding - uses Math.floor
export function calculateVipPrice(price: number): number {
  const vipDiscount = price * 0.15;
  return Math.floor(price - vipDiscount);
}

// Bug: Inconsistent rounding - uses Math.ceil instead of floor
export function calculateTax(price: number, taxRate: number = 0.08): number {
  return Math.ceil(price * taxRate);
}

// This function is okay but uses the buggy calculateDiscount
export function getFinalPrice(basePrice: number, discountPercent: number, isVip: boolean): number {
  let price = calculateDiscount(basePrice, discountPercent);

  if (isVip) {
    price = calculateVipPrice(price);
  }

  const tax = calculateTax(price);
  return price + tax;
}
