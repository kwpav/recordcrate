import { MemoryRouter } from 'react-router-dom';
import React from 'react';
import ReactDOM from 'react-dom';
import AlbumDetail from './AlbumDetail';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<MemoryRouter>
                  <AlbumDetail
                    id="1"
                    albumName="The Last Waltz"
                    artists={[
                      {
                        name: 'The Band',
                        members: [
                          { id: 1, name: 'Rick Danko' },
                          { id: 2, name: 'Levon Helm' },
                          { id: 3, name: 'Garth Hudson' },
                          { id: 4, name: 'Richard Manual' },
                        ],
                        description: '',
                      },
                    ]}
                    releases={[
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
                    ]}
                    description="Hello"
                  />
                  </MemoryRouter>, div);
  ReactDOM.unmountComponentAtNode(div);
});
