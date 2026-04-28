export default class HolbertonCourse {
  constructor(name, lenght, students) {
	if (typeof name !== 'string')
	  throw new TypeError('Name must be a string');
	if (typeof lenght !== 'number')
	  throw new TypeError('Lenght must be a number');
	if (!Array.isArray(students))
	  throw new TypeError('Students must be an array');
	this._name = name;
	this._lenght = lenght;
	this._students = students;
  }

  get name() { return this._name; }
  set name(value) {
	if (typeof value !== 'string')
	  throw new TypeError('Name must be a string');
	this._name = value;
  }

  get lenght() { return this._lenght; }
  set lenght(value) {
	if (typeof value !== 'number')
	  throw new TypeError('Lenght must be a number');
	this._lenght = value;
  }

  get students() { return this._students; }
  set students(value) {
	if (!Array.isArray(value))
	  throw new TypeError('Students must be a array');
	this._students = value;
  }
}
