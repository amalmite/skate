import React, { useEffect, useState } from "react";
import { Row, Container, Col } from "react-bootstrap";
import HomeCarousel from "./HomeCarousel";
import BookingForm from "../BookingForm";
import Favorite from "./Favorite";
import SkateCard from "../Cards/SkateCard";
import MemberShip from "./MemberShip";
import Preloader from "../Preloader/Preloader";
import { Product } from "../ProductDetails";
import './Home.css'
const HomePage = () => {
  const skateProduct = Product.filter((product) => product.type === "skate");
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false);
    }, 700);
  }, []);

  return (
    <div style={{ backgroundColor: "#F2F2F2" }}>
      {isLoading ? (
        <Preloader />
      ) : (
        <div>
          {/* home carousel */}
          <HomeCarousel />
          <Container>
            <Row 
              xs={1}
              md={3}
              className="add"
              // style={{
              //   marginTop: "-8.7%",
              //   padding: "5%",
              //   display: "flex",
              //   justifyContent: "center",
              //   gap: "3%",
              // }}
            >
              {/* Booking form1 */}
              <Col style={{ width: "360px"}} className="md-4 mb-3">
              <div className="card b-zero effect2">
              <BookingForm />
              </div>
              </Col>


              {/* Skate cards 65 55 */}

              {skateProduct.map((product) => (
                <Col className="md-4 mb-3" style={{ width: "360px" }} key={product.id}>
                  <div className="card b-zero" >
                    <SkateCard
                      image={product.image}
                      skate={product.title}
                      price={product.price}
                      clr={product.color}
                      id={product.id}
                    />
                  </div>
                </Col>
              ))}
            </Row>

          {/* Favorite cards list */}

            <Favorite />
          </Container>
          {/* Membsership cards list */}
          <MemberShip />
        </div>
      )}
    </div>
  );
};

export default HomePage;
