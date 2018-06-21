import React from 'react';
import { Link } from 'react-router-dom';

function People(props) {
  return (
    <div id="members">
      <h3>{props.header}</h3>
      <p>
        {props.people.map(person =>
          <Link
            to={`/person/${person.id}`}
            key={person.id}
          >
            {person.name}
          </Link>)}
      </p>
    </div>
  );
}

export default People;
