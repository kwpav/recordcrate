import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import People from './People';

const BandDetail = ({ name, members, description, discography }) => (
  <div className="container">
    <div>
      <h1 className="page-title">{name}</h1>
      <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
    </div>
    <div id="page-details">
      <h3>About</h3>
      <p>
        {description}
      </p>
    </div>
    <People
      header="Members"
      people={members}
    />
    <div id="discography">
      <h3>Discography</h3>
      <table className="table table-hover">
        <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Label</th>
            <th scope="col">Year</th>
          </tr>
        </thead>
        <tbody>
          {discography.map(album => (
            <tr key={album.id}>
              <th scope="row">
                <Link to={`/albums/${album.id}`}>{album.albumName}</Link>
              </th>
              <td>{album.label}</td>
              <td>{album.releaseDate}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);

BandDetail.propTypes = {
  name: PropTypes.string.isRequired,
  members: PropTypes.arrayOf(PropTypes.object).isRequired,
  description: PropTypes.string.isRequired,
  discography: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default BandDetail;
