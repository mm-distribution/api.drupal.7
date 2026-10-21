# ModuleDependencyTestCase::testThemeMetaData()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 589–598 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L589-L598)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testThemeMetaData()
```

## Documentation

```text
Tests whether the correct theme metadata is returned.
```

## Code

```php
  function testThemeMetaData() {
    // Generate the list of available themes.
    $themes = system_rebuild_theme_data();
    // Check that the mtime field exists for the bartik theme.
    $this->assertTrue(!empty($themes['bartik']->info['mtime']), 'The bartik.info file modification time field is present.');
    // Use 0 if mtime isn't present, to avoid an array index notice.
    $test_mtime = !empty($themes['bartik']->info['mtime']) ? $themes['bartik']->info['mtime'] : 0;
    // Ensure the mtime field contains a number that is greater than zero.
    $this->assertTrue(is_numeric($test_mtime) && ($test_mtime > 0), 'The bartik.info file modification time field contains a timestamp.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
