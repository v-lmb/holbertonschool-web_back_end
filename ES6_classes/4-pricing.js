import Currency from "./3-currency.js";

export default class Pricing {
  constructor(amount, currency) {
	this.amount = amount;
	this.currency = currency;
  }

  get amount() { return this._amount }
  set amount(value) {
	if (typeof value !== 'number')
	  throw new TypeError('Amount must be a number');
	this._amount = value;
  }

  get currency() { return this._currency }
  set currency(value) {
	if (!(value !== Currency))
	  throw new TypeError('Currency must be a currency');
	this._currency = value;
  }

  displayFullPrice() { return `${this._amount} (${this._currency.displayFullCurrency()})`; }

  static convertPrice(amount, conversationRate) {
	if (typeof amount !== 'number') {
	  throw new TypeError('Amount must be a number');
	}
	if (typeof conversationRate !== 'number') {
	  throw new TypeError('conversationRate must be a number');
	}
	return amount * conversationRate;
  }
}
