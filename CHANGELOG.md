# Changelog — 2026-10-26

## Bilingual consolidation
- Preserve the existing 7,100 Simplified Chinese expansion entries and 7,100 English expansion entries; add an explicit US English mirror for expansion additions.
- Extend the optional Linkle dialogue adaptation to EU/US English while preserving Simplified Chinese.
- Use English package/option names, descriptions and English-facing documentation; retain Chinese documentation and author credit.
- Update the title credit's English display and default trial label without changing Nintendo copyright or other layouts.

## Previously fixed content retained
- Retain r4 scene, NPC namespace, savedata/quest, LoadBalancer and RSTB protection work.
- Consolidate the five diagnosed Linkle support-bone allocation guards inside the optional equipment compatibility scope.
- Keep the selected village music's two legacy/current names, event users, registry and map trigger in the same optional folder.

## Village music level
- Lower both village music definitions from 0.45 to 0.25. Keep BARS timing, looping and the BFSTM audio bytes unchanged.
- Preserve the main package's LaboursShrine BARS registration.
- Rebuild SLink from native + the two village users, excluding unrelated shortcut sound modifications from a private integration snapshot.

## Not included
DAR combat system, standalone martial-arts/trial packages, NPDM/hooks, other clothing mods, and all other separately installed library mods are not folded into this Second Wind BNP.

## Test boundary
The earlier music route was reported working by the user on 2026-10-26. The new bilingual combinations and 0.25 gain have static/round-trip validation but still require in-game regression checks.

## Text verification summary

Main expansion text: 7,100 entries per language (CNzh, EUen, USen). Optional Linkle dialogue: 975 Simplified Chinese entries, plus 865 entries for each English region. English output: 378 per-table MSBT round trips passed; controls and entry attributes preserved. English and Chinese counts differ because neutral English lines need no gender/address edit, while additional English-specific references are adapted.

## AI-assisted preparation
Artificial intelligence assisted dialogue adaptation, troubleshooting, scripts and verification documentation. Context review and offline format checks were performed, but no claim of complete in-game verification is made. This disclosure grants no new rights over upstream assets.
