db.people.insert({
    sex: 'Male',
    first_name: 'Jakub',
    last_name: 'Szalek',
    job: 'Analyst',
    email: 's16422@pjwstk.edu.pl',
    location: {
      city: 'Warsaw',
      address: { streetname: 'Gwiazdzista', streetnumber: '7' }
    },
    description: "description",
    height: 185,
    weight: 65,
    birth_date: '1997-03-004T02:12:17Z',
    nationality: 'Poland',
    credit: [
      {
        type: 'visa',
        number: '8907456765326789',
        currency: 'PLN',
        balance: '0'
      }
    ]
  });