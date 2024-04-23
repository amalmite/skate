import React, { useContext, useState } from "react";
import "./ProductCard.css";
import { Image } from "react-bootstrap";
import { Product } from "../ProductDetails";
import AuthContext from "../Context/AuthContext";

const ProductCard = ({ image, name, id }) => {
  const { booking, setBooking } = useContext(AuthContext);
  const [added, setAdded] = useState(false);

  const handleSubmit = (e, id) => {
    e.preventDefault();

    const productData = Product.find((option) => option.id === id);

    const isAdded = booking.some((product) => product.productId === id);

    if (!isAdded) {
      setBooking((prevBooking) => [
        ...prevBooking,
        {
          productId: id,
          quantity: "1",
          data: productData,
        },
      ]);
      setAdded(true);
      console.log(booking);
    } else {
    }
  };

  return (


    <div className="product-card shadow b-zero">
      {/* Product cards */}
      <div
        className="d-flex justify-content-center align-content-center py-2"
        style={{ height: "10rem" }}
      >
        <Image src={image} alt="Product" className="object-fit-cover" />
      </div>
      <div className="product-content">
        <p className="text-1">stock 25+</p>
        <div className="text-2">
          <span>{name}</span>
        </div>
        <button
          className="product-action"
          type="button"
          onClick={(e) => handleSubmit(e, id)}
        >
          {added ? "Already added" : "Add to Cart"}
        </button>
      </div>
    </div>
  );
};

export default ProductCard;
