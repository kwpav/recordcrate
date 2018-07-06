import React from 'react';
import PropTypes from 'prop-types';

function CollectWantLinks({ status }) {
  if (status === 'collected' || status === 'wanted') {
    return (
      <div>
        <a href="#" className="collect-link card-link text-muted disabled">
          {status}
        </a>
      </div>
    );
  }
  return (
    <div>
      <a href="#" className="collect-link card-link">want</a>
      <a href="#" className="collect-link card-link">collect</a>
    </div>
  );
}
CollectWantLinks.propTypes = {
  status: PropTypes.string.isRequired,
};

export default CollectWantLinks;
