import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import CollectWantLinks from './CollectWantLinks';

const AlbumCard = ({
  id,
  albumName,
  artists,
  releases,
  description,
}) => (
  <div className="record-info card">
    <a href="#"><img className="card-img-top" src="http://placehold.it/225" alt="Card image cap" /></a>
    <div className="card-body">
      <Link to={`/albums/${id}`}><h4 className="album-name card-title">{albumName}</h4></Link>
      <Link to={`/bands/${artists[0].id}`}><h6 className="artist-name card-subtitle mb-2 text-muted">{artists[0].name}</h6></Link>
      <p className="card-text">
        Format: {releases[0].format}
        <br />
        Released: {releases[0].releaseDate}
        <br />
        {description.substring(0, 175)}...
      </p>
      <CollectWantLinks status={releases[0].status} />
    </div>
  </div>
);

AlbumCard.propTypes = {
  id: PropTypes.number.isRequired,
  albumName: PropTypes.string.isRequired,
  artists: PropTypes.arrayOf(PropTypes.object).isRequired,
  releases: PropTypes.arrayOf(PropTypes.object).isRequired,
  description: PropTypes.string.isRequired,
};

export default AlbumCard;
