from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Captura e verificação de evidência digital web."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    capture_parser = subparsers.add_parser(
        "capture",
        help="Capturar uma página web e gerar artefactos de evidência.",
    )
    capture_parser.add_argument("url", help="URL a capturar")
    capture_parser.add_argument(
        "--output-dir",
        default="output",
        help="Diretório base para guardar execuções de captura",
    )
    capture_parser.add_argument(
        "--timeout-ms",
        type=int,
        default=30000,
        help="Timeout da navegação em milissegundos",
    )
    capture_parser.add_argument(
        "--headed",
        action="store_true",
        help="Abre o browser em modo visível",
    )

    verify_parser = subparsers.add_parser(
        "verify",
        help="Verificar a integridade de uma pasta de execução ou ZIP.",
    )
    verify_parser.add_argument("target", help="Caminho para pasta ou ZIP a verificar")

    return parser
