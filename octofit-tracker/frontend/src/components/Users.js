import React, { useEffect, useState } from 'react';

const endpointName = 'users';
const baseUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`;
const endpoint = `${baseUrl}/${endpointName}/`;

export default function Users() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [modalContent, setModalContent] = useState(null);

  useEffect(() => {
    console.log('Fetching Users from', endpoint);
    fetch(endpoint)
      .then((r) => r.json())
      .then((json) => {
        console.log('Users response:', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error('Users fetch error:', err))
      .finally(() => setLoading(false));
  }, []);

  function openModal(item) {
    setModalContent(item);
    setShowModal(true);
  }

  function closeModal() {
    setShowModal(false);
    setModalContent(null);
  }

  return (
    <div className="card">
      <div className="card-header d-flex align-items-center justify-content-between">
        <h5 className="mb-0">Users</h5>
      </div>
      <div className="card-body">
        {loading && <p>Loading...</p>}
        {!loading && (
          <div className="table-responsive">
            <table className="table table-striped table-hover table-sm align-middle">
              <thead>
                <tr>
                  <th style={{width: '5%'}}>#</th>
                  <th style={{width: '20%'}}>ID / Name</th>
                  <th>Details</th>
                  <th style={{width: '18%'}}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    <td>{idx + 1}</td>
                    <td>{item.id || item.username || item.name || '-'}</td>
                    <td className="card-json">{JSON.stringify(item)}</td>
                    <td>
                      <button className="btn btn-sm btn-primary me-2" onClick={() => openModal(item)}>View</button>
                      <a className="btn btn-sm btn-link" href={`${endpoint}${item.id ? item.id + '/' : ''}`} target="_blank" rel="noreferrer">API</a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {showModal && (
          <div className="modal d-block" tabIndex="-1" role="dialog">
            <div className="modal-dialog modal-lg" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">User Details</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={closeModal}></button>
                </div>
                <div className="modal-body">
                  <pre className="card-json">{JSON.stringify(modalContent, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button className="btn btn-secondary" onClick={closeModal}>Close</button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
