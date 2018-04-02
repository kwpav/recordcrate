import React from 'react';

function People(props) {
  return (
    <div id="members">
      <h3>{props.header}</h3>
      <p>
        {props.people.map((person) => <a href="#">{person} </a>)}
      </p>
    </div>
  );
}

export default People;
