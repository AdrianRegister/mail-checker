import { testEmailData } from '../../../backend/testEmailData';

const DataReadout = () => {
  return (
    <div className="max-h-96 overflow-y-auto">
      <table>
        <thead>
          <tr>
            <th>Info</th>
          </tr>
        </thead>
        <tbody>
          {testEmailData.map((email, index) => {
            return (
              <tr key={index}>
                <td className="whitespace-nowrap">
                  <p>{email}</p>
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
