import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumTable from './AlbumTable';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumTable
                header="Involved"
                headers={['Title', 'Record Label', 'Country', 'Year']}
                albums={[{
                  name: 'The Last Waltz',
                  recordLabel: 'Warner Bros.',
                  country: 'US',
                  releaseDate: '1978',
                }]}
              />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
