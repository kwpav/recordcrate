import React from 'react';
import AlbumCard from './AlbumCard';

// TODO should the data be in groups of 3 for easier jsx?
const data = [
  [
    {
      band: 'The Band',
      album: 'The Last Waltz',
      date: '1/1/1970',
    },
    {
      band: 'The Band',
      album: 'Stage Freight',
      date: '1/1/1970',
    },
    {
      band: 'The Band',
      album: 'Music from Big Pink',
      date: '1/1/1970',
    },
  ],
  [
    {
      band: 'The Grateful Dead',
      album: 'American Beauty',
      date: '1/1/1980',
    },
    {
      band: 'The Grateful Dead',
      album: 'Workingmans Dead',
      date: '1/1/1980',

    },
    {
      band: 'The Grateful Dead',
      album: 'Barton Hall',
      date: '1/1/1980',
    }],
];

const AlbumList = props => (
  <div className="container">
    <h1 className="page-title">{props.pageTitle}</h1>
    <div className="card-group record-collection">
      {data.map(group => (
        <div className="record-shelf row">
          {group.map(release => (
            <div className="col-md-4">
              <AlbumCard albumName={release.album} bandName={release.band} />
            </div>
          ))}
        </div>
    ))}
    </div>
  </div>
);

export default AlbumList;
