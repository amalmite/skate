import React, { useContext, useState } from "react";
import "./BookingForm.css";
import AuthContext from "./Context/AuthContext";
import { Form } from "react-bootstrap";
import { Card } from "react-bootstrap";
import { Product } from "./ProductDetails";


const BookingForm = () => {
  const { setBooking } = useContext(AuthContext);
  const [formData, setFormData] = useState({
    selectDate: "",
    membership: "",
    selectSession: "",
    numAdmits: "",
  });

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    setBooking((prevBooking) => [
      ...prevBooking,
      {
        quantity: formData.numAdmits,
        date: formData.selectDate,
        time: formData.selectSession,
      },
    ]);
    setFormData({
      selectDate: "",
      membership: "",
      selectSession: "",
      numAdmits: "",
    });
  };

    return (
    <>
      <div>
        <Card style={{ borderRadius: "0px", border: "0px" }}>
          <Card.Header className="form-header" style={{ height: "3rem" }}>
            BOOK NOW
          </Card.Header>
          < Form className="p-4" onSubmit={handleSubmit}>
            <input
              type="date"
              className="mt-2 mb-3 p-2"
              value={formData.selectDate}
              id="selectDate"
              onChange={handleInputChange}
              required
            />

            <select
                  id="membership"
                  className="mt-2 mb-3 p-2"
                  value={formData.membership}
                  onChange={handleInputChange}
                >
                  <option>Select Membership</option>
                  {Product.filter((product) => product.type !== "product").map(
                    (option) => (
                      <option key={option.id} value={option.id}>
                        {option.title}-AED{option.price}
                      </option>
                    )
                  )}
                </select>
            <select
              className="mt-3 mb-3 p-2"
              value={formData.selectedSession}
              onChange={handleInputChange}
            >
              <option>Select Session</option>
              <option value="1">11:00 - 12:00</option>
              <option value="2">12:10 - 01:10</option>
              <option value="3">01:20 - 02:20</option>
              <option value="4">02:30 - 03:30</option>
              <option value="5">03:40 - 04:20</option>
              <option value="6">01:20 - 02:20</option>
            </select>

            <input
              className="mt-3 mb-3 p-2"
              type="number"
              id="numAdmits"
              placeholder="Number of Admissions"
              value={formData.numAdmits}
              onChange={handleInputChange}
            />
          </Form>

          <Card.Footer className="form-header form-button" style={{ height: "4rem" }}>
            BOOK NOW 
          </Card.Footer>
        </Card>
      </div>
    </>
  );
};

export default BookingForm;
