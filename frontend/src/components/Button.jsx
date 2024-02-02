function Button({ buttonText }) {
  return (
    <button
      className="rounded-full bg-emerald-500 w-fit p-3 shadow-md hover:bg-emerald-600 active:bg-emerald-700 active:translate-y-0.5 font-bold"
      type="button"
      name={buttonText}
    >
      {buttonText}
    </button>
  );
}

export default Button;
