import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import SignIn from './SignIn';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM
    .render(<MemoryRouter>
              <SignIn />
            </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
