const fs = require('fs');

function countStudents(path) {
  let content;
  try {
	content = fs.readFileSync(path, 'utf8');
  } catch (err) {
	throw new Error('Cannot load the database');
  }

  const lines = content.split('\n').filter(ligne => ligne.trim() !== '');
  const students = lines.slice(1).map(ligne => {
	const [firstname,, , field] = ligne.split(',');
	return { firstname, field };
  });

  console.log(`Number of students: ${students.length}`);

  const byField = students.reduce((acc, stud) => {
	if (!acc[stud.field]) acc[stud.field] = [];
	acc[stud.field].push(stud.firstname);
	return acc;
  }, {});

  for (const [field, names] of Object.entries(byField)) {
	console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
