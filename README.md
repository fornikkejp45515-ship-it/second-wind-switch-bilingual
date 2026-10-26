# Second Wind — Switch Bilingual Edition

Second Wind adds a lot to discover in Hyrule. This project is a small effort to make that adventure easier to enjoy on Switch, whether you read English or Simplified Chinese, and whether you play as Link or use a separately installed Linkle mod.

The aim is not to replace the original team's work. It is to bring the port's fixes, language options and optional village music together in one understandable package, with clear credits and fewer loose patches to keep track of. There are still rough edges to test, and honest feedback is welcome.

**AI assistance disclosure:** Artificial intelligence was used to help with dialogue adaptation, troubleshooting, script preparation and validation summaries. The work also includes context-specific review and file-format checks; that is not a claim that every line or scene has been verified in game. Original creators remain credited, and AI assistance does not change their rights or permissions.

Unofficial Switch integration of **Second Wind 1.9.14-alpha-6**, with **English (EU/US)** and **Simplified Chinese** in one BNP. Package names, descriptions, and option labels are in English. Port and integration: **Mi Laoshu & Kugou (米老鼠和酷狗)**.

## Requirements
- A legally obtained copy of Breath of the Wild for Switch, with the update/DLC required by Second Wind.
- A compatible Switch-profile BNP mod manager. Install and merge through your manager; this BNP is **not** a direct romfs overlay.
- The Linkle character mod is **not included**. Install it separately only if using the Linkle compatibility options.

## Included options
| Option | Default | Purpose |
|---|---|---|
| Eventide Island Fix [Required] | On | Existing actor-limit/Eventide compatibility |
| Shrine Overhaul | On | Optional redesigns of existing shrines |
| Linkle: Second Wind Equipment Compatibility | Off | SW equipment adaptation and five support-bone budget safeguards; requires Linkle |
| Linkle: Bilingual Dialogue Compatibility | Off | Contextual Linkle names/forms of address in English and Simplified Chinese |
| Village Music: Outset Island [Non-Commercial Audio] | Off | Optional village music, including legacy/current name compatibility |

The manager UI is English. **The game's configured text language** selects English or Simplified Chinese; selecting Linkle dialogue does not change the game language. EUen and USen both receive explicit English additions.

## Installation and upgrade
1. Back up your current mod configuration and saves.
2. Replace the earlier Second Wind comparison/r4 package with this package; do not install both core packages together.
3. Select your options. Keep both Linkle options off if playing as Link.
4. Remove/disable the old standalone village music test BNPs. The selected music option includes that work; do not stack older versions.
5. The five-clothing budget patch is included only when Linkle equipment compatibility is selected. Do not require the separate duplicate patch in that combination.
6. Merge/export using your own manager, then completely close the emulator before deploying the new output. Do not directly copy the sparse Bootup.pack out of the BNP.
7. Avoid leaving an older duplicate DLC export enabled in a second mod location. The two music names are compatible, but that does not resolve unrelated duplicate-map conflicts.

## Village music
Both `OrdonVillageBgm` and the legacy `SWOutsetVillageBgm` use the same supplied Outset Island stream. Its MusicList volume is **0.25 instead of 0.45**; other music and emulator audio settings are unchanged. The stream is not re-encoded. The working route previously received a user-confirmed playback result; the reduced level still needs in-game listening.

The optional SLink database is built from native data plus only the two village event users, not a user's private mod snapshot. It does not carry independent QuickSelect sound changes. Another mod replacing SLink2DB may need a shared database; this release does not claim generic SLink merging by every manager.

## Validation status
Offline validation checks archive integrity, option metadata, language logs, MSBT control-node round trips, resource budget floors, title-layout text edits, music registration/event chains, and preservation of baseline gameplay logs. New bilingual combinations, English layout in all scenes, and the reduced village gain are **not yet certified by a full in-game regression test**.

## Permissions and credits
See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The contributor states that Second Wind's original author has granted permission for this port/publication. Linkle content in this package is described as compatibility material, not the separately distributed Linkle character mod. The supplied Arcade Player recording is reported to permit **non-commercial** use. These statements are recorded as contributor-provided permission information, not independent verification or a blanket license for every game/third-party asset.

No game ROM, title keys, firmware, emulator binary, save, memory dump, or private diagnostic log is part of this publication.

---

## 中文说明
这是 Second Wind 1.9.14-alpha-6 的非官方 Switch 中英整合版。一个 BNP 同时保留简体中文和欧/美英文，包介绍及所有选项使用英文；游戏里显示哪种语言由游戏的语言设置决定。

本包不含林可儿角色本体。玩林克时不要勾选两个 Linkle 选项；使用林可儿时需另装本体。已修复的村庄音乐收进可选项，音量从0.45调低至0.25，音轨不重新编码。旧的独立配乐测试补丁不要继续叠加。

用本版替换旧Second Wind核心包，再由你自行合并导出。完全退出模拟器后再部署。BNP里的Bootup是差异包，不能直接拿出来覆盖。注意停用另一加载目录中重复的旧DLC导出；双名称兼容仅处理音乐，不处理其他地图覆盖。

本次未自动安装、运行BCML或修改实际游戏目录。中英新增组合与降音量仍需游戏内测试。原作者许可及音源非商用许可由提供者说明，各素材权利保留。

## Text verification summary

Main expansion text: 7,100 entries per language (CNzh, EUen, USen). Optional Linkle dialogue: 975 Simplified Chinese entries, plus 865 entries for each English region. English output: 378 per-table MSBT round trips passed; controls and entry attributes preserved. English and Chinese counts differ because neutral English lines need no gender/address edit, while additional English-specific references are adapted.

### 关于人工智能辅助
本项目使用了人工智能，辅助对话适配、问题排查、脚本编写和验证说明整理；也进行了按语境检查与文件格式校验。这不代表所有台词、场景和组合都已经在游戏中验证。原作者的贡献、署名和素材权利不会因此改变。希望这份整理能让你少折腾一些，多花一点时间好好冒险。
