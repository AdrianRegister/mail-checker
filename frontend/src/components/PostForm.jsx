import Button from "./Button";

const PostForm = ({ defaultValue }) => {
  return (
    <form
      className="bg-emerald-100 rounded-lg p-4 shadow-lg"
      action="ENTER URL HERE"
    >
      <div className="flex flex-row pb-10">
        <div className="flex flex-row pt-2 pb-2 items-center">
          <label className="pr-1" htmlFor="level">
            Level:{" "}
          </label>
          <select name="level" id="level">
            <option value="all">All</option>
            <option value="a2-cycle">A2 Cycle</option>
            <option value="b1-cycle">B1 Cycle</option>
            <option value="b2-cycle">B2 Cycle</option>
            <option value="c1-cycle">C1 Cycle</option>
            <option value="c2-cycle">C2 Cycle</option>
            <option value="t3">T3</option>
            <option value="tpet">TPET</option>
          </select>
        </div>
        <div className="flex flex-row pt-2 pb-2 items-center">
          <label className="pr-1 pl-2" htmlFor="teacher">
            Teacher:{" "}
          </label>
          <input
            type="text"
            value={defaultValue}
            placeholder="Type teacher name"
            name="teacher"
          />
        </div>
      </div>
      <div className="flex flex-row justify-evenly pb-10">
        <div>
          <input
            className="text-emerald-800 rounded-full bg-white"
            type="checkbox"
            id="test"
            name="test"
            value="test"
          />
          <label className="pl-2" htmlFor="test">
            TESTS
          </label>
        </div>
        <div>
          <input
            className="text-emerald-800 rounded-full bg-white"
            type="checkbox"
            id="exam"
            name="exam"
            value="exam"
          />
          <label className="pl-2" htmlFor="exam">
            EXAMS
          </label>
        </div>
      </div>
      <div className="flex justify-center">
        <Button buttonText={"Search"} />
      </div>
    </form>
  );
};

export default PostForm;
