import React from 'react';
import PropTypes from 'prop-types';
import RecordCrateAPI from '../RecordCrateAPI';
import BandDetail from './BandDetail';

// This is a wrapper around the BandDetail component.
// It is used to get the ':id' param from the router,
// which we can then pass th the API.
class BandDetailContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      id: 0,
      name: '',
      members: [{ id: 0, name: '' }],
      description: '',
      discography: [{ id: 0, albumName: '', releaseDate: '' }],
    };
  }

  componentDidMount() {
    this.setState(RecordCrateAPI.artists.get(this.props.match.params.id));
  }

  render() {
    return (
      <BandDetail {...this.state} />
    );
  }
}

BandDetailContainer.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.object,
  }).isRequired,
};

export default BandDetailContainer;
