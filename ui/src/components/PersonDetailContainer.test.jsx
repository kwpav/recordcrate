import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import PersonDetailContainer from './PersonDetailContainer';

describe('The PersonDetailContainer component', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM
      .render(<MemoryRouter>
                <PersonDetailContainer match={{ params: {} }} />
              </MemoryRouter>, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
