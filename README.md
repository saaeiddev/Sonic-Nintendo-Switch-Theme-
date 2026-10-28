# Sonic Nintendo Switch Theme

**Creator: Amir Saeid Dehghan** · [فارسی](README.fa.md)

![Green Hill artwork](artwork/sonic-green-hill-source.png)

> **Experimental work in progress.** This is not a finished release. The seven packages have passed basic ZIP, metadata and image checks, but have not yet been verified with NXThemeTool, installed with NXThemes Installer or tested on a Switch. The Home package contains six custom applet icons. Packages use stock system layouts; no custom layout or hardware screenshots are included. The illustrations below are schematic mockups, not a promise of the actual system layout.

A fan-made Sonic visual direction combining Green Hill, checkerboard cliffs, golden rings and the heroes of the series. The original generated artwork is retained under `artwork/`; all backgrounds are 1280 × 720 baseline JPEGs.

## Screen previews

**Illustrative mockups, not console screenshots.** These images use the packaged backgrounds and home icon artwork, but the simulated interface panels and labels are not included in the `.nxtheme` packages. Real placements, appearance and readability depend on your firmware and system theme.

![Overview of all seven illustrative previews](previews/overview.jpg)

| Screen | Preview |
| --- | --- |
| Home Menu | ![Home Menu illustrative preview](previews/home.jpg) |
| Lock Screen | ![Lock Screen illustrative preview](previews/lock.jpg) |
| All Applications | ![All Applications illustrative preview](previews/apps.jpg) |
| Settings | ![Settings illustrative preview](previews/set.jpg) |
| User Profile | ![User Profile illustrative preview](previews/user.jpg) |
| News | ![News illustrative preview](previews/news.jpg) |
| Player Selection | ![Player Selection illustrative preview](previews/psl.jpg) |

## Menu targets

| File | System section |
| --- | --- |
| `packages/sonic-home.nxtheme` | Home Menu |
| `packages/sonic-lock.nxtheme` | Lock Screen |
| `packages/sonic-apps.nxtheme` | All Applications |
| `packages/sonic-set.nxtheme` | System Settings |
| `packages/sonic-user.nxtheme` | User Profile |
| `packages/sonic-news.nxtheme` | News |
| `packages/sonic-psl.nxtheme` | Player Selection |

## Compatibility and installation

Custom themes require a compatible, modified Switch running Atmosphère and NXThemes Installer. Stock consoles do not support `.nxtheme` files. These ZIP-format packages target the modern installer generation (3.0 or later); verify firmware, Atmosphère and installer compatibility using the [official project](https://github.com/exelix11/SwitchThemeInjector/releases). Because these files have not yet been checked by the official tool or on hardware, **do not treat them as a verified release**.

After independent validation, copy the packages to `themes/` at the root of the microSD card, open NXThemes Installer, select each desired part, follow its setup prompts, and reboot. Before a system update, uninstall themes. If a theme causes a boot problem, consult the official project's recovery guidance; preserve your backups and confirm the correct title ID before removing any files.

## Building and validation

Requires Python 3 and Pillow (`python -m pip install Pillow`). Run `python scripts/build.py` from the repository root. It converts the four source PNGs to baseline JPEGs and creates one ZIP-based package per target. The script checks archive CRCs, manifest values, image dimensions, icon dimensions and JPEG progressive encoding. Run `python scripts/make_icons.py` to regenerate the icon sources, and `python scripts/render_previews.py` to regenerate mockups after building. It is an independent check, not a substitute for `NxThemeTool validate`, installer testing, layout/readability testing or hardware testing.

Use [NXThemeTool and NXThemes Installer](https://github.com/exelix11/SwitchThemeInjector) or [Themezer's builder](https://themezer.net/tools/nxtheme-creator) to independently validate packages and create compatible layouts. No extracted firmware or SZS files are distributed here. Custom layouts may depend on firmware and require appropriate locally obtained system files.

## Project files

```text
artwork/      Original generated artwork (PNG)
backgrounds/  1280 × 720 package source images (JPEG)
packages/     Experimental NXTheme packages
icons/        Six transparent 64 × 56 Home applet icons
previews/     Illustrative interface mockups (not console captures)
scripts/      Reproducible build, icon and preview scripts
README.md     English documentation
README.fa.md  Persian documentation
```

To customize, edit or replace the artwork, preserve the source file names, then rebuild. Test contrast against the actual menu and validate each target before release. The art shown above is an illustration, not a console screenshot.

## Credits

Project creator: **Amir Saeid Dehghan**. Artwork generated for this fan project. Sonic the Hedgehog and related characters and trademarks belong to SEGA; Nintendo Switch and Nintendo trademarks belong to Nintendo. This project is unofficial, not endorsed by or affiliated with either company.
