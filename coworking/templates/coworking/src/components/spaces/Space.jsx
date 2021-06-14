const Space = (props) => {
  return (
      <div className={"space-card-wrap"}>
        <div className={"space-card"}>
          <div>
            <span className={"space-card-name"}>{props.space.name}</span>
          </div>
          <div>
            <p className={"space-card-description"}>{props.space.description}</p>
          </div>
          <div>
            <span className={"space-card-param"}>Адрес: </span>
            <span className={"space-card-param"}>{props.space.address}</span>
          </div>
          <div>
            <span className={"space-card-param"}>Вместимость: </span>
            <span className={"space-card-param"}>{props.space.capacity}</span>
          </div>
          <div>
            <span className={"space-card-param"}>Площадь: </span>
            <span className={"space-card-param"}>{props.space.area} (м<sup>2</sup>)</span>
          </div>
          <div>
            <span className={"space-card-param"}>Стоимость: </span>
            <span className={"space-card-param"}>{props.space.daily_cost} руб/день</span>
          </div>
        </div>
      </div>
  );
}

export default Space;