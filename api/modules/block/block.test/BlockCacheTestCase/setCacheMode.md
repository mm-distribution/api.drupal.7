# BlockCacheTestCase::setCacheMode()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 662–672 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L662-L672)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
private function setCacheMode($cache_mode)
```

## Documentation

```text
Private helper method to set the test block's cache mode.
```

## Code

```php
  private function setCacheMode($cache_mode) {
    db_update('block')
      ->fields(array('cache' => $cache_mode))
      ->condition('module', 'block_test')
      ->execute();

    $current_mode = db_query("SELECT cache FROM {block} WHERE module = 'block_test'")->fetchField();
    if ($current_mode != $cache_mode) {
      $this->fail(t('Unable to set cache mode to %mode. Current mode: %current_mode', array('%mode' => $cache_mode, '%current_mode' => $current_mode)));
    }
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
