import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import People from './People';
import Tracklist from './Tracklist';
import AlbumTable from './AlbumTable';

const AlbumDetail = props => (
  <div className="container">
    <div>
      <h1 className="page-title">{props.albumName}</h1>
      <Link to="/band/1"><h2 id="page-subtitle">{props.bandName}</h2></Link>
      <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
    </div>

    <div id="page-details">
      <h3>About</h3>
      <p>The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco. The Last Waltz was advertised as The Band's "farewell concert appearance",[2] and the concert saw The Band joined by more than a dozen special guests, including Eric Clapton, Ringo Starr, Bob Dylan, Ronnie Wood, Muddy Waters, Neil Young, Neil Diamond, Van Morrison, Bobby Charles, Dr. John, Paul Butterfield, Emmylou Harris, Ronnie Hawkins, Joni Mitchell, and The Staple Singers. The musical director for the concert was The Band's original record producer, John Simon.</p>
    </div>
    <Tracklist tracks={props.tracks} />
    <People
      header="People"
      people={props.people}
    />
    <AlbumTable
      header="Other Versions"
      headers={['Title (Format)', 'Record Label', 'Country', 'Year']}
      albums={[{
          name: 'The Last Waltz (3x LP)',
          recordLabel: 'Warner Bros.',
          country: 'US',
          releaseDate: '1978',
        }]}
    />

  </div>
);

AlbumDetail.propTypes = {
  albumName: PropTypes.string.isRequired,
  bandName: PropTypes.string.isRequired,
  tracks: PropTypes.arrayOf(PropTypes.object).isRequired,
  people: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default AlbumDetail;
