# Second Wind 1.9.14-alpha-6 — Switch Bilingual Edition

For players who want to spend less time juggling patches and more time exploring Hyrule: this release gathers the port, English/Chinese text, optional Linkle adaptation and quieter village music into one package. Thank you to the original creators and to everyone who helped test the rough edges.

**AI-assisted project:** AI helped with dialogue adaptation, troubleshooting, scripts and validation summaries. Context review and format checks complement that assistance; they do not replace in-game testing.

## One complete BNP, English interface, two text languages
- Keeps Simplified Chinese; explicitly supports English EU and US.
- Main expansion: 7,100 entries per language.
- Optional Linkle dialogue: 975 Chinese entries and 865 entries for each English region.
- All package/option names and descriptions are in English. Game text follows the game's configured language, not an artificial in-game language switch.
- Linkle character mod is not included; compatibility options require it separately.

## Consolidated fixes and quieter music
- Keeps r4 LoadBalancer, scene, gameplay/savedata/quest and resource-budget work.
- Keeps the original Eventide and Shrine Overhaul options.
- Includes five diagnosed support-bone budget safeguards in Linkle equipment compatibility.
- Includes village audio registration, two event names and the optional map trigger together.
- Village MusicList gain changes from 0.45 to 0.25 only; the original supplied stream bytes, loop points and other music are unchanged.
- Preserves LaboursShrine audio registration and excludes unrelated shortcut-event changes from a private mod snapshot.

## Install
Replace the previous Second Wind core, do not stack old core versions. Disable earlier standalone village-music test BNPs. Select only the optional features you use, merge/export through your own Switch-profile manager, close the emulator fully, then deploy. Sparse PACK files inside the BNP are not direct overlays.

## Permissions
The contributor states that the original Second Wind author has permitted this publication. The optional Linkle material is an adaptation patch, not the Linkle base. The supplied Arcade Player recording is reported to permit non-commercial use. Each source retains its own rights; see THIRD_PARTY_NOTICES.md. No ROM, keys, firmware, save, private diagnostics or tool executables are included in the repository.

## Validation
4,110 staged files; archive integrity and full extraction/hash verification; MSBT control-node round trips; measured message allocations; unchanged baseline gameplay logs and optional shrines. The earlier audio route was user-confirmed working. This new combined bilingual build and the quieter gain still need full in-game regression testing.
