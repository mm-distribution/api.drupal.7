# BlockInvalidRegionTestCase::testBlockInInvalidRegion()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 860–901 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L860-L901)
- **Class:** [BlockInvalidRegionTestCase](../BlockInvalidRegionTestCase.md)
- **Module/theme:** block

## Signature

```php
function testBlockInInvalidRegion()
```

## Documentation

```text
Tests that blocks assigned to invalid regions work correctly.
```

## Code

```php
  function testBlockInInvalidRegion() {
    // Enable a test block in the default theme and place it in an invalid region.
    db_merge('block')
      ->key(array(
        'module' => 'block_test',
        'delta' => 'test_html_id',
        'theme' => variable_get('theme_default', 'stark'),
      ))
      ->fields(array(
        'status' => 1,
        'region' => 'invalid_region',
        'cache' => DRUPAL_NO_CACHE,
      ))
      ->execute();

    $warning_message = t('The block %info was assigned to the invalid region %region and has been disabled.', array('%info' => t('Test block html id'), '%region' => 'invalid_region'));

    // Clearing the cache should disable the test block placed in the invalid region.
    $this->drupalPost('admin/config/development/performance', array(), 'Clear all caches');
    $this->assertRaw($warning_message, 'Enabled block was in the invalid region and has been disabled.');

    // Clear the cache to check if the warning message is not triggered.
    $this->drupalPost('admin/config/development/performance', array(), 'Clear all caches');
    $this->assertNoRaw($warning_message, 'Disabled block in the invalid region will not trigger the warning.');

    // Place disabled test block in the invalid region of the default theme.
    db_merge('block')
      ->key(array(
        'module' => 'block_test',
        'delta' => 'test_html_id',
        'theme' => variable_get('theme_default', 'stark'),
      ))
      ->fields(array(
        'region' => 'invalid_region',
        'cache' => DRUPAL_NO_CACHE,
      ))
      ->execute();

    // Clear the cache to check if the warning message is not triggered.
    $this->drupalPost('admin/config/development/performance', array(), 'Clear all caches');
    $this->assertNoRaw($warning_message, 'Disabled block in the invalid region will not trigger the warning.');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
