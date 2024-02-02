import Button from "./components/Button.jsx";
import PostForm from "./components/PostForm.jsx";

function App() {
  return (
    <div className="bg-neutral-300 w-screen h-screen font-sans tracking-wider">
      <h2 className="text-center text-black text-xl font-bold pt-2 pb-2">
        Frontend
      </h2>
      <div className="grid grid-cols-4 gap-2 w-3/4 mx-auto">
        <div className="mx-auto">
          <Button buttonText={"placeholder"} /> {/* REMEMBER PROPS! */}
        </div>
        <div className="mx-auto col-span-2">
          <PostForm teacherNameValue={""} /> {/* REMEMBER PROPS! */}
        </div>
      </div>
    </div>
  );
}

export default App;
