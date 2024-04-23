import React from 'react';
import ExampleCarouselImage from '../Cards/ExampleCarouselImage';
import './HomeCarousel.css'
import { Carousel } from 'react-bootstrap';
import image1 from '../../images/carousal1.jpg';
import image3 from '../../images/carousal3.jpg';

const HomeCarousel = () => {
  return (
    <>
      <Carousel>
        <Carousel.Item interval={1000}>
          <ExampleCarouselImage src={image1}/>
          <div className="overlay"></div> {/* Add overlay */}
          <Carousel.Caption className="text-center">
            <h1 id="btitle" className="fw-bold  fs-sm-3 shadow-sm tm-banner-title text-uppercase">Enjoy <span class="tm-yellow-text">With Your</span> Family</h1>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <ExampleCarouselImage src={image3} />
          <div className="overlay"></div> {/* Add overlay */}
          <Carousel.Caption className="text-center ">
            <h1 id="ctitle" className="fw-bold  fs-sm-5 shadow-sm tm-banner-title text-uppercase">Happy Kids  <span class="tm-yellow-text">Make You </span> Happy</h1>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </>
  );
}

export default HomeCarousel;
