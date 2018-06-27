import React from 'react';
import { Link } from 'react-router-dom';

const People = props => (
  <div id="people">
    <h3>{props.header}</h3>
    <ul id="people-list">
      {props.people.map(person =>
        <li key={person.id}>
          <Link key={person.id} to={`/person/${person.id}`}>
            {person.name}
          </Link>
        </li>)}
    </ul>
  </div>
);

export default People;
