import React from 'react';
import { Link } from 'react-router-dom';

const AlbumTable = props => (
  <div id="other-versions">
    <h3>{props.header}</h3>
    <table className="table table-hover">
      <thead>
        <tr>
          <th scope="col">Title (Format)</th>
          <th scope="col">Label</th>
          <th scope="col">Country</th>
          <th scope="col">Year</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row"><Link to="/album/1">The Last Waltz (3xLP, Album)</Link></th>
          <td>Warner Bros. Records</td>
          <td>US</td>
          <td>1978</td>
        </tr>
        <tr>
          <th scope="row"><Link to="/album/1">The Last Waltz (3xLP, Album)</Link></th>
          <td>Warner Bros. Records</td>
          <td>Canada</td>
          <td>1978</td>
        </tr>
      </tbody>
    </table>
  </div>
);

export default AlbumTable;

