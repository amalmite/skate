import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import axiosInstance from '../utils/axiosIntance';
import axios from 'axios';


const UserProfile = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Retrieve session ID from local storage
    const sessionID = localStorage.getItem('session_id');

    // Make authenticated API request
    const fetchData = async () => {
      try {
        const response = await axios.get('your-backend-url/api/data', {
          headers: {
            Authorization: `Bearer ${sessionID}` // Include session ID in authorization header
          }
        });
        console.log(response.data);
        setData(response.data);
      } catch (error) {
        // Handle error (e.g., session expired)
        console.error('API request failed:', error);
      }
    };

    if (sessionID) {
      fetchData(); // Fetch data only if session ID exists
    }

  }, []); // Execute once on component mount

  return (
    <section style={{ backgroundColor: '#f4f5f7' }}>
      {/* <Container className="py-5">
        <Row className="justify-content-center align-items-center">
          <Col lg="6" className="mb-4 mb-lg-0">
            <Card className="mb-3" style={{ borderRadius: '.5rem' }}>
              {userData && (
                <Row className="g-0">
                  <Col md="4" className="gradient-custom text-center" style={{ borderTopLeftRadius: '.5rem', borderBottomLeftRadius: '.5rem' }}>
                    <h5>{userData.name}</h5>
                    <p>{userData.role}</p>
                    <i className="far fa-edit mb-5"></i>
                  </Col>
                  <Col md="8">
                    <Card.Body className="p-4">
                      <h6>Information</h6>
                      <hr className="mt-0 mb-4" />
                      <Row className="pt-1">
                        <Col size="6" className="mb-3">
                          <h6>Email</h6>
                          <p className="text-muted">{userData.email}</p>
                        </Col>
                        <Col size="6" className="mb-3">
                          <h6>Phone</h6>
                          <p className="text-muted">{userData.phone_number}</p>
                        </Col>
                        <Col size="6" className="mb-3">
                          <h6>Username</h6>
                          <p className="text-muted">{userData.phone_number}</p>
                        </Col>
                      </Row>
                   

                    </Card.Body>
                  </Col>
                </Row>
              )}
            </Card>
          </Col>
        </Row>
      </Container> */}
    </section>
  );
};

export default UserProfile;
