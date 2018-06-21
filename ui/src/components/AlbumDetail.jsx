import React from 'react';
import { Link } from 'react-router-dom';
import People from './People';
import Tracklist from './Tracklist';
import AlbumTable from './AlbumTable';

function AlbumDetail(props) {
  return (
    <div className="record-collection container">
      <div>
        <h1 className="page-title">The Last Waltz</h1>
        <Link to="/band/1"><h2 id="page-subtitle">The Band</h2></Link>
        <img src="https://img.discogs.com/bHGI7q-dbvdhlIbEmVhguF_KIFw=/fit-in/455x455/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1564673-1443567983-5247.jpeg.jpg" />
      </div>

      <div id="page-details">
        <p>The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco. The Last Waltz was advertised as The Band's "farewell concert appearance",[2] and the concert saw The Band joined by more than a dozen special guests, including Eric Clapton, Ringo Starr, Bob Dylan, Ronnie Wood, Muddy Waters, Neil Young, Neil Diamond, Van Morrison, Bobby Charles, Dr. John, Paul Butterfield, Emmylou Harris, Ronnie Hawkins, Joni Mitchell, and The Staple Singers. The musical director for the concert was The Band's original record producer, John Simon.</p>
      </div>
      <Tracklist />
      <People
        header="People"
        people={
          [
            { id: 1, name: 'Rick Danko' },
            { id: 2, name: 'Levon Helm' },
            { id: 3, name: 'Garth Hudson' },
            { id: 4, name: 'Richard Manual' },
          ]
        }
      />
      <AlbumTable header="Other Versions" />
    </div>
  );
}

export default AlbumDetail;
