import React, { Component } from 'react';
import { Link } from 'react-router-dom';

function AlbumDetail(props) {
  return (
    <div className="record-collection container">

      <div>
        <h1 id="page-title">The Last Waltz</h1>
        <Link to="/band/1"><h2 id="page-subtitle">The Band</h2></Link>
        <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
      </div>

      <div id="page-details">
        <p>The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco. The Last Waltz was advertised as The Band's "farewell concert appearance",[2] and the concert saw The Band joined by more than a dozen special guests, including Eric Clapton, Ringo Starr, Bob Dylan, Ronnie Wood, Muddy Waters, Neil Young, Neil Diamond, Van Morrison, Bobby Charles, Dr. John, Paul Butterfield, Emmylou Harris, Ronnie Hawkins, Joni Mitchell, and The Staple Singers. The musical director for the concert was The Band's original record producer, John Simon.</p>
      </div>

      <div id="tracklist">
        <h3>Tracklist</h3>
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Title</th>
              <th scope="col">Length</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1.</th>
              <td>Theme from the Last Waltz</td>
              <td>3:28</td>
            </tr>
            <tr>
              <th scope="row">2.</th>
              <td>Up On Cripple Creek</td>
              <td>4:44</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div id="people">
        <h3>People</h3>
        <a href="#">Rick Danko</a>, <a href="#">Levon Helm</a>, <a href="#">Garth Hudson</a>, <a href="#">Richard Manuel</a>
      </div>

      <div id="other-versions">
        <h3>Other Versions</h3>
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
              <td>Canda</td>
              <td>1978</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AlbumDetail;
