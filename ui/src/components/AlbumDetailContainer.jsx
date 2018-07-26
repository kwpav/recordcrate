import React from 'react';
import PropTypes from 'prop-types';
import RecordCrateAPI from '../RecordCrateAPI';
import AlbumDetail from './AlbumDetail';

// This is a wrapper around the AlbumDetail component.
// It is used to get the ':id' param from the router,
// which we can then pass th the API.
class AlbumDetailContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      albumName: '',
      artists: [{}],
      releases: [{
        tracks: [{
          id: 0,
        }],
        people: [{
          id: 0,
        }],
      }],
      description: '',
    };
  }

  componentDidMount() {
    this.setState(RecordCrateAPI.records.get(this.props.match.params.id));
  }

  render() {
    return (
      <AlbumDetail {...this.state} />
    );
  }
}

AlbumDetailContainer.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.object,
  }).isRequired,
};

export default AlbumDetailContainer;
