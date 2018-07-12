import React from 'react';
import PropTypes from 'prop-types';
import AlbumCard from './AlbumCard';

// TODO should the data be in groups of 3 for easier jsx?
const data = [
  [
    {
      id: 1,
      bandName: 'The Band',
      albumName: 'The Last Waltz',
      releaseDate: '1/1/1970',
      format: '4xLP',
      status: '',
    },
    {
      id: 2,
      bandName: 'The Band',
      albumName: 'Stage Freight',
      releaseDate: '1/1/1970',
      format: 'LP',
      status: '',
    },
    {
      id: 3,
      bandName: 'The Band',
      albumName: 'Music from Big Pink',
      releaseDate: '1/1/1970',
      format: 'LP',
      status: '',
    },
  ],
  [
    {
      id: 4,
      bandName: 'The Grateful Dead',
      albumName: 'American Beauty',
      releaseDate: '1/1/1980',
      format: 'LP',
      status: '',
    },
    {
      id: 5,
      bandName: 'The Grateful Dead',
      albumName: 'Workingmans Dead',
      releaseDate: '1/1/1980',
      format: 'LP',
      status: '',
    },
    {
      id: 6,
      bandName: 'The Grateful Dead',
      albumName: 'Barton Hall',
      releaseDate: '1/1/1980',
      format: 'LP',
      status: '',
    }],
];

const AlbumList = props => (
  <div className="container">
    <h1 className="page-title">{props.pageTitle}</h1>
    <div className="card-group record-collection">
      {data.map((group, i) => (
        <div key={i} className="record-shelf row">
          {group.map(release => (
            <div key={release.id} className="col-md-4">
              <AlbumCard {...release} />
            </div>
          ))}
        </div>
    ))}
    </div>
  </div>
);

AlbumList.propTypes = {
  pageTitle: PropTypes.string,
};

export default AlbumList;
