import React from 'react';
import PropTypes from 'prop-types';
import AlbumTable from './AlbumTable';

function PersonDetail({ name, description, involved }) {
  return (
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
        albums={[{
            name: 'The Last Waltz',
            recordLabel: 'Warner Bros.',
            country: 'US',
            releaseDate: '1978',
          }]}
      />
    </div>
  );
}

PersonDetail.propTypes = {
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  involved: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default PersonDetail;
