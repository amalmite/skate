import React, { useState } from "react";
import logo from "../../images/logo.png";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";


import { Container, Form, Button, Row, Col } from "react-bootstrap";
import axiosInstance from "../utils/axiosIntance";
import { useParams,useNavigate } from 'react-router-dom';

const Resetpassword = () => {
    const navigate =useNavigate()
    const { uidb64, token } = useParams();

  const [formData, setFormData] = useState({
    new_password: "",
    password2: "",
  });
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await axiosInstance.post(
          `/api/reset-password/${uidb64}/${token}/`,  
          formData
        );
        if (response.status === 200){
        toast.success("Password reset successfully", {
          onClose: () => {
            navigate("/login");
          },
        });
    }
      } catch (error) {
          console.log(error);
          if (error.response && error.response.status === 400 && error.response.data && error.response.data) {
            toast.error(error.response.data)
            Object.entries(error.response.data).forEach(([key, value]) =>
            toast.error(`${value}`)
          );
          } else if (error.response && error.response.status === 400 && error.response.data.error) {
            toast.error(error.response.data.error);
          } else {
            toast.error('An error occurred. Please try again later.');
          }
        }
      }


  return (
    <Container>
      <ToastContainer />
      <Row className="justify-content-center">
        <Col md={6} style={{ marginTop: "15%" }}>
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
              <h5 className="fw-normal my-4">Reset Password</h5>
            </div>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-4">
                <Form.Control
                  type="password"
                  name="new_password"
                  id="new_password"
                  placeholder="New password"
                  onChange={handleChange}
                  required
                />
              </Form.Group>
              <Form.Group className="mb-4">
                <Form.Control
                  type="password"
                  name="password2"
                  id="password2"
                  placeholder="Confirm Password"
                  onChange={handleChange}
                  required
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
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default Resetpassword;
