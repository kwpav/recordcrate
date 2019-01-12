import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const People = ({ header, people }) => (
  <div id="people">
    <h3>{header}</h3>
    <ul id="people-list">
      {people.map(person => (
        <li key={person.id}>
          <Link key={person.id} to={`/people/${person.id}`}>
            {person.name}
          </Link>
        </li>
      ))}
    </ul>
  </div>
);

People.propTypes = {
  header: PropTypes.string.isRequired,
  people: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default People;
