import "./Header.scss";  
import {cover} from "../assets/"


const Header = () => {
  return (
    <div className="video-container">
      <video autoPlay loop muted playsInline>
        <source src={videoSrc} type="video/mp4" />
      </video>
    </div>
  );
};

export default Header;
