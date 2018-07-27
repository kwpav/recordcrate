import React from 'react';
import PropTypes from 'prop-types';
import RecordCrateAPI from '../RecordCrateAPI';
import PersonDetail from './PersonDetail';

// This is a wrapper around the PersonDetail component.
// It is used to get the ':id' param from the router,
// which we can then pass th the API.
class PersonDetailContainer extends React.Component {
  constructor() {
    super();
    this.state = {
      id: 1,
      name: '',
      description: '',
      involved: [{ id: 0 }],
    };
  }

  componentDidMount() {
    this.setState(RecordCrateAPI.people.get(this.props.match.params.id));
  }

  render() {
    return (
      <PersonDetail {...this.state} />
    );
  }
}

PersonDetailContainer.propTypes = {
  match: PropTypes.shape({
    params: PropTypes.object,
  }).isRequired,
};

export default PersonDetailContainer;
