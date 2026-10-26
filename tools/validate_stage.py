"""Read-only checks for a staged bilingual BNP; never starts a mod manager."""
import argparse,json,hashlib,re
from pathlib import Path


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage",type=Path)
    args=ap.parse_args();root=args.stage.resolve(strict=True)
    info=json.loads((root/"info.json").read_text("utf-8-sig"))
    assert info["platform"]=="switch"
    visible=[info["name"],info["desc"]]
    options=[v for values in info["options"].values() for v in values]
    for option in options:
        visible.extend([option["name"],option["desc"]])
        folder=option["folder"]
        assert folder and "/" not in folder and "\\" not in folder and folder not in [".",".."]
        assert (root/"options"/folder).is_dir()
    assert not any(re.search(r"[\u3400-\u9fff]",s) for s in visible)
    counts={}
    for label,folder in [("main",root),("linkle",root/"options/Linkle Dialogue Compatibility")]:
        tx=json.loads((folder/"logs/texts.json").read_text("utf-8-sig"))
        assert {"CNzh","EUen","USen"}<=set(tx)
        counts[label]={k:sum(len(v) for v in tables.values()) for k,tables in tx.items()}
        for language in ["EUen","USen"]:
            for entries in tx[language].values():
                for entry in entries.values():
                    for node in entry.get("contents",[]):
                        if "text" in node:assert not re.search(r"[\u3400-\u9fff]",node["text"])
    files=[]
    for path in sorted(root.rglob("*")):
        if not path.is_file():continue
        rel=path.relative_to(root).as_posix()
        assert not any(x in ["exefs","exefs_patches"] for x in path.relative_to(root).parts)
        files.append({"path":rel,"bytes":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    print(json.dumps({"files":len(files),"text_entries":counts,"manager_executed":False},indent=2))


if __name__=="__main__":main()
