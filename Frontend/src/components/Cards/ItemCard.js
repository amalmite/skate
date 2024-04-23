import React from "react";
import Card from "react-bootstrap/Card";
import "./ItemCard.css";

const ItemCard = ({ image, title, ft }) => {



  return (
    <>

    {/* Membsership cards */}
    
      <Card className="item-card b-zero shadow-sm">
        <Card.Img
          variant="top"
          height={180}
          src={image}
          className="b-zero object-fit-cover"
          alt="Membership"
        />
        <Card.Body>
          <Card.Text className="text-center">{title}</Card.Text>
          <hr />
        </Card.Body>
        <Card.Footer
          className="item-footer d-flex justify-content-center align-items-center b-zero "
        >
          {ft}
        </Card.Footer>
      </Card>
    </>
  );
};

export default ItemCard;
