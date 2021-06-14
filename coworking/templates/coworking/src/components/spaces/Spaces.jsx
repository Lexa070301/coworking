import Space from "./Space";

const Spaces = (props) => {
  let spaces = props.spaces.map((space, index) => <Space key={index} space={space}/>)
  return (
      <div>
        <div className={"container-fluid d-flex justify-content-between"}>
          {spaces}
        </div>
      </div>
  );
}

export default Spaces;