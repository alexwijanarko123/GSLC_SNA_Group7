import './App.css'

function App() {
  return (
    <div className="dashboard-container">
      <header className="header">
        <h1>🔒 PaySecure Internal Dashboard</h1>
        <div className="user-info">
          <span>Admin System</span>
          <span className="badge">Kelompok 7 SNA</span>
        </div>
      </header>

      <main className="main-content">
        <section className="metrics">
          <div className="card">
            <h3>Total Saldo Sistem</h3>
            <p className="amount">Rp 4.250.000.000</p>
          </div>
          <div className="card">
            <h3>Transaksi Berhasil (Hari ini)</h3>
            <p className="amount">1,245</p>
          </div>
          <div className="card alert">
            <h3>Anomali Terdeteksi</h3>
            <p className="amount">3</p>
          </div>
        </section>

        <section className="transactions">
          <h2>Log Transaksi Terakhir</h2>
          <table>
            <thead>
              <tr>
                <th>ID Transaksi</th>
                <th>Waktu</th>
                <th>Nominal</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>TRX-00192A</td>
                <td>10:45 WIB</td>
                <td>Rp 15.000.000</td>
                <td className="status success">Sukses</td>
              </tr>
              <tr>
                <td>TRX-00192B</td>
                <td>10:42 WIB</td>
                <td>Rp 2.500.000</td>
                <td className="status success">Sukses</td>
              </tr>
              <tr>
                <td>TRX-00192C</td>
                <td>10:30 WIB</td>
                <td>Rp 45.000.000</td>
                <td className="status warning">Review Manual</td>
              </tr>
              <tr>
                <td>TRX-00192D</td>
                <td>10:15 WIB</td>
                <td>Rp 150.000</td>
                <td className="status failed">Gagal</td>
              </tr>
            </tbody>
          </table>
        </section>
      </main>
    </div>
  )
}

export default App