import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import BandDetailContainer from './BandDetailContainer';

describe('The AlbumDetailContainer component', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM
      .render(<MemoryRouter>
                <BandDetailContainer match={{ params: {} }} />
              </MemoryRouter>, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
