import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumTable from './AlbumTable';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumTable header="Involved" />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
