#!/usr/bin/env python3
"""Export the editable diagrams used by dissertation.tex to vector PDF."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


IMAGE_DIR = Path(__file__).resolve().parent
DRAWIO_DIAGRAMS = (
    "intro_overall_problem",
    "ch1_edge_need_concept",
    "ch1_method_logic",
    "ch2_model_mapping",
    "ch2_system_graph",
    "ch3_auction_layer",
    "ch4_arch_qmix",
    "ch4_adaptive_control",
    "ch5_ample_amr_concept",
    "ch5_ample_architecture",
    "ch6_warehouse_scenario",
    "ch7_prototype_architecture",
)
SVG_DIAGRAMS = ("ch1_edge_computing", "ch3_auction")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="Diagram names; default: all")
    args = parser.parse_args()
    names = set(args.names or DRAWIO_DIAGRAMS + SVG_DIAGRAMS)
    unknown = names.difference(DRAWIO_DIAGRAMS + SVG_DIAGRAMS)
    if unknown:
        parser.error("Unknown diagrams: " + ", ".join(sorted(unknown)))

    drawio = os.environ.get("DRAWIO") or shutil.which("drawio")
    mac_drawio = Path("/Applications/draw.io.app/Contents/MacOS/draw.io")
    if not drawio and mac_drawio.is_file():
        drawio = str(mac_drawio)
    rsvg = shutil.which("rsvg-convert")
    if names.intersection(DRAWIO_DIAGRAMS) and not drawio:
        parser.error("Install draw.io Desktop or set DRAWIO to its executable")
    if names.intersection(SVG_DIAGRAMS) and not rsvg:
        parser.error("Install rsvg-convert (librsvg)")

    # Write to a temporary file first, so a failed export keeps the previous PDF.
    with tempfile.TemporaryDirectory(prefix="dissertation-diagrams-") as directory:
        for name in DRAWIO_DIAGRAMS + SVG_DIAGRAMS:
            if name not in names:
                continue
            output = Path(directory) / (name + ".pdf")
            if name in DRAWIO_DIAGRAMS:
                command = [
                    drawio, "--export", "--format", "pdf", "--crop",
                    "--border", "8", "--output", str(output),
                    str(IMAGE_DIR / "drawio" / (name + ".drawio")),
                ]
            else:
                command = [
                    rsvg, "--format", "pdf", "--output", str(output),
                    str(IMAGE_DIR / "svg" / (name + ".svg")),
                ]
            subprocess.run(command, check=True, timeout=60)
            if not output.is_file() or output.stat().st_size < 100:
                raise RuntimeError("Missing PDF export: " + name)
            shutil.copyfile(output, IMAGE_DIR / output.name)
            print(name + ".pdf", flush=True)


if __name__ == "__main__":
    main()
