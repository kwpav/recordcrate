import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumCard from './AlbumCard';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <AlbumCard albumName="American Beauty" bandName="The Last Waltz" />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
