import React, { useState } from 'react';
import logo from "../../images/logo.png";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import { useNavigate } from "react-router-dom";

import { Container, Form, Button,Row,Col } from 'react-bootstrap';
import axiosInstance from '../utils/axiosIntance';

const Forgotpassword = () => {
    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        email: "",
          });
          const handleChange = (e) => {
            const { name, value } = e.target;
            setFormData(prevState => ({
                ...prevState,
                [name]: value
            }));
        };
    
        const handleSubmit = async (e) => {
            e.preventDefault();
            try {
              const response = await axiosInstance.post(
                "api/forgot-password/",
                formData,
                
              );
              console.log(response);
              if (response.status === 200) {

                toast.success(response.data.detail, {
                    onClose: () => {
                      navigate("/login");
                    },
                  });
              } else {
                toast.error("Failed to Forgotpassword");
              }
            } catch (error) {
                console.log(error);
                if (error.response && error.response.status === 400 && error.response.data && error.response.data.email && error.response.data.email[0]) {
                  toast.error(error.response.data.email[0]);
                } else if (error.response && error.response.status === 404 && error.response.data.error) {
                  toast.error(error.response.data.error);
                } else {
                  toast.error('An error occurred. Please try again later.');
                }
              }
            }
              
    
  return (
    <Container >
        <ToastContainer/>
        <Row className="justify-content-center">
        <Col md={6} style={{marginTop:'15%'}}>
          <div className="d-flex flex-column justify-content-center">
          <div className="d-flex flex-row justify-content-center align-items-center mt-2">
              <img
                alt=""
                src={logo}
                width="100"
                height="70"
                className="d-inline-block align-top"
              />
            </div>

            <div className="d-flex justify-content-center align-items-center">
              <h5 className="fw-normal my-4">Forgot Password</h5>
            </div>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-4">
                <Form.Control
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Email address"
                  onChange={handleChange}
                  />
              </Form.Group>
              <Button
                className="mb-4 w-100"
                style={{ backgroundColor: "#0367A6" }}
                type="submit"
              >
                Submit
              </Button>
            </Form>
    
              <a href="/login" style={{ color: "#393f81" }}>
                login
              </a>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default Forgotpassword;
