import Space from "./Space";

const Spaces = (props) => {
  let spaces = props.spaces.map((space, index) => <Space key={index} space={space} index={index}/>)
  return (
      <>
        <div className={"container-fluid"}>
          <h1 className={"text-start"}>Доступные пространства</h1>
        </div>
        <div className={"spaces-block"}>
          <div className={"container-fluid d-flex justify-content-start"}>
            {spaces}
          </div>
        </div>
      </>
  );
}

export default Spaces;