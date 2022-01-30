import React from 'react'

export default function Practice() {
  var people = [
    {
      name: "Mike Smith",
      family: {
        mother: "Jane Smith",
        father: {
          father1:"Harry Smith",
          father2:"Mike의 아빠",
        },
        sister: "Samantha Smith"
      },
      age: 35
    },
    {
      name: "Tom Jones",
      family: {
        mother: "Norah Jones",
        father: {
          father1:"Richard Jones",
          father2:"Tom jones아빠"
        },
        brother: "Howard Jones"
      },
      age: 25
    }
  ];
  
  for (var {name: n, family: { father: {father2 : f} } } of people) {
    // console.log("Name: " + n + ", Father: " + f);
  }
  return (
    <div>
      객체구조분해할당연습(console주석 해제)
    </div>
  )
}
