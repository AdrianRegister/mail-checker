import { testEmailData } from '../../../backend/testEmailData';

const DataReadout = () => {
  return (
    <div className="max-h-96 overflow-y-auto mx-auto col-span-2">
      <table className="table-auto border-separate border-spacing-2">
        <tbody>
          <tr>
            <th>Level</th>
            <th>Type</th>
            <th>Student name</th>
            <th>Teacher name</th>
          </tr>
          {testEmailData.map((email, index) => {
            const { level, type, studentName, teacherName } = email;
            return (
              <tr key={index}>
                <td className="whitespace-nowrap">
                  <p>{level}</p>
                </td>
                <td className="whitespace-nowrap">
                  <p>{type}</p>
                </td>
                <td className="whitespace-nowrap">
                  <p>{studentName}</p>
                </td>
                <td className="whitespace-nowrap">
                  <p>{teacherName}</p>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default DataReadout;
