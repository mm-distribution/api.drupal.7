# ThemeTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/theme.test`](_file.md), lines 11–167 · [local source](../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L11-L167)
- **Module/theme:** batch_test

## Signature

```php
class ThemeTestCase extends DrupalWebTestCase
```

## Documentation

```text
Unit tests for the Theme API.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](ThemeTestCase/getInfo.md)
- [setUp()](ThemeTestCase/setUp.md)
- [testThemeSuggestions()](ThemeTestCase/testThemeSuggestions.md) — Test function theme_get_suggestions() for SA-CORE-2009-003.
- [testPreprocessForSuggestions()](ThemeTestCase/testPreprocessForSuggestions.md) — Ensures preprocess functions run even for suggestion implementations.
- [testFrontPageThemeSuggestion()](ThemeTestCase/testFrontPageThemeSuggestion.md) — Ensure page-front template suggestion is added when on front page.
- [testAlter()](ThemeTestCase/testAlter.md) — Ensures theme hook_*_alter() implementations can run before anything is rendered.
- [testCSSOverride()](ThemeTestCase/testCSSOverride.md) — Ensures a theme's .info file is able to override a module CSS file from being added to the page.
- [testRegistryRebuild()](ThemeTestCase/testRegistryRebuild.md) — Ensures the theme registry is rebuilt when modules are disabled/enabled.
- [testListThemes()](ThemeTestCase/testListThemes.md) — Test the list_themes() function.
- [testThemeGetSetting()](ThemeTestCase/testThemeGetSetting.md) — Test the theme_get_setting() function.
- [testDrupalAddRegionContent()](ThemeTestCase/testDrupalAddRegionContent.md) — Test the drupal_add_region_content() function.

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
