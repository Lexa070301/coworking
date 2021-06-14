import {NavLink} from "react-router-dom";

const Space = (props) => {
  return (
      <div className={"space-card-wrap"}>
        <NavLink to={`/spaces/${props.index}`} key={props.index}>
          <div className={"space-card"}>
            <div>
              <span className={"space-card__name"}>{props.space.name}</span>
            </div>
            <div>
              <p className={"space-card__description"}>{props.space.description}</p>
            </div>
            <div>
              <span className={"space-card__param"}>Адрес: </span>
              <span className={"space-card__param"}>{props.space.address}</span>
            </div>
            <div>
              <span className={"space-card__param"}>Вместимость: </span>
              <span className={"space-card__param"}>{props.space.capacity}</span>
            </div>
            <div>
              <span className={"space-card__param"}>Площадь: </span>
              <span className={"space-card__param"}>{props.space.area} (м<sup>2</sup>)</span>
            </div>
            <div>
              <span className={"space-card__param"}>Стоимость: </span>
              <span className={"space-card__param"}>{props.space.daily_cost} руб/день</span>
            </div>
          </div>
        </NavLink>
      </div>
  );
}

export default Space;