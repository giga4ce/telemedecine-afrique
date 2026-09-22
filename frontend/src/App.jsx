// Static single page for the POC skeleton (SPEC-02).
// No API client, no routing, no business logic — enriched in SPEC-13.
export default function App() {
  return (
    <main
      style={{
        fontFamily: "system-ui, sans-serif",
        display: "flex",
        minHeight: "100vh",
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "column",
        gap: "0.5rem",
        color: "#1f2937",
      }}
    >
      <h1>POC Téléradiologie</h1>
      <p>Application démarrée — squelette frontend (SPEC-02).</p>
    </main>
  );
}
