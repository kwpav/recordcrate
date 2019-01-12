import React from "react";
import PropTypes from "prop-types";
import AlbumCard from "./AlbumCard";

// TODO:
// right now this assumes that records prop is an array where each index has 3 records
// this is to form them into rows of 3 on the page
// if the data is not changed before here, this will need to be refactored
// or the data can be transformed before here
const AlbumList = ({ pageTitle, records }) => (
  <div className="container">
    <h1 className="page-title">{pageTitle}</h1>
    <div className="card-group record-collection">
      {records.map((group, i) => (
        <div key={i} className="record-shelf row">
          {group.map(record => (
            <div key={record.id} className="col-md-4">
              <AlbumCard {...record} />
            </div>
          ))}
        </div>
      ))}
    </div>
  </div>
);

AlbumList.defaultProps = {
  pageTitle: ""
};

AlbumList.propTypes = {
  pageTitle: PropTypes.string,
  records: PropTypes.arrayOf(PropTypes.array).isRequired
};

export default AlbumList;
