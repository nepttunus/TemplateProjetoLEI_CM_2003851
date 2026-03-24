async function getActiveTabUrl() {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tabs || tabs.length === 0) {
    return null;
  }
  return tabs[0].url || null;
}

async function sendCaptureRequest(url) {
  const response = await fetch("http://127.0.0.1:8000/capture", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      url,
      output_dir: "output",
      timeout_ms: 30000,
      headless: true,
      actor: "browser_extension"
    })
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  return await response.json();
}

document.addEventListener("DOMContentLoaded", async () => {
  const urlElement = document.getElementById("currentUrl");
  const statusElement = document.getElementById("status");
  const captureButton = document.getElementById("captureBtn");
  const runDirElement = document.getElementById("runDir");
  const zipPathElement = document.getElementById("zipPath");

  let activeUrl = null;

  try {
    activeUrl = await getActiveTabUrl();
    urlElement.textContent = activeUrl || "Não foi possível obter o URL ativo.";
  } catch (error) {
    urlElement.textContent = "Erro ao obter o URL ativo.";
  }

  captureButton.addEventListener("click", async () => {
    if (!activeUrl) {
      statusElement.textContent = "Não existe URL ativa para capturar.";
      return;
    }

    statusElement.textContent = "A executar captura...";
    runDirElement.textContent = "Em processamento...";
    zipPathElement.textContent = "Em processamento...";
    captureButton.disabled = true;

    try {
      const result = await sendCaptureRequest(activeUrl);
      statusElement.textContent = "Captura concluída com sucesso.";
      runDirElement.textContent = result.run_dir || "N/D";
      zipPathElement.textContent = result.zip || "N/D";
    } catch (error) {
      statusElement.textContent = "Erro ao contactar o motor local.";
      runDirElement.textContent = "Erro.";
      zipPathElement.textContent = "Erro.";
    } finally {
      captureButton.disabled = false;
    }
  });
});
