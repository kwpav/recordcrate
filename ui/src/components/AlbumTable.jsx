import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const AlbumTable = props => (
  <div>
    <h3>{props.header}</h3>
    <table className="table table-hover">
      <thead>
        <tr>
          {props.headers.map(header => (
            <th key={header} scope="col">{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {props.albums.map(album => (
          <tr key={album.name}>
            <th scope="row"><Link to="/album/1">{album.name}</Link></th>
            <td>{album.recordLabel}</td>
            <td>{album.country}</td>
            <td>{album.releaseDate}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

AlbumTable.propTypes = {
  header: PropTypes.string.isRequired,
  albums: PropTypes.array.isRequired,
};

export default AlbumTable;

