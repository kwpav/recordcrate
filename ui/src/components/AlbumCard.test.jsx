import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumCard from './AlbumCard';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumCard />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
