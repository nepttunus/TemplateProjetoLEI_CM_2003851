from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osint-evidence",
        description="Captura e verificação de evidência digital para o MVP de OSINT.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    capture_parser = subparsers.add_parser(
        "capture",
        help="Captura uma página web e cria um pacote de evidência.",
    )
    capture_parser.add_argument("url", help="URL alvo a capturar.")
    capture_parser.add_argument(
        "--output-dir",
        default="output",
        help="Diretório base onde a evidência será guardada.",
    )
    capture_parser.add_argument(
        "--timeout-ms",
        type=int,
        default=30000,
        help="Timeout da navegação em milissegundos.",
    )
    capture_parser.add_argument(
        "--headed",
        dest="headless",
        action="store_false",
        default=True,
        help="Mostra o browser durante a captura.",
    )

    verify_parser = subparsers.add_parser(
        "verify",
        help="Verifica a integridade de uma pasta de evidência ou ficheiro ZIP.",
    )
    verify_parser.add_argument(
        "path",
        help="Caminho para a pasta de evidência ou para o ZIP gerado.",
    )

    return parser
