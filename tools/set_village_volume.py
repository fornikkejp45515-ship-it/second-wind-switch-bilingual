"""Copy a prepared music option and update only its two village gain parameters.
Requires oead. No installation, merge, export, or live game changes are performed.
"""
import argparse,shutil,json
from pathlib import Path
import oead
NAMES={"OrdonVillageBgm","SWOutsetVillageBgm"}
KEY="Sound/Music/MusicList.bmscdef"
BASE="01007EF00011E000/romfs/Pack/Bootup.pack"


def set_values(node,gain):
    count=0
    for obj in node.objects.values():
        if "Name" in obj.params and str(obj.params["Name"].v) in NAMES:
            obj.params["Volume"]=oead.aamp.Parameter(oead.F32(gain));count+=1
    for child in node.lists.values():count+=set_values(child,gain)
    return count


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_option",type=Path);ap.add_argument("output_option",type=Path)
    ap.add_argument("--gain",type=float,default=0.25)
    args=ap.parse_args();assert 0<=args.gain<=1
    src=args.input_option.resolve(strict=True);dst=args.output_option.resolve()
    assert src!=dst and src not in dst.parents and not dst.exists()
    shutil.copytree(src,dst)
    pack=dst/BASE;a=oead.Sarc(pack.read_bytes());files={str(f.name):bytes(f.data) for f in a.get_files()}
    music=oead.aamp.ParameterIO.from_binary(files[KEY]);assert set_values(music,args.gain)==2
    files[KEY]=bytes(music.to_binary());w=oead.SarcWriter.from_sarc(a)
    w.files[KEY]=files[KEY];pack.write_bytes(bytes(w.write()[1]))
    log=dst/"logs/deepmerge.aamp";deep=oead.aamp.ParameterIO.from_binary(log.read_bytes())
    assert set_values(deep,args.gain)==2;log.write_bytes(bytes(deep.to_binary()))
    # Gain changes do not increase the serialized parameter count or size.
    print(json.dumps({"output_option":str(dst),"gain":args.gain,"names":sorted(NAMES),"manager_executed":False},indent=2))


if __name__=="__main__":main()
