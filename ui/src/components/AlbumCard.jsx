import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import CollectWantLinks from './CollectWantLinks';

const AlbumCard = props => (
  <div className="record-info card">
    <a href="#"><img className="card-img-top" src="http://placehold.it/225" alt="Card image cap" /></a>
    <div className="card-body">
      <Link to="/album/1"><h4 className="album-name card-title">{props.albumName}</h4></Link>
      <Link to="/band/1"><h6 className="artist-name card-subtitle mb-2 text-muted">{props.bandName}</h6></Link>
      <p className="card-text">
        Format: {props.format}
        <br />
        Released: {props.releaseDate}
        <br />
        The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco.
      </p>
      <CollectWantLinks status={props.status} />
    </div>
  </div>
);
AlbumCard.propTypes = {
  albumName: PropTypes.string.isRequired,
  bandName: PropTypes.string.isRequired,
  format: PropTypes.string.isRequired,
  releaseDate: PropTypes.string.isRequired,
  status: PropTypes.string.isRequired,
};

export default AlbumCard;
