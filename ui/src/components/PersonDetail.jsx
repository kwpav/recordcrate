import React from 'react';
import PropTypes from 'prop-types';
import AlbumTable from './AlbumTable';

const PersonDetail = ({
  name,
  description,
  involved,
}) => (
  <div className="container">
    <div>
      <h1 className="page-title">{name}</h1>
      <img src="http://placehold.it/225" alt={name} />
    </div>

    <div id="page-details">
      <p>{description}</p>
    </div>

    <AlbumTable
      header="Involved"
      headers={['Title', 'Record Label', 'Country', 'Year']}
      albums={involved}
    />
  </div>
);

PersonDetail.propTypes = {
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  involved: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default PersonDetail;
