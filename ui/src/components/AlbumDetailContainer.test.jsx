import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumDetailContainer from './AlbumDetailContainer';

describe('The AlbumDetailContainer component', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM
      .render(<MemoryRouter>
                <AlbumDetailContainer match={{ params: {} }} />
              </MemoryRouter>, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
