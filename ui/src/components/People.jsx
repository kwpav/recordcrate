import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const People = props => (
  <div id="people">
    <h3>{props.header}</h3>
    <ul id="people-list">
      {props.people.map(person => (
        <li key={person.id}>
          <Link key={person.id} to={`/person/${person.id}`}>
            {person.name}
          </Link>
        </li>))}
    </ul>
  </div>
);

People.propTypes = {
  header: PropTypes.string.isRequired,
  people: PropTypes.array.isRequired,
};

export default People;
