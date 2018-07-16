import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumList from './AlbumList';

const mockData = {
  records:
    [
      {
        id: 1,
        albumName: 'The Last Waltz',
        artists: [
          {
            id: 1,
            name: 'The Band',
            members: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            description: '',
          },
        ],
        releases: [
          {
            recordLabel: 'MGM',
            tracks: [
              { id: 1, title: 'Theme from the Last Waltz', length: '3:28' },
              { id: 2, title: 'Up on Cripple Creek', length: '4:44' },
            ],
            people: [
              { id: 1, name: 'Rick Danko' },
              { id: 2, name: 'Levon Helm' },
              { id: 3, name: 'Garth Hudson' },
              { id: 4, name: 'Richard Manual' },
            ],
            format: '4xLP',
            releaseDate: '1/1/1970',
            releaseCountry: 'US',
            status: '',
          },
        ],
        description: 'The Last Waltz was a concert by the Canadian-American rock group The Band, held on American Thanksgiving Day, November 25, 1976, at Winterland Ballroom in San Francisco. The Last Waltz was advertised as The Band\'s "farewell concert appearance",[2] and the concert saw The Band joined by more than a dozen special guests, including Eric Clapton, Ringo Starr, Bob Dylan, Ronnie Wood, Muddy Waters, Neil Young, Neil Diamond, Van Morrison, Bobby Charles, Dr. John, Paul Butterfield, Emmylou Harris, Ronnie Hawkins, Joni Mitchell, and The Staple Singers. The musical director for the concert was The Band\'s original record producer, John Simon.',
      },
    ],
};

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumList pageTitle="" records={[mockData.records]} />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
