import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import People from './People';
import Tracklist from './Tracklist';
import AlbumTable from './AlbumTable';

const AlbumDetail = ({
  albumName,
  artists,
  releases,
  description,
}) => (
  <div className="container">
    <div>
      <h1 className="page-title">{albumName}</h1>
      <Link to={`/bands/${artists[0].id}`}><h2 id="page-subtitle">{artists[0].name}</h2></Link>
      <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
    </div>

    <div id="page-details">
      <h3>About</h3>
      <p>{description}</p>
    </div>

    <Tracklist tracks={releases[0].tracks} />
    <People
      header="People"
      people={releases[0].people}
    />

    <AlbumTable
      header="Other Versions"
      headers={['Title (Format)', 'Record Label', 'Country', 'Year']}
      albums={[{
        name: `${albumName} (${releases[0].format})`,
        recordLabel: releases[0].recordLabel,
        country: releases[0].releaseCountry,
        releaseDate: releases[0].releaseDate,
      }]}
    />
  </div>
);

AlbumDetail.propTypes = {
  albumName: PropTypes.string.isRequired,
  artists: PropTypes.arrayOf(PropTypes.object).isRequired,
  releases: PropTypes.arrayOf(PropTypes.object).isRequired,
  description: PropTypes.string.isRequired,
};

export default AlbumDetail;
