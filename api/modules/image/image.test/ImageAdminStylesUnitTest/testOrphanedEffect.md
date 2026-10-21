# ImageAdminStylesUnitTest::testOrphanedEffect()

- **Type:** Method
- **File:** [`modules/image/image.test`](../_file.md), lines 928–935 · [local source](../../../../../source/modules/image/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test#L928-L935)
- **Class:** [ImageAdminStylesUnitTest](../ImageAdminStylesUnitTest.md)
- **Module/theme:** image

## Signature

```php
function testOrphanedEffect()
```

## Documentation

```text
Test disabling a module providing an effect in use by an image style.
```

## Code

```php
  function testOrphanedEffect() {
    // This will not check whether anything depends on the module.
    module_disable(array('image_module_test'), FALSE);
    $this->drupalGet('admin/config/media/image-styles');
    $this->assertText('Test Image Style', 'Image style with an orphaned effect displayed in the list of styles.');
    $image_log = db_query_range('SELECT message FROM {watchdog} WHERE type = :type ORDER BY wid DESC', 0, 1, array(':type' => 'image'))->fetchField();
    $this->assertEqual('Image style %style_name has an effect %effect_name with no definition.', $image_log, 'A watchdog message was logged for the broken image style effect');
  }
```

---
_Drupal 7.103 · [modules/image/image.test](https://github.com/drupal/drupal/blob/7.103/modules/image/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
