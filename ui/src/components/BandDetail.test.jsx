import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import BandDetail from './BandDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <BandDetail
                name="The Band"
                members={
                  [
                    { id: 1, name: 'Rick Danko' },
                    { id: 2, name: 'Levon Helm' },
                    { id: 3, name: 'Garth Hudson' },
                    { id: 4, name: 'Richard Manual' },
                  ]
                }
                description=""
                discography={[
                  {
                    id: 1,
                    albumName: 'The Last Waltz',
                    label: 'MGM',
                    releaseDate: '1/1/1970',
                  }]
                }
              />
              </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
